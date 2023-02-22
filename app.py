import datetime, json, os
from flask import Flask, render_template, request,  redirect, url_for, flash

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

comments = []
formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
filename = os.path.join(app.static_folder, 'data', 'spam.json')
with open(filename) as test_file:
    spamData = json.load(test_file)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        comment_content = request.form.get("content")
        user_name = request.form.get("userName")
        for i in spamData:
            if i in comment_content:
                flash('Your message looks like spam. Please rephrase it')
                return redirect(url_for('home'))
        comments.append((comment_content, formatted_date, user_name))
    return render_template("home.html", comments=comments, spamData=spamData)


@app.get("/recent")
def recentPage():
    return render_template("recent.html", comments=comments)

