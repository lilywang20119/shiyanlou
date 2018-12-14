#!/usr/bin/env python3
#-*-coding:utf-8 -*-
import sys

try:
    salary =int(sys.argv[1])
    #print(salary)
except:
    print("Parameter Error")
tax_total = salary -0 -3500
#print(tax_total)
if tax_total <= 1500:
    tax = tax_total*3/100 
elif 1500< tax_total <= 4500:
    tax = tax_total *10/100 -105
elif 4500< tax_total <= 9000:
    tax = tax_total *20/100 -555
elif 9000 < tax_total <= 35000:
    tax = tax_total *25/100 -1005
elif 35000 <tax_total <= 55000:
    tax = tax_total *30/100 -2755
elif 55000 < tax_total <= 80000:
    tax = tax_total * 35/100 -5505
else:
    tax = tax_total * 45% -13505

print("%.2f"% tax)
