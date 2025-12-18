import argparse

description = """
Password-protect files. 

Can: 
1. Create a new encrypted file with the postfix .enc
2. 

"""


def main():
    parser = argparse.ArgumentParser(description="Password-protect files")
    mode = parser.add_mutually_exclusive_group()

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("-l", "--lock", action="store_true", help="Lock (encrypt) file")
    mode.add_argument(
        "-u", "--unlock", action="store_true", help="Unlock (decrypt) file"
    )

    parser.add_argument("-n", "--new", help="Create a new file")

    parser.add_argument("file", help="File to encrypt or decrypt")

    args = parser.parse_args()

    print(args)

    if args.encrypt is True and args.decrypt is False:
        print("encrypt")
        # encrypt_file(args.file)
    elif args.decrypt is True and args.encrypt is False:
        print("decrypt")
        # decrypt_file(args.file)
    else:
        raise ValueError("Only one of --encrypt (-e) or --decrypt (-d) must be passed")


if __name__ == "__main__":
    main()
