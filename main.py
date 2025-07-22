import argparse
from vault import add_password, get_password, delete_password, edit_service, list_services


def main():
    parser = argparse.ArgumentParser(description='Password Manager CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Add command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('--service', required=True)
    add_parser.add_argument('--username', required=True)
    add_parser.add_argument('--password', required=True)

    # Get command
    get_parser = subparsers.add_parser('get')
    get_parser.add_argument('--service', required=True)

    # Delete command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('--service', required=True)

    # Edit command
    edit_parser = subparsers.add_parser('edit')
    edit_parser.add_argument('--service', required=True)
    edit_parser.add_argument('--username')
    edit_parser.add_argument('--password')

    # List command
    subparsers.add_parser('list')

    args = parser.parse_args()

    if args.command == 'add':
        add_password(args.service, args.username, args.password)
    elif args.command == 'get':
        get_password(args.service)
    elif args.command == 'delete':
        delete_password(args.service)
    elif args.command == 'edit':
        edit_service(args.service, args.username, args.password)
    elif args.command == 'list':
        list_services()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
