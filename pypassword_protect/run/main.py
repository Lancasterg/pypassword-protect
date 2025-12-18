import argparse
from getpass import getpass

from pypassword_protect.source.encryption_decryption import create_file, CurrentState
from dataclasses import dataclass

description = """
Password-protect files. 

Can: 
1. Create a new encrypted file with the postfix .enc
2. 



    # parser.add_argument("file", help="File to encrypt or decrypt")
    # parser.add_argument("-l", "--lock", action="store_true", help="Lock (encrypt) file")
    # parser.add_argument(
    #     "-u", "--unlock", action="store_true", help="Unlock (decrypt) file"
    # )

"""


@dataclass
class ProtectedFile:
    new: str | None
    password: str | None
    state: CurrentState = CurrentState.UNLOCKED


def parse_arguments() -> ProtectedFile:
    parser = argparse.ArgumentParser(description="Password-protect files")

    parser.add_argument("-n", "--new", help="Create a new file")
    parser.add_argument("-p", "--password", action="store_true", help="Password for the new file")

    args = parser.parse_args()

    if args.password is True:
        password = getpass()
    else:
        password = ""  # empty string for now
    return ProtectedFile(
        new=args.new,
        password=password
    )


def main():

    protected_file = parse_arguments()

    # if args.new is not None:
    #     create_file(args.new)
    #
    # else:
    #     if args.encrypt is True and args.decrypt is False:
    #         print("encrypt")
    #         # encrypt_file(args.file)
    #     elif args.decrypt is True and args.encrypt is False:
    #         print("decrypt")
    #         # decrypt_file(args.file)
    #     else:
    #         raise ValueError("Only one of --encrypt (-e) or --decrypt (-d) must be passed")


if __name__ == "__main__":
    main()
