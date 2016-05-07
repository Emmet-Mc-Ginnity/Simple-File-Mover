"""
A simple module to transfer files from one directory to another
"""

import os
import shutil


def get_all_files(directory):
    """
    Returns all of the files in a given directory, including nested ones

    :param directory: String - directory to retrieve the files from
    :return: List - containing each file in the directory including path
    """

    dir_list = os.listdir(directory)
    all_files = []
    for file in dir_list:
        if os.path.isdir(directory + "/" + file):
            all_files = all_files + get_all_files(directory + "/" + file)
        else:
            all_files.append(directory + "\\" + file)
    return all_files


def move_successful(num_files, target_folder):
    """
    Checks if the files were moved/copied successfully

    :param num_files: Int - number of files in the directory
    :param target_folder: String - argument for the destination folder
    :return: String - transfer status as string
    """
    count = 0

    destination_files = os.listdir(target_folder)
    for file in destination_files:
        if os.path.isfile(target_folder + '\\' + file):
            count += 1

    if count == num_files:
        return "All files were successfully moved"

    elif count == 0:
        return "No files were successfully moved"

    return "Some files were moved successfully"


def move_files(files, target_folder, extension=None):
    """
    Moves all files to the directory with a given extension

    :param files: List - files to be transferred
    :param extension: String - specified file extension
    :param target_folder: String - argument for the destination folder
    :return: none
    """

    if extension is None:
        extension = ""

    for file in files:
        if file.endswith("." + extension):
            try:
                shutil.copy(file, target_folder)
            except PermissionError:
                print("Error copying file "+file + "\n")
            except shutil.Error:
                ""
    print(move_successful(len(files), target_folder))


def copy_files(files, target_folder,  extension=None):
    """
    Copies all files to the directory with a given extension

    :param files: List - files to be transferred
    :param extension: String - specified file extension
    :param target_folder: String - argument for the destination folder
    :return: none
    """

    if extension is None:
        extension = ""

    for file in files:
        if file.endswith(extension):
            try:
                shutil.copy(file, target_folder)
            except PermissionError:
                print("Error moving file "+file + "\n")
            except shutil.Error:
                ""
    print(move_successful(len(files), target_folder))


def start():
    """
    The controller function that controls the flow of the program

    :return: none
    """

    directory = input("Please enter a directory\n:>")

    while True:
        option = input("Do you want to copy(c) or move(m) the files?\n:>")
        if option != "c" and option != "m":
            print("Please select a valid option.\n")
        else:
            break

    target_directory = input("Where would you like to put these files?\n:>")

    files = get_all_files(directory)
    if len(files) == 0:
        return "No files to be moved"

    extension = input("Should I look for a specific extension? \n"
                      " Please enter 'n' if not, else enter your extension with '.' \n:>")

    if extension == "n":
        extension = None

    if option == "m":
        move_files(files, target_directory, extension)
    elif option == "c":
        copy_files(files, target_directory, extension)

    return


if __name__ == "__main__":
    start()
