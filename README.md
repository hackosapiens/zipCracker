# zipCracker
simple Password cracker for encrypted zip files

* Function: crack_zip(zip_path, password_list)

This function attempts to crack a zip file given a list of potential passwords.

*Parameters:

    zip_path (str): The path to the zip file that needs to be cracked.
    password_list (list): A list of potential passwords to try.

*Behaviour: The function opens the zip file and iterates over each password in the password list. For each password, it attempts to extract all files from the zip file. If the extraction is successful, it means the password is correct. The function then prints the password and returns it. If the extraction fails (which raises an exception), it means the password is incorrect, and the function continues with the next password. If no password is found after trying all passwords in the list, the function prints a message and returns None

*Example:
zip_file_path = input("Enter the path to the zip file you want to crack: ")
password_file_path = input("Enter the path to the password file: ")

with open(password_file_path, 'r') as f:
    passwords = [line.strip() for line in f]

crack_zip(zip_file_path, passwords)
