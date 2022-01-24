"""
    [summary]
    """
import os
import jwt
import bcrypt
from datetime import datetime, timedelta
from cherrypy import expose, tools, request, response, _cperror
from src.app.models.user_model import UserModel

class AuthController():
    """
    [summary]
    """

    def generate_token(self, params):
        secret = os.getenv("SECRET")
        params["exp"] = self.set_expiration_time(30)
        return jwt.encode(params, secret, algorithm="HS256")
    
    def set_expiration_time(self, seconds):
        return datetime.utcnow() + timedelta(seconds=seconds)
    
    def current_datetime_to_str(self):
        return datetime.utcnow().astimezone().strftime("%Y-%m-%dT%H:%M:%S %z")
    
    def encrypt_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
         
    @expose
    @tools.json_in()
    @tools.json_out()
    @tools.allow(methods=['POST'])
    def register(self):

        try:
            email = request.json["email"]
            is_none = not UserModel.get_or_none(UserModel.email == email)

            if not is_none:
                response.status = 400
                return { "message": "User already exist."}

            request.json["createdAt"] = self.current_datetime_to_str()
            request.json["password"] = self.encrypt_password(request.json["password"])

            user = UserModel().create(**request.json)
            token = self.generate_token({"id":user.id})

            return {"user": user.to_dict(), "token": token}
        except Exception as ex:
            print(ex, type(ex).__name__, ex.args)
            response.status = 400
            return { "message": "Registration failed."}
    
    @expose
    @tools.json_in()
    @tools.json_out()
    @tools.allow(methods=['POST'])
    def authenticate(self):

        try:
            email = request.json["email"]
            password = request.json["password"].encode('utf-8')

            user = UserModel.get_or_none(UserModel.email == email)

            if not user:
                response.status = 400
                return { "message": "User not found"}
            
            if not bcrypt.checkpw(password, user.password.encode('utf-8')):
                response.status = 400
                return { "message": "Invalid passowrd"}
            
            token = self.generate_token({"id":user.id})

            return {"user": user.to_dict(), "token": token}
            
        except Exception as ex:
            print(ex, type(ex).__name__, ex.args)
            response.status = 400
            return { "message": "Authentication failed."}
        





        
    
