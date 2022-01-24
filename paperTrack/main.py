"""
    [summary]
"""

import cherrypy

from src.app.models.user_model import UserModel
from src.app.controllers.auth_controller import AuthController

user = UserModel()
user.create_table()

cherrypy.tree.mount(AuthController(), "/auth", "server.conf")
cherrypy.quickstart(config="server.conf")
