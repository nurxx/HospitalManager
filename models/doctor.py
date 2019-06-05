from sys import path
path.append('../')
from database_layer.data_manipulation import Database
from .user import User 

class Doctor:

    def __init__(self, id, user_id, specialty, phone):
        self.id = id 
        self.user_id = user_id
        self.specialty = specialty
        self.phone = phone 

    @classmethod
    def create_new_doctor(cls, user_id, specialty, phone):
        try:
            doctor = Database.add_doctor(user_id,specialty, phone)
        except DatabaseConnectionError:
            print('Oops, something went wrong with the server! Please, try again.')
            sys.exit(1)
        return cls.find_doctor(user_id)

    @classmethod
    def find_doctor(cls,user_id):
        attr = Database.find_doctor(user_id)
        if attr:
            return cls(attr[0],attr[1],attr[2],attr[3])

    def list_slots(self):
        doctor_slots = Database.list_doctor_slots(self.id)
        print('|  ID  |  Date  |  From  |  To  | Reservation Status |')
        print('|------|--------|--------|------|--------------------|')
        for slot in doctor_slots:
            print('| {:^8} | {:^8} | {:^8} | {:^8} | {:^8} |'.format(slot[0],slot[1],slot[2],slot[3],slot[4]))

    def add_slot(self,slot_id,date,start_hour,end_hour,reservation_status):
        Database.add_available_slot(self.id, slot_id, date,start_hour, end_hour, reservation_status)

    def remove_slot(self,slot_id):
        Database.delete_slot(slot_id)
