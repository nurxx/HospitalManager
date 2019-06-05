from sys import path
path.append('../')
from database_layer.data_manipulation import Database
from utils.errors import *

class User:
    def __init__(self,id,username,password,full_name,status):
        self.id = id
        self.username = username
        self.password = password
        self.full_name = full_name
        self._status = status

    @classmethod
    def create_new_user(cls, username, password, full_name, status):
        try:
            current_user = Database.add_user(username,password,full_name,status)
        except DatabaseConnectionError:
            print('Something went wrong with the server! Please, try again.')


    @classmethod
    def find(cls, username, password):
        attr = Database.find_user(username, password)
        if attr:
            return cls(attr[0],attr[1],attr[2],attr[3],attr[4])

    @classmethod
    def _get_last_registered_status_doctor(cls):
        return Database.last_reg_doctor()[0] # return last registered doctors user_id 

    @classmethod
    def _get_last_registered_status_patient(cls):
        return Database.last_reg_patient()[0]

    @property
    def status(self):
        return self._status

    def is_doctor(self):
        return self.status == 'doctor'







