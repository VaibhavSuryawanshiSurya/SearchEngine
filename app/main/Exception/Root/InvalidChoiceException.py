try:
    import os
    from app.main.Controller.Root.ActiveRootFinder import *
    from app.main.Utils.Logger.logging import *
except Exception as e:
    print(e,'\n')


class InvalidDriveError(Exception):

    def __init__(self,drive_choose):
        self.drive_choose = drive_choose

    def __str__(self):
        return(f'{self.drive_choose} Drive is not present in system\nTry Again!')


def validateDrive(drive_choose, drive_count):
    if drive_choose not in range(1, drive_count+2):
        raise InvalidDriveError(drive_choose)
    

if __name__ == '__main__':
    validateDrive('E:')