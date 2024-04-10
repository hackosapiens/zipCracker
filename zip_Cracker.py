import zipfile

def crack_zip(zip_path, password_list):
    with zipfile.ZipFile(zip_path) as z:
        for password in password_list:
            try:
                z.extractall(pwd=password.encode())
                print(f'Password found: {password}')
                return password
            except:
                continue
    print('Password not found.')
    return None

# Example usage:
zip_file_path = input("Enter the path to the zip file you want to crack: ")  # Ask user for zip file path
password_file_path = input("Enter the path to the password file: ")  # Ask user for password file path

# Read the password file and create a list of passwords
with open(password_file_path, 'r') as f:
    passwords = [line.strip() for line in f]

crack_zip(zip_file_path, passwords)
