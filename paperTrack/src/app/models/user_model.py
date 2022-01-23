"""
    [summary]
    """
from peewee import TextField, DateTimeField

from src.app.models.base_model import BaseModel


class UserModel(BaseModel):
    """
    [summary]

    Parameters
    ----------
    BaseModel : [type]
        [description]
    """

    name = TextField()
    mail = TextField(unique=True)
    password = TextField()
    passwordResetToken = TextField(null=True)
    passwordResetExpires = DateTimeField(null=True)
    createdAt = DateTimeField()
