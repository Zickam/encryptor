class PasswordIsNotSet(Exception):
    def __init__(self, message="Password hasn't been set up before using it!"):
        super().__init__(message)
        