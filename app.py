import datetime, json, os
from flask import Flask, render_template, request,  redirect, url_for, flash

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

comments = []
formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
spamWord = os.path.join(app.static_folder, 'data', 'spam.json')
commentsJson = os.path.join(app.static_folder, 'data', 'comments.json')

with open(spamWord) as spamWord:
    spamData = json.load(spamWord)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        comment_content = request.form.get("content")
        user_name = request.form.get("userName")
        for i in spamData:
            if i in comment_content:
                flash('Your message looks like spam. Please rephrase it')
                return redirect(url_for('home'))
        comments.append((user_name, comment_content, formatted_date))
        with open(commentsJson, 'w') as commentFile:
                json.dump(comments, commentFile)
    return render_template("home.html", comments=comments, spamData=spamData)


@app.get("/recent")
def recentPage():
    return render_template("recent.html", comments=comments)

app.run()
