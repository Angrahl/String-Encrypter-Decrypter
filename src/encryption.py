import sys
from cryptography.fernet import Fernet


def write_key():
    """Creates the key file for string encryption
    """
    key = Fernet.generate_key()
    with open('encryption_key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    """Reads the key file for string encryption
    """
    return open('encryption_key.key', 'rb').read()


def string_entry():
    """String entry from the user
    """
    msg = input('Enter a string to encrypt : ')
    x = len(msg)

    if x == 0:
        print('The string to encrypt cannot be empty!')
        sys.exit(1)

    return msg


def file_writer(smth_to_write):
    """Creates the specified file and
    writes the encrypted message in it
    """

    # No need to have a try/except for file creation/writing here since option 'w' is set
    file = open('encrypted_msg.txt', 'wt')
    file.write(smth_to_write)
    
    try:
        file.close()
    except:
        print('Error while closing the file!')
        sys.exit(1)


def main():
    """The main function to run the script
    """
    write_key()
    key = load_key()
    message = string_entry().encode()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(message)

    # I use decode() here to avoid having the 'b' token,
    # which means bytes, when displaying the results
    decode_encrypted = encrypted.decode()

    print('The following message will be written in \'encrypted_msg.txt\' : {}'.format(
        decode_encrypted))

    file_writer(decode_encrypted)


if __name__ == '__main__':
    main()
