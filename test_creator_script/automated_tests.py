from main_v2 import Test
from photoelectric_effect_problems import Table_problem

#Testing Test.get_questions()
def test_get_questions():
    test_object = \
        Test()
    #Fetching questions
    choices = \
        test_object.get_questions('./testiniai/', 4)
    try:
        #print(type(choices) == list)
        #print(choices)
        print('Test passed! get_questions')
    except:
        print('get_questions didn\'t pass the test')
        pass

#Testing file as string
def test_file_as_string():
    test_object = \
        Test()
    content = test_object.file_as_string('./testiniai/testinis6_1.tex')
    try:
        #print(content)
        print('test_file_as_string test passed!')
        return content
    except:
        print('negerai test_file_as_string')
        pass

#ToDo Test centering and multicols:
    def test_multicols():
        pass

    def test_center():
        pass

    def test_replace_placeholder():
        pass

    
#Excecuting tests   
test_get_questions()
output_text = test_file_as_string()
with open('./test_output.txt', 'w+', encoding='utf8') as f:
    f.write(output_text)

#Generate trial test:
trial_title = \
''' 
Čia yra bandomasis kontrolinis darbas sugeneruotas Oskaro Balkaus sunkiu 2,5 dienų darbo \n
prašome vertinti, gerbti ir mylėti
'''
trial_test =  Test(name='trial', title=trial_title)
trial_test.get_questions('./testiniai/', 4)
trial_test.form_multicolumns(2)
trial_test.replace_placeholders("%Q0%")
trial_test.get_questions('./insert/', 4)
trial_test.replace_placeholders("%Q1%")

trial_problem = Table_problem('islaisvinimo_darbai.json')
data = trial_problem.gather_data("metalai")
trial_table = trial_problem.form_tabular(' |c|c|c| ', data)

data_two = trial_problem.gather_data("fotonai")
trial_table_two = trial_problem.form_tabular(' |c|c|c| ', data_two)

trial_table += trial_table_two

trial_test.content = trial_table
trial_test.form_multicolumns(2)
trial_test.replace_placeholders("%Q2%")
trial_placeholders = {
    '0': ['Li', 'Na', 'Cs', 'Ca', 'Nb', 'Zr'],
    '1': ['violetinės', 'mėlynos', 'žydros', 'žalios']
}
trial_problem.formulate_problem(
    'trecia_užduotis.tex',
    trial_placeholders,
    'trecia',
    12,
    'trecia'
)
trial_test.get_questions('./trecia/', 1)
trial_test.replace_placeholders("%Q3%")

trial_test.export_test('./trial/trial_test.tex')