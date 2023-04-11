import os
import openai

from flask import Flask, render_template, request

app = Flask(__name__, static_folder="static", static_url_path="/static")
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        weather = request.form["weather"]
        mood = request.form["mood"]
        content = request.form["content"]
        image_prompt = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
        {"role": "user", "content": "'반에서 1등했다'한 강아지를 관계대명사를 이용해서 영어로 바꿔줘"},
        {"role": "assistant", "content": "My dog, who came in first in his class"},
        {"role": "user", "content": f"'{content}'한 강아지를 관계대명사를 이용해서 영어로 바꿔줘"},
        ])
        print(image_prompt)
        image = openai.Image.create(
            prompt=f"{image_prompt}",
            n=1,
            size="256x256"
        )
        print(image)
        title = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
        {"role": "user", "content": f"'날씨:{weather},기분:{mood},사건:{content}'의 내용으로 쓸 일기의 제목을 유머러스하게 적어줘. "},
        ])
        print(title)
        contents = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
        {"role": "user", "content": f"'날씨:{weather},기분:{mood},사건:{content}' 의 내용으로 5줄로 일기를 적어줘"},
        ])
        print(contents)
        return render_template("result.html", title=title.choices[0].message.content, contents=contents.choices[0].message.content, image_url = image['data'][0]['url'])
    return render_template("write.html")

if __name__ == "__main__":
    app.run(debug=True)