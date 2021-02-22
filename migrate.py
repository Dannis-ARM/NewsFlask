from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from App import create_app,db,models

# The migration need no db.create_all() or db.drop_all()
app = create_app("develop")
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command("db",MigrateCommand)

if __name__ == "__main__":
    manager.run()


