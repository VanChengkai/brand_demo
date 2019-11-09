# -*- encoding=UTF-8 —*—
from application import app, db
from flask_script import Manager


manager = Manager(app)

@manager.command
def __init__db():
    db.drop_all()
    db.create_all(app=app)

if __name__ == "__main__":
    manager.run()