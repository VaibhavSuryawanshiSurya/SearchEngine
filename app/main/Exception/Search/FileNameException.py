from app.main.Utils.Logger.logging import *


class InvalidInputError(Exception):

    def __init__(self,filename):
        self.filename = filename

    def __str__(self):
        return(f'"{self.filename}" is Invalid File Name\nTry Again!')


def validateInput(filename):
    invalid_Char = (r'/','?',':','*','"','<','>','|')
    if filename == '' or any([True if i in invalid_Char else False for i in filename]):
        raise InvalidInputError(filename)

if __name__ == '__main__':
    validateInput('Midel pages.docx')