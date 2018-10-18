from builtins import int
import pandas as pd
from datetime import datetime
import openpyxl
from difflib import SequenceMatcher
import progressbar
def excel_time_2_string(excel_time):
    t = pd.to_datetime('1899-12-30') + pd.to_timedelta(excel_time,'D')
    return t.strftime('%d.%m.%Y')

def excel_time_2_ay(excel_time):
    '''
    converts excel float format to pandas datetime object
    then converts to month as integer
    '''
    t = pd.to_datetime('1899-12-30') + pd.to_timedelta(excel_time,'D')
    return t.strftime('%m')

def excel_time_2_gun(excel_time):
    '''
    converts excel float format to pandas datetime object
    then converts to day as integer
    '''
    t = pd.to_datetime('1899-12-30') + pd.to_timedelta(excel_time,'D')
    return t.strftime('%d')

def str_to_day(day):
    dummy = datetime.strptime(day,'%d.%m.%Y')
    epoch_time = datetime.timestamp(dummy)
    day = epoch_time/(3600*24)
    return day

def difference(a,b):
    difference = str_to_day(a)-str_to_day(b)
    return int(difference)

def xlsx_2_df(path, first_row_header = True):
    wb = openpyxl.load_workbook(path)
    sheet_names = wb.get_sheet_names()
    for i in range (len(sheet_names)):
        carrier = sheet_names[i]
        sheet_ranges = wb[carrier]
        df_carrier = pd.DataFrame(sheet_ranges.values)
        if i == 0:
            df = pd.DataFrame(columns=df_carrier.iloc[0])
        df_carrier.columns = df_carrier.iloc[0]
        df_carrier = df_carrier.iloc[1:]
        df = df.append(df_carrier)
        return df
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
def list_2_csv(list_item,name):
    df = pd.DataFrame(list_item)
    df.to_csv(name,index = False,encoding='utf-16', header=None)
