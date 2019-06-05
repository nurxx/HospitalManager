import hashlib, os
from sys import path
path.append('../')
from models.user import User
from models.doctor import Doctor
from models.patient import Patient
from utils.errors import *

class Controller:

    @staticmethod 
    def _hash(password):
        password_salt = '1Ha7'
        hashed = hashlib.md5()
        hashed.update(('%s%s' % (password_salt, password)).encode('utf-8'))
        hashed = hashed.hexdigest()
        return hashed

    @staticmethod
    def _validate_password(password):
        if len(password) > 50 or password.isdigit():
            print('Not a valid password!')
            raise InvalidPasswordError
    
    @staticmethod
    def _do_passwords_match(pass1,pass2):
        if not pass1 == pass2:
            raise PasswordsDontMatchError

    @classmethod
    def login(cls,username,password):
        cls._validate_password(password)
        hashed_password = cls._hash(password)
        current_user = User.find(username,hashed_password)
        return current_user

    @classmethod
    def register(cls,username,password,confirm_password,full_name,status):
        cls._validate_password(password)
        cls._validate_password(confirm_password)

        hashed_pass1 = cls._hash(password)
        hashed_pass2 = cls._hash(confirm_password)
        cls._do_passwords_match(hashed_pass1,hashed_pass2)

        if User.find(username,hashed_pass1):
            raise UserAlreadyExistsError

        return User.create_new_user(username,hashed_pass1,full_name,status)

    @classmethod
    def register_doctor(cls,specialty,phone):
        user_id = User._get_last_registered_status_doctor()
        return Doctor.create_new_doctor(user_id,specialty,phone)

    @classmethod
    def register_patient(cls,age,gender,phone):
        user_id = User._get_last_registered_status_patient()
        return Patient.create_new_patient(user_id,age,gender,phone)

    @classmethod 
    def get_doctor(cls,user_id):
        return Doctor.find_doctor(user_id)

    @classmethod
    def get_patient(cls,user_id):
        return Patient.find_patient(user_id)

    @classmethod
    def list_slots(cls,doctor):
        doctor.list_slots()

    @classmethod
    def add_slot(cls,doctor,slot_id,date,start_hour,end_hour,reservation_status):
        doctor.add_slot(slot_id,date,start_hour,end_hour,reservation_status)

    @classmethod
    def remove_slot(cls,doctor,slot_id):
        doctor.remove_slot(slot_id)

    @classmethod
    def view_available_slots(cls,patient):
        patient.view_available_slots()

    @classmethod
    def reserve_slot(cls,patient,slot_id):
        patient.reserve_slot(slot_id)

    @classmethod
    def cancel_reservation(cls,patient,slot_id):
        patient.cancel_reservation(slot_id)

    @classmethod
    def show_reservations(cls,patient):
        patient.show_reservations()


