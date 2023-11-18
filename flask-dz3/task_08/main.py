from flask import Flask,render_template, request
from  task_08.model import db, User
from task_08.forms import RegisterForm
from flask_wtf.csrf import CSRFProtect


app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mybase.db'
db.init_app(app)




@app.route('/')
def index():
    return 'hello'

@app.cli.command("init_db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name=form.name.data
        # lastname=form.
        email=form.email.data
        password=form.password.data
        user = User(name=name, email=email, password=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return 'okey'
    else:
        return render_template('registration.html', form=form)



if __name__=='__main__':
    pass
