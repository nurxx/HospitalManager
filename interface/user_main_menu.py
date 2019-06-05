from sys import path
path.append('../')
from controller.controller import Controller 

class MainMenu:
    
    @classmethod
    def show_doctor_options(cls,doctor):
        options = '''
        1) View my slots
        2) Add slot
        3) Delete slot
        4) Exit
        '''
        print(options)

        choice = ''
        while choice != '4':
            choice = input('Select option:> ')

            if choice == '1':
                print('##### Here are all your slots for the moment! #####')
                Controller.list_slots(doctor)

            elif choice == '2':
                print('##### Adding new slot #####')
                slot_id = input('Slot ID:> ')
                date = input('Date:> ')
                start_hour = input('Start time:> ')
                end_hour = input('End time:> ')
                reservation_status = input('Reservation status:> ')
                Controller.add_slot(doctor,slot_id,date,start_hour,end_hour,reservation_status)

            elif choice == '3':
                to_be_removed = input('Slot ID:> ')
                print('##### Removing a slot #####')
                Controller.remove_slot(doctor,to_be_removed)
                print('##### Slot with id : {} was succesfully removed! #####'.format(to_be_removed))

    @classmethod 
    def show_patient_options(cls,patient):
        options = '''
        1) View available slots
        2) Reserve slot
        3) Cancel reservation
        4) Show my reservations
        5) Exit
        '''
        print(options)

        choice = ''
        while choice != '5':
            choice = input('Select option:> ')
            if choice == '1':
                Controller.view_available_slots(patient)
            elif choice == '2':
                print('##### Reserving a slot ... Please, select ID ... #####')
                slot_id = input('Slot ID:> ')
                Controller.reserve_slot(patient, slot_id)
            elif choice == '3':
                slot_id = input('Cancel by slot id:> ')
                Controller.cancel_reservation(patient, slot_id)
            elif choice == '4':
                Controller.show_reservations(patient)
