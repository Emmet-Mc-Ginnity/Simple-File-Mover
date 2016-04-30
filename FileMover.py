import os
import shutil


def get_all_files(directory):
    """
    Returns all of the files in a given directory, including nested ones
    :param directory: string
    :return: list
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

    :param num_files: int
    :param target_folder: string
    :return: string
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


def move_files(files, target_folder):
    """
    Moves all files in the given directory, and removes them from folders
    :param files: list
    :param target_folder: string
    """

    for file in files:
        try:
            shutil.move(file, target_folder)
        except PermissionError:
            print("Error moving file "+file + "\n")

    print(move_successful(len(files), target_folder))


def copy_files(files, target_folder):
    """
    Copies all files to destination without deleting any
    :param files: list
    :param target_folder: string
    :return: nothing
    """

    for file in files:
        try:
            shutil.copy(file, target_folder)
        except PermissionError:
            print(file + "was not moved successfully")

    print(move_successful(len(files), target_folder))


def move_files_with_extension(files, extension, target_folder):
    """
    Moves all files to the directory with a given extension

    :param files: list
    :param extension: string
    :param target_folder: string
    :return: nothing
    """

    if len(files) == 0:
        return "No files to be moved"

    for file in files:
        if file.endswith("." + extension):
            try:
                shutil.copy(file, target_folder)
            except PermissionError:
                print("Error copying file "+file + "\n")
            except shutil.Error:
                ""
    print(move_successful(len(files), target_folder))


def copy_files_with_extension(files, extension, target_folder):
    """
    Moves all files to the directory with a given extension

    :param files: list
    :param extension: string
    :param target_folder: string
    :return: nothing
    """

    if len(files) == 0:
        return "No files to be moved"

    for file in files:
        if file.endswith("." + extension):
            try:
                shutil.move(file, target_folder)
            except PermissionError:
                print("Error moving file "+file + "\n")
            except shutil.Error:
                ""
    print(move_successful(len(files), target_folder))


def start():
    """
    The controller module that keeps track of everything
    :return: nothing
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

    extension = input("Should I look for a specific extension? Please enter 'n' if not, else enter your extension \n:>")

    if extension == "n":
        if option == "m":
            move_files(files, target_directory)
        elif option == "c":
            copy_files(files, target_directory)
        return
    else:
        if option == "m":
            move_files_with_extension(files, extension, target_directory)
        elif option == "c":
            copy_files_with_extension(files, extension, target_directory)


if __name__ == "__main__":
    start()

