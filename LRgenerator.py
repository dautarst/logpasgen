from email import header
import logging
import random
import csv
from itertools import zip_longest
from sqlite3 import Row
from numpy import row_stack
import pandas as pd


chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('количество пар логин\пароль')
lengthlogin = input('длина логина?')
lengthpass = input('длина пароля?')

number = int(number)
lengthlogin = int(lengthlogin)
lengthpass = int(lengthpass)
login = []
for n in range(number):
    log =''
    for i in range(lengthlogin):
        log += random.choice(chars)
    login.append(log);
print(login);
password=[]
for n in range(number):
    pas =''
    for i in range(lengthpass):
        pas += random.choice(chars)
    password.append(pas);
print(password);
lppair=[login,password];
print(lppair)
export_data = zip(login,password)
result = list(export_data)
print(result)
export_csv = pd.DataFrame(result)
export_csv.to_csv('users.csv', index = False, sep=',')

with open('users.csv', 'r') as f:
    lines = f.readlines()
with open('users.csv', 'w') as f:
    f.writelines(lines[1:])
