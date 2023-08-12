#Создать страницу, на которой будет форма для ввода имени и электронной почты, 
#при отправке которой будет создан cookie-файл
#с данными пользователя, а также будет произведено перенаправление на страницу приветствия,
#где будет отображаться имя пользователя.
#На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл
#с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = redirect('welcom')
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return response  
    return render_template('task01.html')

@app.route('/welcom', methods = ['GET', 'POST'])
def welcom():
    name = request.cookies.get('name')
    email = request.cookies.get('email')
    return render_template('welcom.html', name=name, email=email)

@app.route('/delcookie')
def delcookie(): 
    response = redirect('login')
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response

if __name__ == '__main__':
    app.run(debug=True)