"""
    [summary]
    """
from peewee import TextField, DateTimeField, IntegerField

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
    email = TextField(unique=True)
    password = TextField()
    passwordResetToken = TextField(null=True)
    passwordResetExpires = DateTimeField(null=True)
    createdAt = DateTimeField()

    def to_dict(self):
        """
        [summary]

        Returns
        -------
        [type]
            [description]
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "createdAt": self.createdAt
        }
