# HashBreaker

HashBreaker is a script designed to crack hash values using a wordlist. 
The script supports various hash types and prints the results to the terminal.

## Requirements

To run the password cracker script, ensure your environment meets the following requirements:

### Python Version

- Python 3.6 or higher (Tested on Python 3.11)

### Required Modules

- `os`: Standard Python library for interacting with the operating system.
- `argparse`: Standard Python library for parsing command-line arguments.
- `hashlib`: Standard Python library for hashing functions.
- `time`: Standard Python library for measuring time.

## Usage

```sh
python3 password_cracker.py "hashValue" -w path/to/passwords/list.txt
```

## Example Output
```sh
Possible types of this hash are : 
     + : sha256

[*] Crack operation start ...
    + : sha256
	  Password found :	biker50 

[*] Crack operation completed in 0.03 seconds
```
## Author
  **CHAHAT Abdennour**
