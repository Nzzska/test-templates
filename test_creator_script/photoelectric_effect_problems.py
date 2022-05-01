import json
import random
import os

ev_to_J = 1.6 * 10 ** (-19)

class Table_problem():
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def gather_data(self, variable):
        data = json.load(open(self.data_dir, encoding='utf8'))
        data = data[variable]
        columns = self.init_columns(data, variable)
        for table_item in data:
            for column in data[table_item]:
                columns[variable].append(table_item)
                columns[column].append(data[table_item][column])
        return columns
    
    def init_columns(self, data, variable):
        cols = {}
        cols[variable] = []
        for table_item in data:
            for column in data[table_item]:
                cols[column] = []
        return cols

    def form_tabular(
        self, 
        table_type, 
        content):
        tabular = \
        """\\begin{{figure}}
        \\centering
        \\begin{{tabular}}{{{s}}} 
        \\hline \n""".format(s=table_type)
        cols_names = []
        for content_name in content:
            cols_names.append(content_name)
        row = self.empty_table_row(len(content))
        tabular += self.fill_row_content(
                cols_names,
                row
            )
        for i in range(0, len(content[cols_names[1]])):
            cols = []
            for j in content:
                cols.append(content[j][i])
            tabular += self.fill_row_content(
                cols,
                row
            )
        tabular += ' \n \\end{tabular} \n \\end{figure} \n'
        return tabular

    def empty_table_row(self, number_of_cols):
        output = ''
        for i in range(0, number_of_cols):
            if (i != number_of_cols-1):
                output += "{"+str(i)+"} & "
            else:
                output += "{"+str(i)+"} \\\\ \n \\hline "
        return output

    def fill_row_content(self, content, input):
        output = input
        output = str(output).format(*content)
        return output

    def extract_content_row(self, row_number, content):
        output = []
        for column in content:
            output.append(content[column][row_number])
        return output

    def formulate_problem(
        self, 
        problem_path, 
        placeholder_replacements,
        output_foler,
        number_of_problems,
        problem_naming):
        self.create_problem_dir(output_foler)
        problem = open(problem_path, 'r', encoding='utf8').read()
        for j in range(0, number_of_problems):
            replacements = []
            for i in range(0, len(placeholder_replacements)):
                replacements.append(
                    random.choice(placeholder_replacements[str(i)])
                )
            current_problem = problem.format(*replacements)
            current_name = problem_naming + '_' + str(j) + '.tex'
            open(output_foler+'/'+current_name, 'w+', encoding='utf8').write(
                current_problem
            )


    def create_problem_dir(self, output_folder):
        files = os.listdir()
        if (output_folder not in files):
            print(os.listdir())
            os.mkdir(output_folder)
        else:
            pass
# trial_problem = Table_problem('islaisvinimo_darbai.json')
# data = trial_problem.gather_data("metalai")
# trial_problem.form_tabular(' |c|c|c| ', data)
