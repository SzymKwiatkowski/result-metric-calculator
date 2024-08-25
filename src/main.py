"""Main script"""
import argparse

from utils.helpers import load_config


def main(args):
    """Main executable script"""
    config = load_config(args.config)
    area = config['AREA']
    print(area)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')
    parser.add_argument('-c', '--config', action='store', default='../config.yaml')
    parser.add_argument('-e', '--epochs', action='store', default=50,
                        type=int, help='Specified number of maximum epochs')
    parser.add_argument('-d', '--data', action='store', default="../data",
                        type=str, help='Path to root folder of data')
    parser.add_argument('-n', '--use-neptune', action='store', type=bool, default=False,
                        help="Use neptune logger with credentials provided in config")
    args_parsed = parser.parse_args()
    main(args_parsed)
