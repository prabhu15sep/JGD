#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 21:19:53 2018

@author: Prabz
"""
import pandas as pd
import numpy as np

def to_file(pframe,fname,fileformat,str_trade_date,x_writer=np.nan):
    if(pd.notna(x_writer)):
        writer = x_writer
    elif(fileformat == "EXCEL"):
        writer = pd.ExcelWriter("Strat1_{}.xlsx".format(str_trade_date))
    if fileformat == "CSV":
        #pframe.dropna(how='all')
        pframe.to_csv("{}_{}.csv".format(fname,str_trade_date))
        writer = np.nan
        
    if fileformat == "EXCEL":
        pframe.to_excel(writer,fname)
        pframe.to_excel(writer,"here")
        writer.save()
    
    return writer   

def find_nlargest(input_list,size=3,n1=1,n2=1,n3=1):
    temp = input_list.copy()
    if sum(~np.isnan(x) for x in temp) < size:
        return np.NaN,np.NaN,np.NaN
    #test.sort()
    #desc_test = test[::-1]
    desc_list = np.sort(temp)[::-1]
    return  desc_list[n1 - 1],desc_list[n2 - 1],desc_list[n3 - 1]
    
def find_nlargest_avg(input_list,size=5,n1=1,n2=1,n3=1):
    temp = input_list.copy()
    if sum(~np.isnan(x) for x in temp) < size:
        return np.NaN
    desc_list = np.sort(temp)[::-1]
    return  (desc_list[n1 - 1] + desc_list[n2 - 1] + desc_list[n3 - 1])/3