from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from peewee import *

import os
from Lib import *

app = Flask(__name__)

# sqlite
db = SqliteDatabase('tcf.db')


# mysql
# db = MySQLDatabase(
#     host='localhost',
#     database='tcf',
#     user='root',
#     password=''
# )

@app.route("/")
def index():
    return render_template('index.html', introduction='台中美食介紹')


@app.route("/food")
def food():
    result = Post.select().where(Post.type == 0)
    return render_template('food.html', introduction='主食餐廳介紹', result=result)


@app.route("/dessert")
def desert():
    result = Post.select().where(Post.type == 1)
    return render_template('dessert.html', introduction='甜點餐廳介紹', result=result)


@app.route("/drinks")
def drinks():
    result = Post.select().where(Post.type == 2)
    return render_template('drinks.html', introduction='飲料店介紹', result=result)


@app.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = doHash(request.form['password'])
    user = Member.select().where(Member.email == email, Member.password == password).limit(1)
    if user.exists():
        session['logged_in'] = True
        session['name'] = user[0].name
        session['email'] = user[0].email
        data = {
            'success': 0,
            'message': '登入成功'
        }
        return json.dumps(data)
    else:
        data = {
            'success': -1,
            'message': '帳號或密碼錯誤'
        }
        return json.dumps(data)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user = Member.select().where(Member.email == email)
    if not name or not email or not password:
        data = {
            'success': -1,
            'message': '請填寫完整'
        }
        return json.dumps(data)
    elif user.exists():
        data = {
            'success': -1,
            'message': '信箱已有人使用'
        }
        return json.dumps(data)
    else:
        user = Member(name=name, email=email, password=doHash(password))
        user.save()
        data = {
            'success': 0,
            'message': '註冊成功'
        }
        return json.dumps(data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


class Member(Model):
    name = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db


class Post(Model):
    name = CharField()
    address = CharField()
    time = CharField()
    phone_number = CharField()
    website = CharField()
    image = CharField()
    type = IntegerField()

    class Meta:
        database = db


db.connect()

if not (Member.table_exists() and Post.table_exists()):
    db.create_tables([Member, Post], safe=True)

users = Member.select()
posts = Post.select()
if len(users) == 0 and len(posts) == 0:
    seed(Member, Post)

db.close()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run(host='127.0.0.1', port=8000)
