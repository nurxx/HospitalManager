import sqlite3

def create_table_users():
    connection=sqlite3.connect('hospital.db')
    cursor=connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS USERS(
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(30) NOT NULL UNIQUE,
            password VARCHAR(50) NOT NULL,
            full_name VARCHAR(100) NOT NULL,
            status VARCHAR(10) NOT NULL
            );"""
            )

    connection.commit()
    connection.close()

def create_table_doctors():
    connection=sqlite3.connect('hospital.db')
    cursor=connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS DOCTORS(
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            specialty VARCHAR(30) NOT NULL,
            phone_number VARCHAR(15) NOT NULL,
            FOREIGN KEY(user_id) REFERENCES USERS(id)
            );"""
            )

    connection.commit()
    connection.close()

def create_table_patients():
    connection=sqlite3.connect('hospital.db')
    cursor=connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS PATIENTS(
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            age VARCHAR(30) NOT NULL,
            gender CHAR(1) NOT NULL,
            phone_number VARCHAR(15) NOT NULL,
            FOREIGN KEY(user_id) REFERENCES USERS(id)
            );"""
            )

    connection.commit()
    connection.close()

def create_table_slots():
    connection=sqlite3.connect('hospital.db')
    cursor=connection.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS SLOTS(
            doctor_id INTEGER NOT NULL,
            id CHAR(4) PRIMARY KEY NOT NULL,
            date CHAR(10) NOT NULL,
            start_hour VARCHAR(6) NOT NULL,
            end_hour VARCHAR(6) NOT NULL,
            reservation_status BOOLEAN,
            FOREIGN KEY(doctor_id) REFERENCES DOCTORS(id)
            );"""
            )

    connection.commit()
    connection.close()


def create_table_reservations():
    connection=sqlite3.connect('hospital.db')
    cursor=connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS RESERVATIONS(
            patient_id INTEGER NOT NULL,
            slot_id CHAR(4) NOT NULL,
            status VARCHAR(10) NOT NULL,
            FOREIGN KEY(slot_id) REFERENCES SLOTS(id),
            FOREIGN KEY(patient_id) REFERENCES PATIENTS(id)
            );"""
            )

    connection.commit()
    connection.close()



if __name__ == '__main__':
    create_table_doctors()
    create_table_users()
    create_table_patients()
    create_table_reservations()
    create_table_slots()
