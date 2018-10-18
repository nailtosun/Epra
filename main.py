import progressbar
from time import sleep
from data_formatter import *
import pandas as pd
import time
import os
from normalizer import *

cwd=os.getcwd()
kcetas_file_name = 'kcetas_ildem_all.xlsx'
kaski_file_name = 'kaski_ildem_all.xlsx'
path_kcetas = cwd+'\\Verisetler'+ '\\' + kcetas_file_name
path_kaski = cwd + '\\Verisetler' + '\\' + kaski_file_name

df_kcetas = xlsx_2_df(path_kcetas)
df_kaski = xlsx_2_df(path_kaski)
# Gereksiz kolonları eleme
column_of_interest_kaski = ['MAHALLE_ACIKLAMA', 'CADDE_SOKAK_ACIKLAMA',
                            'KAPI', 'DAIRE', 'ABONE_TIP_ACIKLAMA', 'OKUMA_TARIHI', 'FATURA_ODENEN_TUTAR']
column_of_interest_kcetas = ['SEMT', 'CADDESOKAK', 'BINANO',
                             'DAIRENO', 'ADI', 'AKTIFTUK', 'ORTALAMA', 'SONOKUTAR']

df_kaski = df_kaski[column_of_interest_kaski]
df_kcetas = df_kcetas[column_of_interest_kcetas]

