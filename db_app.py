from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
db = SQLAlchemy(app)


class CRUDMixin(object):
    def delete(self):
        db.session.delete(self)

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r: %r %r>' % (self.id, self.username, self.email)


db.create_all()

admin = User('admin', 'admin@example.com')
db.session.add(admin)
guest = User('guest', 'guest@example.com')
db.session.add(guest)
for i in range(100):
    username = 'user{}'.format(i)
    user = User(username, '{}@example.com'.format(username))
    db.session.add(user)
db.session.commit()

users = User.query.all()
print(users)

admin = User.query.filter_by(username='admin').add_columns('email').first()
print(admin)
for f in admin.keys(): print(f, admin[0].username, admin[0].id, admin[0].email)

# print(User.query, type(User.query))
# for p in User.query.filter(User.username.like('user%')).paginate(page=1, per_page=10, error_out=True).items:
#     print(p)

users = User.query.all()
print(users)

print('-' * 60)

User.query.filter(User.username.like('user%')).delete(synchronize_session=False)

users = User.query.all()
print(users)

User.query.filter(User.username.like('ad%')).update(
    {User.email: 'adminx@eee.com', User.username: 'aaa'}, synchronize_session='fetch'
)

users = User.query.first()
print(users)
users.username = 'asfasfas'
# db.session.add(users)
# db.session.commit()
users.save()

users.delete()

users = User.query.all()
print(users)
