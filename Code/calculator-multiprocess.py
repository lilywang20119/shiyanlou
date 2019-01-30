#!/usr/bin/env python3
#-*-coding:utf-8-*-
import sys
import csv
from multiprocessing import Process,Queue,Pool

class Args(object):
    def __init__(self):
        args1 = sys.argv[1:]
        self.configfile = args1[args1.index('-c')+1]
        self.userdatafile =args1[args1.index('-d')+1]
        self.outputfile = args1[args1.index('-o')+1]

#args = Args()
        
class Config(object):
    def __init__(self):
        self.config=self._read_config()

    def _read_config(self):
        config={'s':0}
        with open(args.configfile,'r') as f:
            for line in f.readlines():
                line=line.strip('\n')
                ss=line.split(' = ')
                a,b = ss[0],ss[1]
#                print(a,b)
                if a == 'JiShuL' or a=='JiShuH':
                    config[a] = float(b)
                else:
                    config['s'] +=float(b)
        
        return config
#config = Config().config
#print(config)

def f1(q1):   
    with open(args.userdatafile,'r') as f:
        data = [tuple(line) for line in csv.reader(f)]
    q1.put(data)


def f2(q1,q2):
    
    for a,b in q1.get():
        salary = int(b)
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
        newdata=[]    
        newdata1=[a,salary,format(shebao,'.2f'),format(tax,'.2f'),format(money,'.2f')]
        newdata.append(newdata1)
    
    q2.put(newdata)
""""    p=Pool(2)
    for i in range(1,3):
        p.apply_async(f4,args=(newdata1,))
        p.close()
        p.join()
"""

def f3(q2):
    with open(args.outputfile,'w') as f:
        for w in q2.get():
            writer = csv.writer(f)
            writer.writerow(w)
def f4(n):
    newdata2 = newdata.append(n)
    return newdata2

def main():
    Process(target=f1,args=(queue1,)).start()
    Process(target=f2,args=(queue1,queue2)).start()
    Process(target=f3,args=(queue2,)).start()

if __name__ =='__main__':
   queue1=Queue()
   queue2=Queue()
   args = Args()
   config=Config().config
   main()
   
