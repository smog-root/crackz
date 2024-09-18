# Crackz 
A tool to recover you'r encrypted ZIP files using brute-force and dictionary attack's.

# Caution
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
crackz.py [-h] -f FILE -w WORDLIST

``` python3 crackz.py -f path/zipfile.zip -w path/wordlist.txt ```

