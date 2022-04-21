import json
import random

ev_to_J = 1.6 * 10 ** (-19)

class Photoelectric_effect_problem():
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def gather_data(self):
        pass

data = json.load(open('islaisvinimo_darbai.json'))
print(data)
uzduoties_txt = open('trecia_užduotis.txt', 'r', encoding='utf8').read()
print(uzduoties_txt)