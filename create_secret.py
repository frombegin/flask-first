import os

print('CSRF_SESSION_KEY = {}'.format(os.urandom(24)))
print('SECRET_KEY = {}'.format(os.urandom(24)))
