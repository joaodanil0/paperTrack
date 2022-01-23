"""
    [summary]
    """
import os
from peewee import Model
from src.database.database import Database
from dotenv import load_dotenv, find_dotenv



class BaseModel(Model):
    """
    [summary]

    Parameters
    ----------
    Model : [type]
        [description]
    """
    class Meta:
        """
        [summary]
        """
        load_dotenv(find_dotenv())
        database = Database(str(os.getenv("DB_TEST")))
