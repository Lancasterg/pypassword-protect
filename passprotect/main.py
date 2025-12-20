import argparse
from dataclasses import dataclass
from getpass import getpass

from passprotect.helpers import (
    lock_file,
    unlock_file,
    BadPasswordException,
    is_locked,
    file_exists,
)

description = """
Password-protect files. 
    TODO: write more in here :)
"""


@dataclass
class Arguments:
    password: str
    lock: bool
    unlock: bool
    file: str


def parse_arguments() -> Arguments:
    parser = argparse.ArgumentParser(description=description)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-l", "--lock", action="store_true", help="Lock a file")
    group.add_argument("-u", "--unlock", action="store_true", help="Unlock a file")

    parser.add_argument(
        "-n",
        "--no-confirm",
        action="store_true",
        help="Don't require lock password confirmation",
    )
    parser.add_argument("file", help="Path to the file")

    args = parser.parse_args()

    if not file_exists(args.file):
        print(f"File {args.file} does not exist")
        exit(0)

    if args.unlock is True:
        if not is_locked(args.file):
            print("File is not locked")
            exit()

    password = getpass("Password: ")

    if args.lock is True and args.no_confirm is False:
        confirm_password = getpass("Confirm password: ")

        if password != confirm_password:
            print("Passwords do not match")
            exit(-1)

    return Arguments(
        password=password, file=args.file, lock=args.lock, unlock=args.unlock
    )


def main() -> None:
    arguments = parse_arguments()

    if arguments.lock:
        lock_file(arguments.file, arguments.password)

    elif arguments.unlock:
        try:
            unlock_file(arguments.file, arguments.password)
        except BadPasswordException:
            print("Password does not match")


if __name__ == "__main__":
    main()
