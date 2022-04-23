import json
import random

ev_to_J = 1.6 * 10 ** (-19)

class Table_problem():
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def gather_data(self, variable):
        data = json.load(open(self.data_dir))
        data = data[variable]
        columns = self.init_columns(data, variable)
        for table_item in data:
            for column in data[table_item]:
                columns[variable].append(table_item)
                columns[column].append(data[table_item][column])
        print(columns)
    
    def init_columns(self, data, variable):
        cols = {}
        cols[variable] = []
        for table_item in data:
            for column in data[table_item]:
                cols[column] = []
        return cols

    def form_tabular(self, table_type, cols_no, rows_no):
        start = \
        """\\begin{{center}}
        \\begin{{tabular}}{s} 
        \\hline""".format(s=table_type)
        pass



trial_problem = Table_problem('islaisvinimo_darbai.json')
trial_problem.gather_data("metalai")
