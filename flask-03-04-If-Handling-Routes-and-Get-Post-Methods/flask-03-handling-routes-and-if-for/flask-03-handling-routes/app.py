from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# lading page
@app.route('/')
def home():
  return 'This is home page for no path, <h1> Welcome Home </h1>'

# home page
@app.route('/about')
def about():
  return '<h1> About page </h1>'


# error page
@app.route('/error')
def error():
  return '<h1> Either you encountered an error or you are not authorized! </h1>'

# admin
@app.route('/admin')
def admin():
  return redirect(url_for('error'))


# greeting page
@app.route('/<name>')
def greet(name):
  return render_template('greet.html', name=name)




# greeting admin page
@app.route('/greet-admin')
def greet_admin():
  return redirect(url_for('greet', name='Master Admin!!!'))


# showing list of 10 item page
@app.route('/list10')
def list10():
  return render_template('list10.html')


# showing even number from 1-10 page
@app.route('/evens')
def evens():
  return render_template('evens.html')




if __name__ == '__main__':
  app.run(port=80, host='0.0.0.0', debug=True)