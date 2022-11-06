
# import module
import os
from datetime import datetime


class common_func:

    def create_folder(self):
        datestring = str(int(datetime.now().strftime("%Y%m%d")))
        current_path = os.path.dirname(__file__)
        create_folder = os.path.join(current_path, datestring)

        # Check whether the specified path exists or not
        isExist = os.path.exists(create_folder)
        if not isExist:
            # Create a new directory because it does not exist
            dir_ = os.makedirs(create_folder)
            return create_folder

    def create_file(self):
        dir_ = self.create_folder()
        print(dir_)
        # get current date and time
        current_datetime = str(int(datetime.now().strftime("%Y%m%d%H%M%S")))
        # print("Current date & time : ", current_datetime)

        # convert datetime obj to string
        str_current_datetime = str(current_datetime)

        # create a file object along with extension
        file_name = str_current_datetime+".json"
        print(os.path.join(dir_, file_name))
        file = open(os.path.join(dir_, file_name), 'w')
        return file

