import numpy as np
import pandas as pd
from datetime import date

Goods_or_services=[]
Prices=[]
Dates=[]
Expense_Type=[]

def add_expense(goods,price,date,expense_type):
    Goods_or_services.append(goods)
    Prices.append(price)
    Dates.append(date)
    Expense_Type.append(expense_type)

option =-1
while(option !=0):
    print('Welcome to the Expense Tracker')
    print('1.Add Food Expense')
    print('2.Add Household Expense')
    print('3.Add Transportation Expense')
    print('4.show and save the  Expense Report')
    print('0.Exit')

    option=int(input('choose an option:\n'))

    print()

    if option ==0:
        print('Exiting the program')
        break
    elif option==1:
        print('Adding food')
        expense_type='FOOD'
    elif option==2:
        print('Adding Household')
        expense_type='HOUSEHOLD'
    elif option==3:
        print('Adding Transportation')
        expense_type='TRANPORTATION'
    elif option==4:
        expense_report =pd.DataFrame()
        expense_report['Goods_or_services']=Goods_or_services
        expense_report['Prices']=Prices
        expense_report['Dates']=Dates
        expense_report['Expense_Type']=Expense_Type

        expense_report.to_csv('D:\expenses.csv')
        print (expense_report)

    else:
        print('You chose an incorrect option.Please choose 0,1,2,3, or 4')

    if option==1 or option ==2 or option==3:
        goods=input('Enter the good or service for the expense type'+expense_type+'\n')
        price=float(input('Enter the price of the good or service:\n'))
        today =date.today()
        add_expense(goods,price,today,expense_type)
        print()

