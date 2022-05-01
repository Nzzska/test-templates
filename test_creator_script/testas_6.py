from main_v2 import Test
from photoelectric_effect_problems import Table_problem

title_text = '''Kontrolinis darbas, 6 skyrius I grupė'''
active_test = Test(name='6 skyrius', title=title_text)

active_test.get_questions('./testiniai/', 4)
active_test.form_multicolumns(2)
active_test.replace_placeholders("%Q0%")

active_test.get_questions('./insert/', 4)
active_test.replace_placeholders("%Q1%")

third_problem = Table_problem('islaisvinimo_darbai.json')

data_metals = third_problem.gather_data("metalai")
data_photons = third_problem.gather_data("fotonai")

metals_table = third_problem.form_tabular(' |c|c|c| ', data_metals)
photons_table = third_problem.form_tabular(' |c|c|c| ', data_photons)

test_table = metals_table + photons_table
active_test.content = test_table
active_test.replace_placeholders("%Q2%")

third_problem_placeholders = {
    '0': ['Li', 'Na', 'Cs', 'Ca', 'Nb', 'Zr'],
    '1': ['violetinės', 'mėlynos', 'žydros', 'žalios']
}
third_problem.formulate_problem(
    'trecia_užduotis.tex',
    third_problem_placeholders,
    'trecia',
    12,
    'trecia'
)

active_test.get_questions('./trecia/', 2)
active_test.replace_placeholders("%Q3%")

active_test.get_questions('./ketvirta/', 3)
salyga = '''Užbaikite rašyti duotas lygtis, jei trūksta skaičių įrašykite skaičius, jei pateiktas klaustukas, 
raskite to elemento nukleonų skaičius.'''
active_test.parts_problem(salyga)
active_test.replace_placeholders('%Q4%')

active_test.export_test('./testas/testas.tex')
