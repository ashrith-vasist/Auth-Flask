from flask import Flask, render_template,session,request,redirect,url_for
from flask_bootstrap import Bootstrap5




class User:
   def __init__(self, id, username, password):
      self.id = id
      self.username = username
      self.password = password
   def __repr__(self):
      return f'<User: {self.username}>'

users=[]
users.append(User(id=1,username='Ash@gmail.com',password='ash@2003'))
users.append(User(id=2,username='San@gmail.com',password='San@2002'))



app = Flask(__name__)
app.secret_key='secrectkeyashonlyknows'
bootstrap = Bootstrap5(app)



@app.route('/')
def Home():
   return render_template('Home.html')

@app.route('/register',methods=("GET","POST"))
def register():
   return render_template('register.html')

@app.route('/login',methods=('GET','POST') )
def login():
   if request.method == 'POST':
      session.pop('user_id',None)
      username = request.form['username']
      password = request.form['password']
      user = [x for x in users if x.username == username][0]
      if user and user.password == password and user.username == username:
         session['user_id']=user.id
         return redirect(url_for('Profile'))
      return redirect(url_for('login'))
   return render_template('login.html')

@app.route('/Profile')
def Profile():
   return render_template('Profile.html')

if __name__ == '__main__':
   app.run()