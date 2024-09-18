# Crackz 
<img src="https://i.ibb.co/WHN3xHn/crzckz.jpg" alt="Project Logo" width="150px" height="150px">

**_A tool to recover you'r encrypted ZIP files using brute-force and dictionary attack's._**

# Caution :warning:
* When using a wordlist, it should not exceed __600 passwords__ due to Python limitations. This will be fixed in future updates.

## Features
* Brute-Force Attack: Tries all possible password combinations.
* Configurable Password Length: Supports setting the maximum length of passwords to test.

## Upcoming Features
* Configurable Password Length: Supports setting the maximum length of passwords to test.
* Progress Reporting: Provides feedback on the current progress of the attack.

## Prerequisites
* Python 3.x: Ensure you have Python 3.x installed. [Download here](https://www.python.org/downloads).

## Installation <br>
1. Clone repsitory: <br>
   ``` https://github.com/smog-root/crackz ```
2. Navigate to the project directory: <br>
  ``` cd path\crackz ```

## Usage
### Help:<br>
crackz.py [-h]

``` python3 crackz.py -h ```

## Crack password! :trollface:
``` python3 crackz.py -f path/file.zip -w path/wordlist.txt ```

## Execution
  __-h , --help           show this help message and exit__<br>
  __-f , --file      Enter zip file path.__<br>
  __-w , --wordlist  Enter password word list path.__<br>
  __-o , --output   Enter output directory for extracted files.__<br>
  __-ex , --extract        Extract files if password is found.__<br>

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
