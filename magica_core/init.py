import os

def init():
    if not os.path.exists('db.json'):
        import json
        from collections import OrderedDict

        init_data = OrderedDict()
        accounts = OrderedDict()
        notes = OrderedDict()


        init_data['auto_named'] = 0
        init_data['accounts'] = accounts
        init_data['notes'] = notes

        with open('db.json', 'w') as fp:
            json.dump(init_data, fp)
