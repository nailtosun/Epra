# Faturaları normalize eder.
import pandas as pd

def kcetas_normalizer(df_out):
    c = 0
    columns = df_out.columns
    df_sorunlu = pd.DataFrame(columns=columns)
    df_out_sorunlu = pd.DataFrame(columns=columns)
    df_out['ADRES'][2]
    carrier = []
    counter = 0
    FIRST_DAY = '01.01.2015'
    LAST_DAY = '31.12.2017'
    THRESHOLD = 20
    outcolumns=['ADRES','AKTIFTUK','DONEM']
    df_out_edit=pd.DataFrame(columns = outcolumns)
    bar = progressbar.ProgressBar(maxval=len(df_out), \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for i in range(1,len(df_out)-1):
        if df_out['ADRES'][i]==df_out['ADRES'][i+1] and df_out['ADRES'][i-1]!=df_out['ADRES'][i]:
            for a in range(difference(df_out['SONOKUTAR'][i],FIRST_DAY)):
                carrier.append(df_out['ORTALAMA'][i])
            counter = counter + 1
        #yılın ara tarihleri
        if df_out['ADRES'][i]==df_out['ADRES'][i+1] and df_out['ADRES'][i]==df_out['ADRES'][i-1]:
            for a in range(difference(df_out['SONOKUTAR'][i],df_out['SONOKUTAR'][i-1])):
                carrier.append(df_out['ORTALAMA'][i])
            counter = counter + 1
        #yılın son ayı
        if df_out['ADRES'][i-1]==df_out['ADRES'][i] and df_out['ADRES'][i] != df_out['ADRES'][i+1]:
            for a in range(difference(LAST_DAY,df_out['SONOKUTAR'][i])):
                carrier.append(df_out['ORTALAMA'][i])
            for b in range(difference(df_out['SONOKUTAR'][i],df_out['SONOKUTAR'][i-1])):
                carrier.append(df_out['ORTALAMA'][i])
            counter = counter + 1
            if len(carrier)==365*3:
                ocak_list_15 = round(sum(carrier[:31]),2)
                subat_list_15 = round(sum(carrier[31:59]),2)
                mart_list_15 = round(sum(carrier[59:90]),2)
                nisan_list_15 = round(sum(carrier[90:120]),2)
                mayıs_list_15 = round(sum(carrier[120:151]),2)
                haziran_list_15 = round(sum(carrier[151:181]),2)
                temmuz_list_15 = round(sum(carrier[181:212]),2)
                agustos_list_15 = round(sum(carrier[212:243]),2)
                eylul_list_15 = round(sum(carrier[243:273]),2)
                ekim_list_15 = round(sum(carrier[273:304]),2)
                kasım_list_15 = round(sum(carrier[304:334]),2)
                aralık_list_15 = round(sum(carrier[334:365]),2)
                ocak_list_16 = round(sum(carrier[365:365+31]),2)
                subat_list_16 = round(sum(carrier[365+31:365+59]),2)
                mart_list_16 = round(sum(carrier[365+59:365+90]),2)
                nisan_list_16 = round(sum(carrier[365+90:365+120]),2)
                mayıs_list_16 = round(sum(carrier[365+120:365+151]),2)
                haziran_list_16 = round(sum(carrier[365+151:365+181]),2)
                temmuz_list_16 = round(sum(carrier[365+181:365+212]),2)
                agustos_list_16 = round(sum(carrier[365+212:365+243]),2)
                eylul_list_16 = round(sum(carrier[365+243:365+273]),2)
                ekim_list_16 = round(sum(carrier[365+273:365+304]),2)
                kasım_list_16 = round(sum(carrier[365+304:365+334]),2)
                aralık_list_16 = round(sum(carrier[365+334:365+365]),2)
                ocak_list_17 = round(sum(carrier[365*2:365*2+31]),2)
                subat_list_17 = round(sum(carrier[365*2+31:365*2+59]),2)
                mart_list_17 = round(sum(carrier[365*2+59:365*2+90]),2)
                nisan_list_17 = round(sum(carrier[365*2+90:365*2+120]),2)
                mayıs_list_17 = round(sum(carrier[365*2+120:365*2+151]),2)
                haziran_list_17 = round(sum(carrier[365*2+151:365*2+181]),2)
                temmuz_list_17 = round(sum(carrier[365*2+181:365*2+212]),2)
                agustos_list_17 = round(sum(carrier[365*2+212:365*2+243]),2)
                eylul_list_17 = round(sum(carrier[365*2+243:365*2+273]),2)
                ekim_list_17 = round(sum(carrier[365*2+273:365*2+304]),2)
                kasım_list_17 = round(sum(carrier[365*2+304:365*2+334]),2)
                aralık_list_17 = round(sum(carrier[365*2+334:365*2+365]),2)
                df_out_edit.loc[c] = [df_out['ADRES'][i] ,ocak_list_15,'OCAK 2015']
                df_out_edit.loc[c+1] = [df_out['ADRES'][i] ,subat_list_15,'SUBAT 2015']
                df_out_edit.loc[c+2] = [df_out['ADRES'][i] ,mart_list_15,'MART 2015']
                df_out_edit.loc[c+3] = [df_out['ADRES'][i] ,nisan_list_15,'NISAN 2015']
                df_out_edit.loc[c+4] = [df_out['ADRES'][i] ,mayıs_list_15,'MAYIS 2015']
                df_out_edit.loc[c+5] = [df_out['ADRES'][i] ,haziran_list_15,'HAZIRAN 2015']
                df_out_edit.loc[c+6] = [df_out['ADRES'][i] ,temmuz_list_15,'TEMMUZ 2015']
                df_out_edit.loc[c+7] = [df_out['ADRES'][i] ,agustos_list_15,'AGUSTOS 2015']
                df_out_edit.loc[c+8] = [df_out['ADRES'][i] ,eylul_list_15,'EYLUL 2015']
                df_out_edit.loc[c+9] = [df_out['ADRES'][i] ,ekim_list_15,'EKIM 2015']
                df_out_edit.loc[c+10] = [df_out['ADRES'][i] ,kasım_list_15,'KASIM 2015']
                df_out_edit.loc[c+11] = [df_out['ADRES'][i] ,aralık_list_15,'ARALIK 2015']
                df_out_edit.loc[c+12] = [df_out['ADRES'][i] ,ocak_list_16,'OCAK 2016']
                df_out_edit.loc[c+13] = [df_out['ADRES'][i] ,subat_list_16,'SUBAT 2016']
                df_out_edit.loc[c+14] = [df_out['ADRES'][i] ,mart_list_16,'MART 2016']
                df_out_edit.loc[c+15] = [df_out['ADRES'][i] ,nisan_list_16,'NISAN 2016']
                df_out_edit.loc[c+16] = [df_out['ADRES'][i] ,mayıs_list_16,'MAYIS 2016']
                df_out_edit.loc[c+17] = [df_out['ADRES'][i] ,haziran_list_16,'HAZIRAN 2016']
                df_out_edit.loc[c+18] = [df_out['ADRES'][i] ,temmuz_list_16,'TEMMUZ 2016']
                df_out_edit.loc[c+19] = [df_out['ADRES'][i] ,agustos_list_16,'AGUSTOS 2016']
                df_out_edit.loc[c+20] = [df_out['ADRES'][i] ,eylul_list_16,'EYLUL 2016']
                df_out_edit.loc[c+21] = [df_out['ADRES'][i] ,ekim_list_16,'EKIM 2016']
                df_out_edit.loc[c+22] = [df_out['ADRES'][i] ,kasım_list_16,'KASIM 2016']
                df_out_edit.loc[c+23] = [df_out['ADRES'][i] ,aralık_list_16,'ARALIK 2016']
                df_out_edit.loc[c+24] = [df_out['ADRES'][i] ,ocak_list_17,'OCAK 2017']
                df_out_edit.loc[c+25] = [df_out['ADRES'][i] ,subat_list_17,'SUBAT 2017']
                df_out_edit.loc[c+26] = [df_out['ADRES'][i] ,mart_list_17,'MART 2017']
                df_out_edit.loc[c+27] = [df_out['ADRES'][i] ,nisan_list_17,'NISAN 2017']
                df_out_edit.loc[c+28] = [df_out['ADRES'][i] ,mayıs_list_17,'MAYIS 2017']
                df_out_edit.loc[c+29] = [df_out['ADRES'][i] ,haziran_list_17,'HAZIRAN 2017']
                df_out_edit.loc[c+30] = [df_out['ADRES'][i] ,temmuz_list_17,'TEMMUZ 2017']
                df_out_edit.loc[c+31] = [df_out['ADRES'][i] ,agustos_list_17,'AGUSTOS 2017']
                df_out_edit.loc[c+32] = [df_out['ADRES'][i] ,eylul_list_17,'EYLUL 2017']
                df_out_edit.loc[c+33] = [df_out['ADRES'][i] ,ekim_list_17,'EKIM 2017']
                df_out_edit.loc[c+34] = [df_out['ADRES'][i] ,kasım_list_17,'KASIM 2017']
                df_out_edit.loc[c+35] = [df_out['ADRES'][i] ,aralık_list_17,'ARALIK 2017']
                c = c + 12*3
                counter = 0
                carrier = []
            else:
                for a in range(counter):
                    row = {'ADRES':df_out['ADRES'][i-a] ,'SONOKUTAR':df_out['SONOKUTAR'][i-a],'ORTALAMA':df_out['ORTALAMA'][i-a],'Aktif Tüketim':df_out['AKTIFTUK'][i-a]}
                    df_carrier = pd.DataFrame(data=row,index = ['0'])
                    df_sorunlu =df_sorunlu.append(df_carrier)
                df_out_sorunlu=df_out_sorunlu.append(df_sorunlu)
                counter = 0
                df_sorunlu=pd.DataFrame(columns=columns)
                print(len(carrier))
                carrier=[]
        bar.update(i+1)
    bar.finish()
    return df_out_edit
def kaski_normalizer(input_df):
    input_df['FATURA_ODENEN_TUTAR'] = [round(x,2) for x in input_df['FATURA_ODENEN_TUTAR']]
    input_df.to_csv('denemever3.txt',index=False,encoding='utf-16')
    ready2normalize=pd.read_csv(r'C:\Users\nailt\Downloads\v1\v1\ready2normalizer.csv',sep=';',encoding='utf-8')
    c = 0
    columns = ready2normalize.columns
    df_sorunlu = pd.DataFrame(columns=columns)
    ready2normalize_sorunlu = pd.DataFrame(columns=columns)
    ready2normalize['ADRES'][2]
    carrier = []
    counter = 0
    FIRST_DAY = '01.01.2015'
    LAST_DAY = '31.12.2017'
    THRESHOLD = 20
    columns
    outcolumns=['ABONE_TIP_ACIKLAMA','ADRES','FATURA_ODENEN_TUTAR','DONEM']
    ready2normalize_edit=pd.DataFrame(columns = outcolumns)
    # %%
    bar = progressbar.ProgressBar(maxval=len(ready2normalize), \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for i in range(1,len(ready2normalize)-1):
        if ready2normalize['ADRES'][i]==ready2normalize['ADRES'][i+1] and ready2normalize['ADRES'][i-1]!=ready2normalize['ADRES'][i]:
            diff = difference(ready2normalize['OKUMA_TARIHI'][i],FIRST_DAY)
            for a in range(diff):
                carrier.append(ready2normalize['FATURA_ODENEN_TUTAR'][i]/diff)
            counter = counter + 1
        #yılın ara tarihleri
        if ready2normalize['ADRES'][i]==ready2normalize['ADRES'][i+1] and ready2normalize['ADRES'][i]==ready2normalize['ADRES'][i-1]:
            diff = difference(ready2normalize['OKUMA_TARIHI'][i],ready2normalize['OKUMA_TARIHI'][i-1])
            for a in range(diff):
                carrier.append(ready2normalize['FATURA_ODENEN_TUTAR'][i]/diff)
            counter = counter + 1
        #yılın son ayı
        if ready2normalize['ADRES'][i-1]==ready2normalize['ADRES'][i] and ready2normalize['ADRES'][i] != ready2normalize['ADRES'][i+1]:
            diff=difference(LAST_DAY,ready2normalize['OKUMA_TARIHI'][i])
            for a in range(diff):
                carrier.append(ready2normalize['FATURA_ODENEN_TUTAR'][i]/diff)
            diff=difference(ready2normalize['OKUMA_TARIHI'][i],ready2normalize['OKUMA_TARIHI'][i-1])
            for b in range(diff):
                carrier.append(ready2normalize['FATURA_ODENEN_TUTAR'][i]/diff)
            counter = counter + 1
            if len(carrier)==365*3:
                ocak_list_15 = round(sum(carrier[:31]),2)
                subat_list_15 = round(sum(carrier[31:59]),2)
                mart_list_15 = round(sum(carrier[59:90]),2)
                nisan_list_15 = round(sum(carrier[90:120]),2)
                mayıs_list_15 = round(sum(carrier[120:151]),2)
                haziran_list_15 = round(sum(carrier[151:181]),2)
                temmuz_list_15 = round(sum(carrier[181:212]),2)
                agustos_list_15 = round(sum(carrier[212:243]),2)
                eylul_list_15 = round(sum(carrier[243:273]),2)
                ekim_list_15 = round(sum(carrier[273:304]),2)
                kasım_list_15 = round(sum(carrier[304:334]),2)
                aralık_list_15 = round(sum(carrier[334:365]),2)
                ocak_list_16 = round(sum(carrier[365:365+31]),2)
                subat_list_16 = round(sum(carrier[365+31:365+59]),2)
                mart_list_16 = round(sum(carrier[365+59:365+90]),2)
                nisan_list_16 = round(sum(carrier[365+90:365+120]),2)
                mayıs_list_16 = round(sum(carrier[365+120:365+151]),2)
                haziran_list_16 = round(sum(carrier[365+151:365+181]),2)
                temmuz_list_16 = round(sum(carrier[365+181:365+212]),2)
                agustos_list_16 = round(sum(carrier[365+212:365+243]),2)
                eylul_list_16 = round(sum(carrier[365+243:365+273]),2)
                ekim_list_16 = round(sum(carrier[365+273:365+304]),2)
                kasım_list_16 = round(sum(carrier[365+304:365+334]),2)
                aralık_list_16 = round(sum(carrier[365+334:365+365]),2)
                ocak_list_17 = round(sum(carrier[365*2:365*2+31]),2)
                subat_list_17 = round(sum(carrier[365*2+31:365*2+59]),2)
                mart_list_17 = round(sum(carrier[365*2+59:365*2+90]),2)
                nisan_list_17 = round(sum(carrier[365*2+90:365*2+120]),2)
                mayıs_list_17 = round(sum(carrier[365*2+120:365*2+151]),2)
                haziran_list_17 = round(sum(carrier[365*2+151:365*2+181]),2)
                temmuz_list_17 = round(sum(carrier[365*2+181:365*2+212]),2)
                agustos_list_17 = round(sum(carrier[365*2+212:365*2+243]),2)
                eylul_list_17 = round(sum(carrier[365*2+243:365*2+273]),2)
                ekim_list_17 = round(sum(carrier[365*2+273:365*2+304]),2)
                kasım_list_17 = round(sum(carrier[365*2+304:365*2+334]),2)
                aralık_list_17 = round(sum(carrier[365*2+334:365*2+365]),2)
                ready2normalize_edit.loc[c] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,ocak_list_15,'OCAK 2015']
                ready2normalize_edit.loc[c+1] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,subat_list_15,'SUBAT 2015']
                ready2normalize_edit.loc[c+2] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,mart_list_15,'MART 2015']
                ready2normalize_edit.loc[c+3] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,nisan_list_15,'NISAN 2015']
                ready2normalize_edit.loc[c+4] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,mayıs_list_15,'MAYIS 2015']
                ready2normalize_edit.loc[c+5] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,haziran_list_15,'HAZIRAN 2015']
                ready2normalize_edit.loc[c+6] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,temmuz_list_15,'TEMMUZ 2015']
                ready2normalize_edit.loc[c+7] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,agustos_list_15,'AGUSTOS 2015']
                ready2normalize_edit.loc[c+8] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,eylul_list_15,'EYLUL 2015']
                ready2normalize_edit.loc[c+9] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,ekim_list_15,'EKIM 2015']
                ready2normalize_edit.loc[c+10] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,kasım_list_15,'KASIM 2015']
                ready2normalize_edit.loc[c+11] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,aralık_list_15,'ARALIK 2015']
                ready2normalize_edit.loc[c+12] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,ocak_list_16,'OCAK 2016']
                ready2normalize_edit.loc[c+13] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,subat_list_16,'SUBAT 2016']
                ready2normalize_edit.loc[c+14] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,mart_list_16,'MART 2016']
                ready2normalize_edit.loc[c+15] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,nisan_list_16,'NISAN 2016']
                ready2normalize_edit.loc[c+16] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,mayıs_list_16,'MAYIS 2016']
                ready2normalize_edit.loc[c+17] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,haziran_list_16,'HAZIRAN 2016']
                ready2normalize_edit.loc[c+18] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,temmuz_list_16,'TEMMUZ 2016']
                ready2normalize_edit.loc[c+19] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,agustos_list_16,'AGUSTOS 2016']
                ready2normalize_edit.loc[c+20] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,eylul_list_16,'EYLUL 2016']
                ready2normalize_edit.loc[c+21] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,ekim_list_16,'EKIM 2016']
                ready2normalize_edit.loc[c+22] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,kasım_list_16,'KASIM 2016']
                ready2normalize_edit.loc[c+23] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,aralık_list_16,'ARALIK 2016']
                ready2normalize_edit.loc[c+24] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,ocak_list_17,'OCAK 2017']
                ready2normalize_edit.loc[c+25] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,subat_list_17,'SUBAT 2017']
                ready2normalize_edit.loc[c+26] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,mart_list_17,'MART 2017']
                ready2normalize_edit.loc[c+27] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,nisan_list_17,'NISAN 2017']
                ready2normalize_edit.loc[c+28] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,mayıs_list_17,'MAYIS 2017']
                ready2normalize_edit.loc[c+29] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,haziran_list_17,'HAZIRAN 2017']
                ready2normalize_edit.loc[c+30] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,temmuz_list_17,'TEMMUZ 2017']
                ready2normalize_edit.loc[c+31] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,agustos_list_17,'AGUSTOS 2017']
                ready2normalize_edit.loc[c+32] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,eylul_list_17,'EYLUL 2017']
                ready2normalize_edit.loc[c+33] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,ekim_list_17,'EKIM 2017']
                ready2normalize_edit.loc[c+34] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,kasım_list_17,'KASIM 2017']
                ready2normalize_edit.loc[c+35] = [ready2normalize['ABONE_TIP_ACIKLAMA'][i] ,ready2normalize['ADRES'][i] ,aralık_list_17,'ARALIK 2017']
                c = c + 12*3
                counter = 0
                carrier = []
            else:
                for a in range(counter):
                    row = {'ABONE_TIP_ACIKLAMA':ready2normalize['ABONE_TIP_ACIKLAMA'][i-a],'ADRES':ready2normalize['ADRES'][i-a] ,'OKUMA_TARIHI':ready2normalize['OKUMA_TARIHI'][i-a],'FATURA_ODENEN_TUTAR':ready2normalize['FATURA_ODENEN_TUTAR'][i-a]}
                    df_carrier = pd.DataFrame(data=row,index = ['0'])
                    df_sorunlu =df_sorunlu.append(df_carrier)
                ready2normalize_sorunlu=ready2normalize_sorunlu.append(df_sorunlu)
                counter = 0
                df_sorunlu=pd.DataFrame(columns=columns)
                carrier=[]
        bar.update(i+1)
    bar.finish()
    return ready2normalize_edit
