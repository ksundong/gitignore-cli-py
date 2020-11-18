import sys

import click
import requests
from fuzzywuzzy import process

VERSION = '0.0.1'
# -h로도 help를 볼 수 있도록 한다.
OPTIONS = dict(help_option_names=['-h', '--help'])
HOST_URL = 'https://gitignore.io/api'
FUZZY_THRESHOLD = 80


@click.group(invoke_without_command=True, context_settings=OPTIONS)
@click.option('-v', '--version', is_flag=True, help='Show version')
def cli(version):
    if version:
        print_version()


def print_version():
    click.echo('giig version: ' + VERSION)


@cli.command(help='Show a list of the ignorable items')
def list():
    click.echo(get_list())


@cli.command(help='Fuzzy search in ignorable items')
@click.argument('keyword')
def search(keyword):
    if not keyword:
        click.echo('No args, args required')

    click.echo('Finding... ' + str(keyword))

    search_list = sorted(','.join(get_list().split('\n')).split(','))
    result_list = [result[0] for result in process.extract(keyword, search_list) if result[1] > FUZZY_THRESHOLD]

    if len(result_list) == 0:
        click.echo('No results found')
        sys.exit(0)

    click.echo(result_list)


@cli.command()
def show():
    pass


@cli.command()
def make():
    pass


def get_list():
    return requests.get(HOST_URL + '/list').text


if __name__ == '__main__':
    cli()
