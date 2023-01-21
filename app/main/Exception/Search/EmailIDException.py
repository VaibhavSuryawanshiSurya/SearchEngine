import re
from app.main.Utils.Logger.logging import *


class InvalidEmailIDError(Exception):

    def __init__(self,user_name):
        self.user_name = user_name

    def __str__(self):
        return(f'"{self.user_name}" is Invalid Email ID \nTry Again!')


def validateUserName(user_name):
    regex = r'\b[\w._-]+@[\w.-]+\.[A-Z|a-z]{2,}\b'
    result = re.findall(regex,user_name)
    if user_name == result[0]:
        return
    raise InvalidEmailIDError(user_name)

if __name__ == '__main__':
    validateInput('Midel pages.docx')