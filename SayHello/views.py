from flask import flash, redirect, url_for, render_template

from app import app
import models as db

from forms import HelloForm

'''视图文件'''


@app.route('/', methods=["GET", "POST"])
def index():
    form = HelloForm()
    messages = []

    data = db.check()
    for i in data:
        i = str(i).split(":::")
        if len(i) == 3:
            messages.append({"name": i[0], "body": i[1],"timestamp":i[2]})

    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        print(name,body)
        db.add(body=body, name=name)
        flash("你的消息已经发送到达!")
        return redirect(url_for("index"))

    return render_template('index.html', form=form, messages=messages)
