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
    for i in data[1]:
        print('{:20} ({:d} books)'.format(i[0], i[1]))
    print('\ntotal {:d} notes'.format(data[0]))


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

    query = input("title | ")
    answer = dict()

    try:
        answer = core.search_by_title(query)['channel']['item']
    except:
        print("{0}: {1}".format(core.search_by_title(query)['errorType'], core.search_by_title(query)['message']))
        return

    print("|No|          Title          |    Author    |   Publisher   |  Date  |")
    for i in range(len(answer)):
        print("|{:2d}|{:25}|{:14}|{:15}|{:8}|".format(i+1,
                                                       answer[i]['title'],
                                                       answer[i]['author'],
                                                       answer[i]['pub_nm'],
                                                       answer[i]['pub_date']))
    book_num = input("Input number | ")

    while book_num > len(answer) or book_num <= 0:
        print("Incorrect number!")
        book_num = input("Input number | ")

    book_num -= 1

    book_info = {
        'title': answer[book_num]['title'],
        'author': answer[book_num]['author'],
        'publisher': answer[book_num]['pub_nm'],
        'date': answer[book_num]['pub_date'],
        'isbn': answer[book_num]['isbn']
    }

    core.add(note, book_info)



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
def export(note, type):
    pass


if __name__ == "__main__":
    cli()
