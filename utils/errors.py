class Error(Exception):
    pass

class InvalidPasswordError(Error):
    pass

class PasswordsDontMatchError(Error):
    pass

class UserAlreadyExistsError(Error):
    pass

class DatabaseConnectionError(Error):
    pass