import argparse
from dataclasses import dataclass
from getpass import getpass

from passprotect.helpers import (BadPasswordException, file_exists, is_locked,
                                 lock_file, unlock_file)

description = """
A simple CLI tool to encrypt (lock) and decrypt (unlock) files using a password.
"""


@dataclass
class Arguments:
    password: str
    lock: bool
    unlock: bool
    file: str
    output_location: str | None


def parse_arguments() -> Arguments:
    parser = argparse.ArgumentParser(description=description)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-l", "--lock", action="store_true", help="Lock a file")
    group.add_argument("-u", "--unlock", action="store_true", help="Unlock a file")
    parser.add_argument(
        "-o", "--output", help="Location to output the locked / unlocked file"
    )

    parser.add_argument(
        "-n",
        "--no-confirm",
        action="store_true",
        help="No password confirmation for locking files",
    )
    parser.add_argument("file", help="Path to the file")

    args = parser.parse_args()

    if not file_exists(args.file):
        print(f"File {args.file} does not exist")
        exit(0)

    if args.unlock is True:
        print(args.file)
        if not is_locked(args.file):
            print("File is not locked")
            exit()

    password = getpass("Password: ")

    if args.lock is True and args.no_confirm is False:
        confirm_password = getpass("Confirm password: ")

        if password != confirm_password:
            print("Passwords do not match")
            exit(-1)

    if args.output is None:
        output_location = args.file
    else:
        output_location = args.output

    return Arguments(
        password=password,
        file=args.file,
        lock=args.lock,
        unlock=args.unlock,
        output_location=output_location,
    )


def main() -> None:
    arguments = parse_arguments()

    if arguments.lock:
        lock_file(arguments.file, arguments.password, arguments.output_location)
        print(f"File {arguments.file} locked to {arguments.output_location}")
    elif arguments.unlock:
        try:
            unlock_file(arguments.file, arguments.password, arguments.output_location)
            print(f"File {arguments.file} unlocked to {arguments.output_location}")

        except BadPasswordException:
            print("Password does not match")
        except ValueError:
            print("Corrupted file cannot be decrypted")


if __name__ == "__main__":
    main()
