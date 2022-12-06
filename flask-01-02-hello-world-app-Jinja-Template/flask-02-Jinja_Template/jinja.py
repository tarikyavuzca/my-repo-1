from flask import Flask
from flask import render_template

app = Flask(__name__)




# @app.route('/')
# def head(number1=10, number2=5):
#   return render_template('index.html', number1=number1, number2=number2)

# @app.route('/')
# def head():
#   return render_template('index.html', number1=10, number2=20)

@app.route('/')
def head():
  number1 = 10
  number2 = 20
  return render_template('index.html', number1=number1, number2=number2)

# @app.route('/number/<string:num1>')
# def number(num1):
#     return render_template('index.html', number1=num1, number2=20)

# @app.route('/sum')
# def number(number1=10, number2=20, sum=None):
#   sum = number1 + number2
#   return render_template('body.html', value1=number1, value2=number2, sum=sum)

@app.route('/sum')
def number():
  x=15
  y=10
  sum = x + y
  return render_template('body.html', value1=x, value2=y, sum=sum)


if __name__ == '__main__':
  
    app.run(debug=True)

# app.run(host='localhost', port=81)