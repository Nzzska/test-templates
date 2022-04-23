import json

data = json.load(open('islaisvinimo_darbai.json'))
data = data['metalai']
for data_item in data:
    print(data_item + ':' + str(data[data_item]['energija']))