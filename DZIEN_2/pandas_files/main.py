import pandas as pd

data = {
    'jabłka':[3,7,18,3],
    'pomarańcze':[3,0,9,16],
    'mango':[0,0,2,1],
    'winogrono':[0.3,.5,1,0]
}

pframe = pd.DataFrame(data,index=['Ala','Ola','Jan','Leon'])
print(pframe)

pframe.to_csv('owoce.csv')
print(pframe.info())

print("____________________________________________")

dfzawody = pd.read_csv('zawody.csv')
print(dfzawody)

dfkonkurs = pd.read_json('konkurs.json')
print(dfkonkurs)

