question_placeholders = [
    '%Q0%', '%Q1%', '%Q2%', '%Q3%', '%Q4%', '%Q5%', '%Q6%'
]

class Test():
    def __init__(
        self, 
        name='bandomasis', 
        title='bandomasis', 
        mcq_folder='../testiniai',
        number_of_mcq = 4,
        mcq_base_name = ''):
        mcq = Multiple_choice_question('../testiniai/testinis6_1.tex')
        with open(str(name)+'.tex', 'w') as test:
            with open('../title/title.tex', 'r') as title_tex:
                for title_line in title_tex.readlines():
                    if (title_line+'\n' in question_placeholders):
                        test.write(mcq.question_string)
                    else:
                        test.write(title_line)
        #testuojam inserta.
        a = self.insert_question('../multiple_choice/multiple_choice.tex')

    def insert_question(self, question_path):
        content = open(str(question_path), 'r').read()
        print(content)
        return content

class Multiple_choice_question():
    def __init__(self, question_path, number_of_questions = 3):
        self.question_string = ''
        for i in range(0,number_of_questions):
            self.question_path = question_path
            self.question_string += self.format_question()
        self.question_string += '\\end{multicols}'

    def parse_question(self):
        question = {'ans':[]}
        with open(self.question_path, 'r') as question_file:
            for line in question_file.readlines():
                if line.startswith('Q'):
                    question['Q'] = line[1:].strip()
                else:
                    question['ans'].append(line.strip())
        return question

    def format_question(self):
        question = self.parse_question()

        formated_question = """
        \\raggedcolumns\\begin{multicols}{2}
            \\question %s \\begin{choices}
                \\choice %s
                \\choice %s
                \\choice %s
                \\choice %s
            \\end{choices}
        """ %(
            question['Q'], 
            question['ans'][0],
            question['ans'][1],
            question['ans'][2],
            question['ans'][3]
        )

        return formated_question

# mcq = Multiple_choice_question('../testiniai/testinis6_1.tex')
# print(mcq.question_string)
# with open('bandymas.tex', 'w') as bandymas:
#     bandymas.write(mcq.question_string)

Test()