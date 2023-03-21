import abc
from pydantic import BaseModel
from datetime import datetime

DB_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

class OdmModel(BaseModel, metaclass=abc.ABCMeta):

    @staticmethod
    def to_timestamp(dt:datetime, quote=False):
        timestamp = dt.strftime(DB_DATETIME_FORMAT)
        return f"'{timestamp}'" if quote else timestamp
    
    @staticmethod
    def from_timestamp(timestamp:str):
        return datetime.strptime(timestamp, DB_DATETIME_FORMAT)

    @abc.abstractclassmethod
    def get_create_table_statement(cls):
        pass

    @abc.abstractclassmethod
    def get_drop_table_statement(cls):
        pass

    @abc.abstractclassmethod
    def get_insert_statement(cls, **kwargs):
        pass

    @abc.abstractclassmethod
    def get_select_statement(cls, **kwargs):
        pass

    @abc.abstractclassmethod
    def get_update_statement(cls, **kwargs):
        pass
