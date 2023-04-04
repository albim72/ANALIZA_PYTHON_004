import pandas as pd
import xlsxwriter

df = pd.DataFrame({'Dane':[10,12,30,120,128,190,220,270,300,310,330,360,400,450,500]})

writer = pd.ExcelWriter('pandas_data.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='ramka')
writer.save()