# %%
# Stringleri title etme
bar = progressbar.ProgressBar(maxval=len(df_kcetas), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(1, len(df_kcetas)):
    df_kcetas[df_kcetas.columns[0]][i] = df_kcetas[df_kcetas.columns[0]][i].title()
    df_kcetas[df_kcetas.columns[1]][i] = df_kcetas[df_kcetas.columns[1]][i].title()
    bar.update(i+1)
bar.finish()

bar = progressbar.ProgressBar(maxval=len(df_kaski), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(1, len(df_kaski)):
    df_kaski[df_kaski.columns[0]][i] = df_kaski[df_kaski.columns[0]][i].title()
    df_kaski[df_kaski.columns[1]][i] = df_kaski[df_kaski.columns[1]][i].title()
    bar.update(i+1)
bar.finish()
# %%
cadde_sokak_set_kcetas = list(set(df_kcetas[df_kcetas.columns[1]]))
cadde_sokak_set_kaski = list(set(df_kaski[df_kaski.columns[1]]))
similar_list = []
delete_list = []
for xx in range(90,60,-5):
    for i in range(len(cadde_sokak_set_kcetas)):
        for j in range(len(cadde_sokak_set_kaski)):
            threshold = similar(cadde_sokak_set_kcetas[i], cadde_sokak_set_kaski[j])
            if threshold > xx/100:
                small_list = [cadde_sokak_set_kaski[j], cadde_sokak_set_kcetas[i]]
                if (cadde_sokak_set_kaski[j] not in delete_list) and (cadde_sokak_set_kcetas[i] not in delete_list):
                    similar_list.append(small_list)
                    delete_list.append(cadde_sokak_set_kaski[j])
                    delete_list.append(cadde_sokak_set_kcetas[i])
# Mahalle isimlerini eşleme
kaski_mahalle = df_kaski[df_kaski.columns[0]][1]
kcetas_mahalle = df_kcetas[df_kcetas.columns[0]][1]

df_kaski[df_kaski.columns[0]] = [
    w.replace(kaski_mahalle, kcetas_mahalle) for w in df_kaski[df_kaski.columns[0]]]

df_kcetas['ORTALAMA'] = [str(x).replace('.', ',') for x in df_kcetas['ORTALAMA']]
df_kcetas['DAIRENO'] = [str(x).replace('-','') for x in df_kcetas['DAIRENO']]
df_kaski['DAIRE'] = [str(x).zfill(2) for x in df_kaski['DAIRE']]
df_kcetas['DAIRENO'] = [str(x).zfill(2) for x in df_kcetas['DAIRENO']]

final_column_kaski = ['ADRES', 'OKUMA_TARIHI','ABONE_TIP_ACIKLAMA','FATURA_ODENEN_TUTAR']
final_column_kcetas = ['ADRES', 'SONOKUTAR', 'AKTIFTUK', 'ORTALAMA']

df_kaski_final = pd.DataFrame(columns=final_column_kaski)
df_kcetas_final = pd.DataFrame(columns=final_column_kcetas)
# %%
bar = progressbar.ProgressBar(maxval=len(df_kaski), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(1, len(df_kaski)):
    row = {'ADRES': df_kaski['MAHALLE_ACIKLAMA'][i] + ' ' + df_kaski['CADDE_SOKAK_ACIKLAMA'][i] + ' BINANO:' + str(df_kaski['KAPI'][i]) + ' DAIRENO:' + str(df_kaski['DAIRE'][i]),
           'OKUMA_TARIHI': df_kaski['OKUMA_TARIHI'][i],
           'ABONE_TIP_ACIKLAMA': df_kaski['ABONE_TIP_ACIKLAMA'][i],
           'FATURA_ODENEN_TUTAR': df_kaski['FATURA_ODENEN_TUTAR'][i]}
    df = pd.DataFrame(data=row, index=[0])
    df_kaski_final = df_kaski_final.append(df)
    bar.update(i+1)
bar.finish()
# %%
bar = progressbar.ProgressBar(maxval=len(df_kcetas), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(1, len(df_kcetas)):
    row = {'ADRES': df_kcetas['SEMT'][i] + ' ' + df_kcetas['CADDESOKAK'][i] + ' ' + 'BINANO:' + str(df_kcetas['BINANO'][i]) + ' '+'DAIRENO:' + str(df_kcetas['DAIRENO'][i]),
           'SONOKUTAR': df_kcetas['SONOKUTAR'][i],
           'AKTIFTUK': df_kcetas['AKTIFTUK'][i],
           'ORTALAMA': df_kcetas['ORTALAMA'][i]}
    df = pd.DataFrame(data=row, index=[0])
    df_kcetas_final = df_kcetas_final.append(df)
    bar.update(i+1)
bar.finish()
# %%
set_kcetas = list(set(df_kcetas_final['ADRES']))
set_kaski = list(set(df_kaski_final['ADRES']))
ortak_adres_list = []
bar = progressbar.ProgressBar(maxval=len(set_kcetas), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(len(set_kcetas)):
    for j in range(len(set_kaski)):
        if set_kcetas[i] == set_kaski[j]:
            ortak_adres_list.append(set_kcetas[i])
            j = len(set_kaski)-1
        else:
            pass
    bar.update(i+1)
bar.finish()
list_2_csv(ortak_adres_list,'ortak_adres_list.csv')
# %%
# Filtering the addresses that are not matched
df_out = pd.DataFrame(columns=final_column_kcetas)
bar = progressbar.ProgressBar(maxval=len(ortak_adres_list), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(len(ortak_adres_list)):
    for j in range(len(df_kcetas_final)):
        if ortak_adres_list[i]==df_kcetas_final['ADRES'][j]:
            row = {'ADRES': df_kcetas_final['ADRES'][j], 'AKTIFTUK': df_kcetas_final['AKTIFTUK'][j], 'ORTALAMA': df_kcetas_final['ORTALAMA'][j] ,'SONOKUTAR': df_kcetas_final['SONOKUTAR'][j]}
            df_row = pd.DataFrame(data=row,index = ['0'])
            df_out = df_out.append(df_row)
    bar.update(i+1)
bar.finish()

df_out_2 = pd.DataFrame(columns=final_column_kaski)
for i in range(len(ortak_adres_list)):
    for j in range(len(df_kaski_final)):
        if ortak_adres_list[i]==df_kaski_final['ADRES'][j]:
            row = {'ADRES': df_kaski_final['ADRES'][j], 'OKUMA_TARIHI': df_kaski_final['OKUMA_TARIHI'][j],'ABONE_TIP_ACIKLAMA': df_kaski_final['ABONE_TIP_ACIKLAMA'][j],'FATURA_ODENEN_TUTAR' :df_kaski_final['FATURA_ODENEN_TUTAR'][j]}
            df_row = pd.DataFrame(data=row,index = ['0'])
            df_out_2 = df_out_2.append(df_row)
    bar.update(i+1)
bar.finish()

df_out_2.to_csv('kaski_sıralanacak.csv',encoding = 'utf-16')
df_out.to_csv('kcetas_sıralanacak.csv',encoding = 'utf-16')

# Sorting önce tarihler sonra adresler
kcetas_file_name = 'kcetas_sıralanacak.csv'
kaski_file_name = 'kaski_sıralanacak.csv'
path_kcetas = cwd+ '\\' + kcetas_file_name
path_kaski = cwd + '\\' + kaski_file_name
normalize_edilecek_kcetas=pd.read_csv(path_kcetas) # encoding = 'utf-16'
normalize_edilecek_kaski=pd.read_csv(path_kaski)
# Normalizing the bills
kcetas_normalized = kcetas_normalizer(normalize_edilecek_kcetas)
kaski_normalized = kaski_normalizer(normalize_edilecek_kaski)

# %%
if len(kaski_normalized) == len(kcetas_normalized):
    print('ok')
    format = ['ADRES','TIPI','DONEM','KCETAS','KASKI']
    kcetas_normalized.to_csv('kcetas_out.csv',encoding='utf-16')
    kaski_normalized.to_csv('kaski_out.csv',encoding='utf-16')
else:
    raise ValueError('Uzunlukları eşit değil farklılıklar kontrol et!')
# %%
# prints the missing and additional elements in list2
list1=set(kcetas_normalized.ADRES)
list2=set(kaski_normalized.ADRES)
set(list1).difference(list2)
set(list2).difference(list1)
