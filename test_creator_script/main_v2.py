import random
import os

question_placeholders = [
    '%Q0%', '%Q1%', 
    '%Q2%', '%Q3%', 
    '%Q4%', '%Q5%', 
    '%Q6%'
]

class Test():
    def __init__(
        self,
        name='bandomasis',
        title='bandomasis',
        template_location='template.tex'):

        self.title = title
        self.name = name
        self.questions = []
        self.content = ''
        self.tex = open(
            template_location, 
            'r', 
            encoding="utf8").read()
        self.replace_placeholders(placeholder="%TITLE%")
        

    def get_questions(self, folder_name, number_of_questions):
        choices = []
        while (len(choices) != number_of_questions):
            current_choice = folder_name +\
                random.choice(os.listdir(folder_name))
            if (current_choice not in choices):
                choices.append(current_choice)
        self.choices = choices
        self.fnames_to_strings()
        #Returns list of files tex files (questions)

    def fnames_to_strings(self):
        self.choices_content = []
        #print(self.choices)
        for choice in self.choices:
            self.choices_content \
                .append(self.file_as_string(choice))
        self.choices = []
        self.content = \
            self.concat_pieces(self.choices_content)

    def file_as_string(self, filename):
        print(filename)
        content = open(filename, 'r', encoding="utf8") \
            .read()
        return content
    
    #pieces = list of strings
    def concat_pieces(self, pieces):
        final_string = ''
        try:
            for piece in pieces:
                final_string += piece +'\n'
            return final_string
        except:
            print(type(pieces))
            print('error in concat_pieces function')
            pass

    def form_multicolumns(
        self, 
        number_of_columns):
        first_line = \
            '\\raggedcolumns\\begin{{multicols}} \
            {{{no_of_cols}}} \n' \
            .format(no_of_cols = number_of_columns)
        last_line = '\\end{multicols} \n'
        self.content = first_line + self.content + last_line

    def center_content(self):
        first_line = '\\begin{center} \n'
        last_line = '\\end{center} \n'
        self.content = first_line + \
            self.content + last_line

    def replace_placeholders(self, placeholder):
        if (placeholder == "%TITLE%"):
            self.tex = self.tex.replace(placeholder, self.title)
        else:
            self.tex = self.tex.replace(placeholder, self.content)
            self.content = ''

    def export_test(self, filename):
        open(filename, 'w+', encoding="utf8").write(self.tex)

    def parts_problem(self, text):
        beggining = "\\question {0}\\begin{{parts}} \n".format(text)
        ending = "\\end{parts}"
        self.content = beggining + self.content + ending
