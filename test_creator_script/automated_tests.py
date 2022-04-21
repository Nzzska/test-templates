from main_v2 import Test

#Testing Test.get_questions()
def test_get_questions():
    test_object = \
        Test()
    #Fetching questions
    choices = \
        test_object.get_questions('./testiniai/', 4)
    try:
        print(type(choices) == list)
        print(choices)
        print('Test passed!')
    except:
        print('get_questions didn\'t pass the test')
        pass

#Testing file as string
def test_file_as_string():
    test_object = \
        Test()
    content = test_object.file_as_string('./testiniai/testinis6_1.tex')
    try:
        print(content)
        print('test_file_as_string')
        print('test passed!')
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
with open('./test_output.txt', 'w+') as f:
    f.write(output_text)
    print(output_text)