import os
from interface.user_start_menu import StartMenu

class HospitalManager:
    @classmethod
    def start_app(cls):
        StartMenu.run()

if __name__ == '__main__':
    os.system('python3 utils/hospitaldb.py')
    HospitalManager.start_app()
