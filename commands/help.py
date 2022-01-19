import os

def run():
    """help command"""

    current_folder = os.getcwd()
    commands_folder = current_folder + "\\commands"
    changing_folder = os.chdir(commands_folder)
    list_in_folder = os.listdir(changing_folder)
    file_number = 1
    for file in list_in_folder:
        if file.endswith(".py"):
            print(str(file_number) + ' ) ' + file + ' - ' + '')
        file_number += 1

run()