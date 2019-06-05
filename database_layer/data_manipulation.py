from sys import path
path.append('../')
from utils.hospitaldb import *

class Database():

    @staticmethod
    def add_user(username,password,full_name,status):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO USERS(username,password,full_name,status)
            VALUES(?,?,?,?);
            """,(username, password, full_name, status)
                )
        connection.commit()
        connection.close()

    @staticmethod
    def find_user(username,password):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM USERS
            WHERE username = ? AND password = ?;
            """,(username, password)
            )
        user = cursor.fetchone()
        connection.commit()
        connection.close()
        return user

    @staticmethod
    def last_reg_patient():
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT MAX(id)
            FROM USERS
            WHERE status = 'patient';
            """
            )
        user = cursor.fetchone()
        connection.commit()
        connection.close()
        return user

    @staticmethod
    def last_reg_doctor():
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT MAX(id)
            FROM USERS
            WHERE status = 'doctor';
            """
            )
        user = cursor.fetchone()
        connection.commit()
        connection.close()
        return user

    @staticmethod
    def add_doctor(user_id,specialty,phone):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO DOCTORS(user_id,specialty,phone_number)
            VALUES(?,?,?);
            """,(user_id, specialty, phone)
                )
        cursor.execute("SELECT last_insert_rowid();")
        last_id = cursor.fetchone()
        connection.commit()
        connection.close()

        return last_id

    @staticmethod
    def list_doctor_slots(doctor_id):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, date, start_hour, end_hour, reservation_status
            FROM SLOTS
            WHERE doctor_id = {0}; 
            """.format(doctor_id)
            )
        slots = cursor.fetchall()
        connection.commit()
        connection.close()
        return slots

    @staticmethod
    def add_available_slot(doctor_id, id, date, start_hour, end_hour, reservation_status):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO SLOTS(doctor_id, id, date, start_hour, end_hour, reservation_status)
            VALUES(?,?,?,?,?,?);
            """,(doctor_id, id, date, start_hour, end_hour, reservation_status)
            )

        connection.commit()
        connection.close()

    @staticmethod
    def delete_slot(slot_id):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM SLOTS
            WHERE id = {0};
            """.format(slot_id)
            )

        connection.commit()
        connection.close()

    @staticmethod
    def find_doctor(user_id):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM DOCTORS
            WHERE user_id = {}; 
            """.format(user_id)
            )
        doctor = cursor.fetchone()
        connection.commit()
        connection.close()
        return doctor

    @staticmethod
    def find_patient(user_id):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""full_name
            SELECT *
            FROM PATIENTS
            WHERE user_id = {}; 
            """.format(user_id)
            )
        patient = cursor.fetchone()
        connection.commit()
        connection.close()
        return patient

    @staticmethod
    def add_patient(user_id, age, gender, phone):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO PATIENTS(user_id, age, gender, phone_number)
            VALUES(?,?,?,?);
            """,(user_id, age, gender, phone)
                )
        cursor.execute("SELECT last_insert_rowid();")
        last_id = cursor.fetchone()
        connection.commit()
        connection.close()
        return last_id

    @staticmethod
    def list_available_slots():
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, date, start_hour, end_hour, reservation_status
            FROM SLOTS
            """
            )
        slots = cursor.fetchall()
        connection.commit()
        connection.close()
        return slots

    @staticmethod
    def add_reservation(patient_id,slot_id):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO RESERVATIONS(patient_id, slot_id, status)
            VALUES(?,?,'reserved');
            """,(patient_id,slot_id)
            )
        cursor.execute("""
            UPDATE SLOTS
            SET reservation_status = 'reserved'
            WHERE id = {};
            """.format(slot_id))
        connection.commit()
        connection.close()

    @staticmethod
    def cancel_reservation(slot_id):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
           UPDATE RESERVATIONS
            SET status = 'cancelled'
            WHERE slot_id = {};
            """.format(slot_id)
            )
        cursor.execute("""
            UPDATE SLOTS
            SET reservation_status = 'free'
            WHERE id = {};
            """.format(slot_id))
        connection.commit()
        connection.close()

    @staticmethod
    def list_reservations(patient_id):
        connection = sqlite3.connect('hospital.db')
        cursor = connection.cursor()
        cursor.execute("""
           SELECT *
           FROM RESERVATIONS
           WHERE patient_id ={};
            """.format(patient_id)
            )
        all_reservations = cursor.fetchall()
        connection.commit()
        connection.close()
        return all_reservations
