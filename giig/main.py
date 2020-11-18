import click
import requests

VERSION = '0.0.1'
# -h로도 help를 볼 수 있도록 한다.
OPTIONS = dict(help_option_names=['-h', '--help'])
HOST_URL = 'https://gitignore.io/api'


@click.group(invoke_without_command=True, context_settings=OPTIONS)
@click.option('-v', '--version', is_flag=True, help='Show version')
def cli(version):
    if version:
        print_version()


def print_version():
    click.echo('giig version: ' + VERSION)


@cli.command(help='Show a list of the ignorable items')
def list():
    res = requests.get(HOST_URL + '/list')
    click.echo(res.text)


@cli.command()
def search():
    pass


@cli.command()
def show():
    pass


@cli.command()
def make():
    pass


if __name__ == '__main__':
    cli()
