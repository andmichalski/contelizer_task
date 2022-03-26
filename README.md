# Project Title

Contelizer task

## Author

Andrzej Michalski

## Description

The repository contains two main programs: "shuffle_words.py" and "validate_pesel.py". Also contains tests and example text.

### Dependencies
To run this programs You only need to Python3. Scripts are using only Python Standard Libraries. Because of simplicity this scripts no conterization is docker or virtualenv is provided. Tests are using Python builtin unittest framework

### Execution

Execution could be provided on command line in Linux or MacOSFirst user need to go to main directory of repository.

* shuffle_words.py


Script creates a copy of file. in convention copy_old_filename


To run shuffle_words program
```
python3 shuffle_words.py example_text.txt
```



Execution of tests:
```
python3 test_shuffle_words.py
```


* validate_pesel.py
To run validate_pesel program
```
python3 validate_pesel.py 48030546299
```


Execution of tests:
```
python3 test_validate_pesel.py
```

