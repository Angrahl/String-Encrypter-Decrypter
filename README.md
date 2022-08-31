# String Encrypter & Decrypter

This is a small string encrypter/decrypter done with Python and the Fernet module from the **cryptography** package.

The script **encryption.py** will encrypt a string entered by the user using a generated key. This key is generated with the use of cryptography's package Fernet module and will be written in a file named **encryption_key.key**. Then, when the user will enter his message to encrypt, this one will be encrypted, using the key, and written in a file named **encrypted_msg.txt**.

The script **decryption.py** simply opens the file which contains the encrypted message, reads it and decrypts it.

## 1. Installing Python and PIP

To run this script, you will need a valid installation of Python and PIP.

### On Windows

You can download the latest release of Python for Windows [here](https://www.python.org/downloads/)

Normally, PIP is automatically included in the Python installer for the latest versions.

Make sure to tick the box to add Python to your *PATH* environment variable.

Check your Python version by running:
```
> python --version
```
If it's equal or greater than Python 3.4, PIP is already installed on your system, check its version by running:
```
> pip --version
```

### On a Debian-based distribution
```
$ sudo apt install python3
$ sudo apt install python3-pip
```

### On Fedora
```
$ sudo dnf install python3
$ sudo dnf install python-pip
```

## 2. Installing 'cryptography' and run the scripts

Once you installed Python and PIP, you'll need to install the *cryptography* package with PIP to be able to run the scripts (at least for a Windows user)

Run this command to download the *cryptography* package:
```
$ pip install cryptography
```
Or, if the previous command doesn't work:
```
$ pip3 install cryptography
```

To run the scripts, just do (in this order, of course):
```
$ python3 encryption.py
$ python3 decryption.py
```

You can also use the **Makefile** to run the scripts and/or clean the directory.

Just run *make command_you_want_to_use*. Check the Makefile to see the available commands.
