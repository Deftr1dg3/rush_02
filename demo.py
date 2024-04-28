#!/usr/bin/env python3

with open("numbers.dict", "r") as f:
    data = f.read()
    
rows = [row.split(':') for row in data.split('\n')][:-1]

dct = {row[0].strip(): row[1].strip() for row in rows}
dct['-1'] = ""

def print_units(num):
    if num[2] != '0':
        print(f"{dct[num[2]]}", end="")

def print_tens(num: str):
    if num[1] == '0':
        print_units(num)
        print("", end=" ")
    if num[1] == '1':
        print(f"{dct[num[1:]]}", end="")
    else:
        print(f"{dct[num[1] + '0']}", end=" ")
        print_units(num)
   
def print_hundrests(num: str, order: str = "100"):
    print(f"{dct[num[0]]} {dct[order]}", end="")

def print_three(num: str):
    if num[0] != '0':
        print_hundrests(num)
        print("", end=" ")
    if num[1] != '0':
        print_tens(num)
        print("", end=" ")
    if num[1] == '0':
        print_units(num)
 
num = "1543234115"
def print_num(num: str, order: str = "100"):
    if not num:
        return False
    if order == "100":
        order += "0"
    else:
        order += "000"
    if order != "100" and print_num(num[:-3], order):
        print(f" {dct[order]}", end=" ")
    print_three(num[-3:])
    
    return True

def display_word_represenatation(num):
    if (len(num)) % 3 != 0:
        l = len(num) + 3 - len(num) % 3
        num = num.rjust(l, "0")
    print_num(num)  
  
display_word_represenatation(num)