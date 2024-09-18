import zipfile
import argparse
import os
import platform

def clear_terminal():
    """Clears the terminal screen based on the operating system."""

    if platform.system() == 'Windows':
        os.system('cls')

    else:
        os.system('clear')

clear_terminal()

print("""                                             
  ####    #####     ####     ####    ## ##    ######  
 ##  ##   ##  ##   ##  ##   ##  ##   ####        ##   
 ##       #####    ######   ##       ###        ##    
 ##  ##   ## ##    ##  ##   ##  ##   ####      ##     
  ####    ##  ##   ##  ##    ####    ## ##    ######
      
            https://github.com/smog-root

""")

def crack_password(password_list, zip_file_obj, output_path, should_extract):
    """Attempts to crack the zip file password using the given wordlist."""

    for idx, word in enumerate(password_list, start=1):
        try:
            if should_extract:
                zip_file_obj.extractall(path=output_path, pwd=word.encode())
                print(f"[+]Password found at line: {idx}, Password: {word}")
                print(f"[+]Files extracted successfully to: {os.path.abspath(output_path)}")
                return True
            else:
                zip_file_obj.extractall(pwd=word.encode())
                print(f"[+]Password found at line: {idx}")
                print(f"[+]Password: {word}")

                return True
        except (RuntimeError, zipfile.BadZipFile):
            continue
    return False

# Initialize argument parser
parser = argparse.ArgumentParser(description="Zip file password bruteforce attack!")
parser.add_argument('-f', '--file', required=True, help="Enter zip file path.")
parser.add_argument('-w', '--wordlist', required=True, help="Enter password word list path.")
parser.add_argument('-o', '--output', help="Enter output directory for extracted files.")
parser.add_argument('-ex', '--extract', action='store_true', help="Extract files if password is found.")
args = parser.parse_args()


password_list_path = args.wordlist
zip_file_path = args.file
output_path = args.output
should_extract = args.extract

# Validation checks
if should_extract and not output_path:
    print("[-]Error: The -ex option requires an output directory to be specified with -o.")
    exit(1)

if output_path and not should_extract:
    print("[-]Error: To extract the files, you need to define the -ex option.")
    exit(1)

if should_extract and output_path:
    os.makedirs(output_path, exist_ok=True)

try:
    with zipfile.ZipFile(zip_file_path) as obj:
        with open(password_list_path, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
            password_list = file.read().splitlines()
        if not crack_password(password_list, obj, output_path, should_extract):
            print("[*]Password not found in this file!")
except FileNotFoundError:
    print(f"[-]Error: The file '{password_list_path}' does not exist.")
except zipfile.BadZipFile:
    print(f"[-]Error: '{zip_file_path}' is not a valid zip file.")
except Exception as e:
    print(f"[-]An unexpected error occurred: {e}")
