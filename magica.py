# -*- coding:utf-8 -*-
import click
import magica_core.core as core

@click.group()
def cli():
    pass


@cli.command()
def notes():
    """This function is intended to print all existing notes."""
    data = core.notes()
    for i in range(data[0]):
        print('{:4d}| {:20} ({:d} books)'.format((i+1), data[1][i][0], data[1][i][1]))
    print('   total {:d} notes'.format(data[0]))


@cli.command()
@click.argument('note')
def make(note):
    """This function is intended to make a new note.

    :param str note: The name of the note to be created.
    """
    core.make(note)

@cli.command()
@click.argument('note')
def add(note):
    """

    Keyword arguments:
    note -- note's name
    :return:
    """
    pass

@cli.command()
@click.argument('note')
@click.argument('title', required=False)
def info(note, title):
    pass

@cli.command()
@click.argument('note')
@click.argument('title', required=False)
def remove(note, title):
    pass

@cli.command()
@click.argument('note')
@click.option('--type', default='csv')
def save(note, type):
    pass


if __name__=="__main__":
    cli()
