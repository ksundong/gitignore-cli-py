import sys

import click

VERSION = '0.0.1'


@click.command()
@click.option('-v', '--version', is_flag=True, help='Show version')
def main(version):
    if version:
        print_version()
        sys.exit()


def print_version():
    click.echo('giig version: ' + VERSION)


if __name__ == '__main__':
    main()
