from app import app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

# migrate extension
migrate = Migrate(app, db)

# manager extension
manager = Manager(app)
manager.add_command('dm', MigrateCommand)

if __name__ == '__main__':
    manager.run()
