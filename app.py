from flask import Flask

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.jsonrpc import JSONRPC
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)

# Configurations
app.config.from_object('config')
# app.config.from_object('local-config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)
bcrypt = Bcrypt(app)

from models import *


@jsonrpc.method('app.index() -> str')
def index():
    '''this is index description

    multi line...'''
    return "hello JSONRPC!"


from datetime import datetime, timedelta


@jsonrpc.method('time.now() -> str')
def now():
    return datetime.now().isoformat()


@jsonrpc.method('time.add_now(now=str, days=int) -> str')
def add_now(now, days):
    now = datetime.strptime(now, "%Y-%m-%dT%H:%M:%S.%f")
    return (now + timedelta(days=days)).isoformat()


def check_auth(u, p):
    print(u, p)
    return True


@jsonrpc.method('time.auth(s=str) -> str', authenticated=check_auth)
def auth(s):
    return 'auth: ' + s


@jsonrpc.method('time.list(days=int) -> str')
def list(days):
    result = []
    for d in range(days):
        result.append(d)
    return result


@jsonrpc.method('app.all_all(list) -> int')
def list(nums):
    result = 0
    for d in nums:
        result += d
    return result


@jsonrpc.method('app.add(a=int, b=int) -> int')
def add(a, b):
    return a + b


from flask_jsonrpc.exceptions import OtherError


class MyError(OtherError):
    code = 30001
    message = "hello this is my error"


@jsonrpc.method('app.error(str)')
def error(s):
    x = MyError('some error happened! {}'.format(s))
    x.data = {'a': 3, 'b': 3.14}
    raise x


from contextlib import contextmanager


@contextmanager
def open_session(sid):
    yield dict(a=1, b=3.14)


@app.before_request
def before_request():
    print('BEFORE REQUEST!')


@app.after_request
def after_request(request):
    print('AFTER REQUEST!', request, type(request))
    return request


@jsonrpc.method('app.after_auth(sid=str, s=str) -> str')
def after_auth(sid, s):
    with open_session(sid) as session:
        return session


@app.route("/")
def hello():
    # user = User('zhangsan', 'zshan@email.com', '123456')
    # db.session.add(user)
    # db.session.commit()

    if app.config['DEBUG']:
        s = '<hr/>'
        for k in app.config:
            s += '<b>{0}</b>: {1}<hr/>'.format(k, app.config[k])
        return s
    else:
        return "hello world!"


if __name__ == "__main__":
    # pwhashes = []
    # for i in range(10):
    #     pwhashes.append(bcrypt.generate_password_hash('hello'))
    #
    # for pwh in pwhashes:
    #     print(pwh, end='==>')
    #     if not bcrypt.check_password_hash(pwh, 'hello'):
    #         print('ERROR')
    #     else:
    #         print('VERIFIED!')
    app.run()
