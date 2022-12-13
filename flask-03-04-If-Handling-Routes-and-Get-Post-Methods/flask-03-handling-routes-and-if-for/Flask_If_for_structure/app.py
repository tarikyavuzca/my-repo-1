from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
  return render_template('index.html', message='This is my first condition experience')


@app.route('/mylist')
def header():
  myNames = ['Yavuz', 'Omer', 'Erkan']
  return render_template('body.html', object=myNames)



if __name__ == '__main__':
  app.run(debug=True)