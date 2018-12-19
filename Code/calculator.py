#!/usr/bin/env python3
#-*-coding:utf-8-*-
import sys
import csv

class Args(object):
    def __init__(self):
        args1 = sys.argv[1:]

        try:
            self.configfile = args1[args1.index('-c')+1]
            #elif index = args.index('-d'):
            self.userdatafile =args1[args1.index('-d')+1]
            #else:
            self.outputfile = args1[args1.index('-o')+1]
        except ValueError:
            passs
#args = Args()

class Config(object):
    def __init__(self):
        self.config=self._read_config()

    def _read_config(self):
        config={'s':0}
        try:
            with open(args.configfile,'r') as f:
                for line in f.readlines():
                    m = line.split('=')
                    a,b = m[0].strip(),m[1].strip()
                    if a == 'JiShuL' or a=='JiShuH':
                        config[a] = float(b)
                    else:
                        config['s'] +=float(b)
        except ValueError:
            pass
        return config
#config = Config().config
#print(config)

class UserData(object):
    def __init__(self):
        self.userdata = self._read_users_data()

    def _read_users_data(self):
        userdata = []
        try:
            with open(args.userdatafile,'r') as f:
                userdata = [tuple(line) for line in csv.reader(f)]
        except ValueError:
            pass
        return userdata
#userdata = UserData().userdata
#print(userdata)


#class IncomTaxCalculator(object):
def calc_for_all_userdata(salary):
    salary = int(salary)
    shebao = salary*config['s']
    if salary < config['JiShuL']:
        shebao = config['JiShuL']*config['s']
    if salary > config['JiShuH']:
        shebao = config['JiShuH']*config['s']
    total_tax = salary - shebao-3500
    if total_tax <=0:
        tax = 0
    elif 0< total_tax <=1500:
        tax = total_tax*0.03
    elif 1500 <total_tax <=4500:
        tax = total_tax*0.1-105   
    elif 4500 <total_tax <=9000:
        tax = total_tax*0.2-555
    elif 9000<total_tax <=35000:
        tax = total_tax*0.25-1005        
    elif 35000<total_tax<=55000:
        tax = total_tax*0.3-2755        
    elif 55000<total_tax<=80000:
        tax = total_tax*0.35-5505        
    else:
        tax = total_tax*0.45-13505      
    money = salary-shebao-tax
        #return salary_shebao,tax,money
    result1=[]    
    result1=[salary,format(shebao,'.2f'),format(tax,'.2f'),format(money,'.2f')]
    return result1
    
if __name__ =='__main__':
args = Args()
    config = Config().config
    print(config)
    userdata = UserData().userdata
    print(userdata)
    with open(args.outputfile,'w') as f:
        for a,b in userdata:
            result = calc_for_all_userdata(b)
            result.insert(0,a)
            print(result)

            writer = csv.writer(f)
            writer.writerow(result)

  
