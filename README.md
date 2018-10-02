# Find matrix by Pattern
> Application to find the number of occurrences of a matrix of characters in another file. 


## Technologies utilized
* Python 2.x

## Usage

Any Operating System with Python 2.x:

## Option 1

```sh
python  main.py [-h] --bug BUG --land LAND

Example: python main.py --bug bug.txt --land landscape.txt

Where:

bug.txt -> Path to the file containing the pattern

landscape.txt -> Path to the file where the program needs to count the occurrences
```

## Option 2

> Inside a Python Console in the same directory of the files

```sh
from main import count_pattern

count_pattern('bug.txt', 'landscape.txt')

Where:

bug.txt -> Path to the file containing the pattern

landscape.txt -> Path to the file where the program needs to count the occurrences

## Release History

* 0.0.5
    * First release
* 0.0.4
    * Add argparse to receive the filenames by console argument
* 0.0.3
    * Fix bugs and refactor some code
* 0.0.2
    * count_pattern - Function to find and count the pattern occurrences
* 0.0.1
    * to_matrix - Function to extract the base pattern

## Meta

Diemesleno Souza Carvalho – [@diemesleno](https://twitter.com/diemesleno) – diemesleno@gmail.com

[https://github.com/diemesleno/bug_pattern](https://github.com/diemesleno/)
