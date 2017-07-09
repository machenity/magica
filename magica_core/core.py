import json, os

def check_init(func):
    def wrapper(*args):
        if not os.path.exists('db.json'):
            init_data = dict()
            accounts = dict()
            notes = dict()

            init_data['auto_named'] = 0
            init_data['accounts'] = accounts
            init_data['notes'] = notes

            with open('db.json', 'w') as fp:
                json.dump(init_data, fp)
        func(*args)
    return wrapper

@check_init
def make(new_note=''):
    """This function is intended to make a new note.
    이 함수는 새로운 노트를 생성한다.

    :param new_note: A string to be a name of the note to be created.
    생성될 노트의 이름이 될 문자열이다.
    """
    if not (type(new_note) == str):
        raise TypeError

    with open('db.json', 'r') as f:
        db = json.load(f)

    if new_note in db['notes'].keys():
        raise ValueError

    if not new_note:
        num = db['auto_named']
        name = 'note{:d}'.format(num)
        while name in db['notes']:
            num += 1
            name = 'note{:d}'.format(num)
        db['notes'][name] = {}

    else:
        db['notes'][new_note] = {}

    with open('db.json','w') as f:
        json.dump(db, f, ensure_ascii=False)


def notes():
    with open('db.json', 'r') as f:
        db = json.load(f)
        number = len(db['notes'])
        note_list = [(note, len(db['notes'][note])) for note in db['notes'].keys()]

    return [number, note_list]

