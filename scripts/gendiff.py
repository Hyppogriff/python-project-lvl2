import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.print_help()


if __name__ == '__main__':
    main()
