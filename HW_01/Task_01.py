#Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
#и дочерние шаблоны для страниц категорий товаров и отдельных товаров. 
#Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)

class Cloth:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

@app.route('/')
def shop():
    return render_template('base.html')

@app.route('/man/')
def mens_clothing():
    mens_clothing = [Cloth('Джинсы', 52, 2500),
                    Cloth('Свитер', 54, 1500),
                    Cloth('Рубашка', 56, 3500)
                    ]
    return render_template('mens.html', mens_clothing=mens_clothing)

@app.route('/woman/')
def womans_clothing():
    womans_clothing = [Cloth('Платье', 46, 2500),
                       Cloth('Юбка', 48, 1500),
                       Cloth('Блуза', 44, 3500)
                       ]
    return render_template('womans.html', womans_clothing=womans_clothing)

@app.route('/kids/')
def kids_clothing():
    kids_clothing = [Cloth('Комбинизон', 115, 1500),
                    Cloth('Ползунки',80, 500),
                    Cloth('Распашенка', 75 , 400)
                    ]
    return render_template('kins.html', kids_clothing=kids_clothing)

if __name__ == '__main__':
    app.run(debug=True)