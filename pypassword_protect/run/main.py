import argparse
from dataclasses import dataclass
from getpass import getpass

from pypassword_protect.source.helpers import lock_file, unlock_file

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

    parser.add_argument(
        "-l", "--lock", action="store_true", help="Lock (encrypt) the file"
    )
    parser.add_argument(
        "-u", "--unlock", action="store_true", help="Unlock (decrypt) the file"
    )
    parser.add_argument("-f", "--file", help="Path to the file", required=True)

    args = parser.parse_args()

    password = getpass()

    arguments = Arguments(
        password=password, lock=args.lock, unlock=args.unlock, file=args.file
    )

    if arguments.lock is True and arguments.unlock is True:
        raise ValueError("Cannot both lock and unlock the file at the same time")
    if arguments.lock is False and arguments.unlock is False:
        raise ValueError("Must either lock or unlock the file")

    return arguments


def main() -> None:
    arguments = parse_arguments()
    if arguments.lock:
        lock_file(arguments.file, arguments.password)
    elif arguments.unlock:
        unlock_file(arguments.file, arguments.password)


if __name__ == "__main__":
    main()
