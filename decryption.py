import sys
from cryptography.fernet import Fernet
from encryption import load_key


def open_crypted_file():
    """Open the file which contains the encrypted message
    and return the content as a string
    """
    try:
        file = open('encrypted_msg.txt', 'r')
    except:
        print('\'encrypted_msg.txt\' doesn\'t exist in this directory!')
        sys.exit(1)

    with file as f:
        content = f.readlines()

    return str(content)


def main():
    """The main function to run the script
    """
    msg = open_crypted_file().encode()

    """I'm kinda lazy so imported the load_key() function
    from 'encryption.py' as you can see in the imports
    at the beginning of the file
    """
    key = load_key()

    fernet = Fernet(key)

    decrypted = fernet.decrypt(msg)

    decode_decrypted = decrypted.decode()

    print('The original message was : {}'.format(decode_decrypted))


if __name__ == '__main__':
    main()
