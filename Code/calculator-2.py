#!/usr/bin/env python3
import sys

salary_dict = {}
for arg in sys.argv[1:]:
    try:
        salary_dict[arg.split(':')[0]] = int(arg.split(':')[1])
#        print(salary_dict)
    except:
        print("Parameter Error")
def f1(salary):
    total_tax = salary*(1-0.165)-3500
    if 0<total_tax <=1500:
        rate = 0.03
        minus = 0
    elif total_tax <= 0:
        rate = 0
        minus = 0
    elif 1500 <total_tax <=4500:
        rate = 0.1
        minus = 105
    elif 4500 <total_tax <=9000:
        rate = 0.2
        minus = 555
    elif 9000<total_tax <=35000:
        rate = 0.25
        minus = 1005
    elif 35000<total_tax<=55000:
        rate = 0.3
        minus = 2755
    elif 55000<total_tax<=80000:
        rate = 0.35
        minus = 5505
    else:
        rate = 0.45
        minus = 13505
    tax = total_tax * rate - minus
    money = salary *(1-0.165)-tax
    return("%.2f"%money)

if __name__ =='__main__':
    for arg in sys.argv[1:]:
        try:
            salary_dict[arg.split(':')[0]] = int(arg.split(':')[1])
            
        except:
            print("Parameter Error")
    #for key,value in salary_dict.items():
        print("{}:{}".format(arg.split(':')[0],f1(salary_dict[arg.split(':')[0]])))

