import pyAesCrypt
import os

# function that dencrypt files
def dencryption(file, password):

    buffer_size = 512 * 1024

    # call dencrypt function from pyAesCrypt
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    # print the result that the file is encrypted successfully
    print(f"File: {str(os.path.splitext(file)[0])} - DECRYPTED ")

    # delete the origin files
    os.remove(file)

# scan directories
def walking_by_dirs(dir, password):
    # select al dir in this dir
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        # if we faint the file - dencrypt it
        if os.path.isfile(path):
            try:
                dencryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)


config_dir = input("Insert the directory location: ")
# check if the directory exists
if os.path.exists(config_dir):
    print(f"{config_dir}\nConfig directory has found!")
    password = input("Insert the password for dencrypt: ")
    walking_by_dirs(fr'{config_dir}', password)
else:
    print(f"{config_dir}\nConfig directory has not found!")


