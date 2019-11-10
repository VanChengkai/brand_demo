# -*- encoding=UTF-8 —*—
from application import app, db
from flask_script import Manager
from application.models import User

manager = Manager(app)

@manager.command
def __init__db():
    db.drop_all()
    db.create_all()

    for i in range(100):
        db.session.add(User( str(i), 'a'+str(i) ))
    
    db.session.commit()

if __name__ == "__main__":
    manager.run()