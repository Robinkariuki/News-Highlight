frrom app import create_app
from flask_script import Manager, Server
 #creating app instance
 app = create_app('development')

 Manager = Manager(app)

 Manager.add_commnad('server', Server)

 if __name__ == '__main__' :
     manager.run()