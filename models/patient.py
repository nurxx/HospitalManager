from sys import path
path.append('../')
from .user import User 
from database_layer.data_manipulation import Database
from utils.errors import *

class Patient:

    def __init__(self,id,user_id,age,gender,phone):
        self.id = id
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.phone = phone 

    @classmethod 
    def create_new_patient(cls,user_id,age,gender,phone):
        try:
            Database.add_patient(user_id,age,gender,phone)
        except DatabaseConnectionError:
            print('Something went wrong with the server! Please, try again.')
            sys.exit(1)
        return cls.find_patient(user_id)

    @classmethod
    def find_patient(cls,user_id):
        attr = Database.find_patient(user_id)
        if attr:
            return cls(attr[0],attr[1],attr[2],attr[3],attr[4])

    def view_available_slots(self):
        doctor_slots = Database.list_available_slots()
        print('|      ID      |    Date    |    From    |    To    | Reservation Status |')
        print('|--------------|------------|------------|----------|--------------------|')
        for slot in doctor_slots:
            print('| {:^10} | {:^10} | {:^6} | {:^6} | {:^14} |'.format(slot[0],slot[1],slot[2],slot[3],slot[4]))

    def reserve_slot(self,slot_id):
        Database.add_reservation(self.id,slot_id)

    def cancel_reservation(self,slot_id):
        Database.cancel_reservation(slot_id)

    def show_reservations(self):
        reservations = Database.list_reservations(self.id)
        print('|   ID    |       Slot       |  Status  |')
        print('|---------|------------------|----------|')
        for reservation in reservations:
            print('| {:^7} | {:^16} | {:^8} |'.format(reservation[0],reservation[1],reservation[2]))
