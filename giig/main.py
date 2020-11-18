import sys

import click
import requests
from fuzzywuzzy import process

VERSION = '0.0.2'
# -h로도 help를 볼 수 있도록 한다.
OPTIONS = dict(help_option_names=['-h', '--help'])
HOST_URL = 'https://gitignore.io/api/'
FUZZY_THRESHOLD = 80


@click.group(invoke_without_command=True, context_settings=OPTIONS)
@click.option('-v', '--version', is_flag=True, help='Show version')
def cli(version):
    if version:
        print_version()
        sys.exit(0)


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

    result_list = get_result_list(keyword)

    if len(result_list) == 0:
        click.echo('No results found')
        sys.exit(0)

    click.echo(result_list)


@cli.command(help='Show api results')
@click.argument('items', nargs=-1)
def show(items):
    items = validate_items(items)
    check_item_length(items)
    click.echo(get_gitignore(items))


@cli.command(help='Make .gitignore')
@click.argument('items', nargs=-1)
@click.option('-a', '--append', is_flag=True, help='append to .gitignore')
def make(items, append):
    if append:
        file = open('.gitignore', 'a')
    else:
        file = open('.gitignore', 'w')

    items = validate_items(items)
    check_item_length(items)
    file.write(get_gitignore(items))
    file.close()


def get_list():
    return requests.get(HOST_URL + 'list').text


def get_gitignore(items):
    return requests.get(HOST_URL + ','.join(items)).text


def get_result_list(keyword):
    search_list = get_search_list()
    return [result[0] for result in process.extract(keyword, search_list) if result[1] > FUZZY_THRESHOLD]


def get_search_list():
    return sorted(','.join(get_list().split('\n')).split(','))


def validate_items(items):
    validated_items = []
    search_list = get_search_list()
    for item in items:
        if item in search_list:
            validated_items.append(item)

    return validated_items


def check_item_length(items):
    if len(items) == 0:
        click.echo('Please check your input')
        sys.exit(1)


if __name__ == '__main__':
    cli()
