import sys
from getpass import getpass
from sys import path
path.append('../')
from controller.controller import Controller 
from utils.errors import *
from .user_main_menu import MainMenu

class StartMenu:

    @classmethod
    def run(cls):
        print(" ####### Welcome to HackBulgaria Hospital Manager! ####### ")
        options = '''
        What would you like to do?
        1) Login
        2) Register
        3) Exit
        '''
        print(options)

        choice = input()
        if choice == '1':
            username = input('Enter username:> ')
            password = getpass('Enter password:> ')
            current_user = Controller.login(username,password)

            if current_user:

                if current_user.is_doctor():
                    user_id = current_user.id
                    current_user = Controller.get_doctor(user_id)
                    MainMenu.show_doctor_options(current_user)

                else:
                    user_id = current_user.id
                    current_user = Controller.get_patient(user_id)
                    MainMenu.show_patient_options(current_user)
            else:
                print('Wrong username or password!')
                sys.exit(1)

        elif choice == '2':
            print(' ######## Creating your profile ########')
            username = input('Enter username:> ')
            password = getpass('Enter password:> ')
            confirm_password =  getpass('Repeat password:> ')
            full_name = input('Full name:> ')
            status = input('Status [patient/doctor]:> ')

            try:
                current_user = Controller.register(
                    username, password, confirm_password,full_name,status)
            except UserAlreadyExistsError:
                print('Sign up failed! User already exists!')
                sys.exit(1)
            except DatabaseConnectionError:
                print('Oops! Something went wrong with the server. Please, try again.')
                sys.exit(1)
            except PasswordsDontMatchError:
                print('Sign up failed! Passwords don\'t match! Please, try again.')
                sys.exit(1)
            else:

                if status == 'doctor':
                    specialty = input('Specialty:> ')
                    phone = input('Phone:> ')
                    doctor = Controller.register_doctor(specialty,phone)
                    MainMenu.show_doctor_options(doctor)
                    
                elif status == 'patient':
                    age = int(input('Age:> '))
                    gender = input('Gender:> ')
                    phone = input('Phone:> ')
                    patient = Controller.register_patient(age,gender,phone)
                    MainMenu.show_patient_options(patient)
        else:
            print('Quitting App')
