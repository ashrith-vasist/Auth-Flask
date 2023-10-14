from flask import Flask, render_template,session
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secrect_key= b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def Home():
   return render_template('Home.html')

@app.route('/register',methods=("GET","POST"))
def register():
   return render_template('register.html')

@app.route('/login')
def login():
   return render_template('login.html')



if __name__ == '__main__':
   app.run()