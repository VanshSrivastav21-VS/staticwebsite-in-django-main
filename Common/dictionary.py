data = {
    'name': 'Vansh Srivastav',
    'age': '23',
    'skills': ['C','C++','Java']
}

print(data['name'])
print(data['age'])
print(data['skills'][-1])

data2 = {
    'report':{
        'alex':{
            'maths':[45,48,50],
                'science':[55,60,70]
         },
         'amit':{
             'maths':[46,49,51],
             'science':[56,61,71]
         }
    }
}

print(data2['report']['alex'])
print(data2['report']['amit'])

print(sum(data2['report']['alex']['maths']))
print(sum(data2['report']['amit']['science']))