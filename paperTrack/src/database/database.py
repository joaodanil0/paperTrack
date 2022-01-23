"""
    [summary]
    """
from peewee import SqliteDatabase


class Database:
    """
    [summary]
    """

    def __new__(cls, name: str) -> SqliteDatabase:
        return SqliteDatabase(name)

    def get(self):
        """
        [summary]
        """
