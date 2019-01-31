#!/usr/bin/env python3
import sys
import csv
from collections import namedtuple
import getopt
#1.class Arg > shuru: -c test.cfg -d user.csv -o gongzi.csv
#               shuchu:path configfile,userdatafile,outputfile
#2. class Config > shuchu:{} config
#3.class UserData >shuchu:{} id,income
#week4.class Cal > shuru: income
#              shuchu:101,3500,577.50,0.00,2922.50
#week4.output > outputfile path



INCOME_TAX_START_POINT = 3500

IncomTaxLookupItem = namedtuple('IncomTaxLookupItem',['start_point','tax_rate','minus'])

INCOME_TAX_NUM_TABLE = [
    IncomTaxLookupItem(80000, 0.45, 13505),
    IncomTaxLookupItem(55000, 0.35, 5505),
    IncomTaxLookupItem(35000, 0.3, 2755),
    IncomTaxLookupItem(9000, 0.25, 1005),
    IncomTaxLookupItem(4500, 0.2, 555),
    IncomTaxLookupItem(1500, 0.1, 105),
    IncomTaxLookupItem(1500, 0.3, 0)
]



class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def _value_after_option(self,option):
        try:
            index = self.args.index(option)
            return self.args[index+1]
        except:
            print('Args Error')
    @property
    def config_path(self):
        return self._value_after_option('-c')

    @property
    def userdata_path(self):
        return self._value_after_option('-d')

    @property
    def output_path(self):
        return self._value_after_option('-o')

args = Args()

class Config(object):
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {}
        with open(args.config_path,'r') as f:
            for line in f.readlines():
                key,value = line.strip().split('=')
                try:
                    config[key.strip()] = float(value.strip())
                except:
                    print('Parameter Error')
                    exit()
        return config

    def _get_config(self,key):
        try:
            return self.config[key]
        except:
            print('Config Error')
            exit()

    @property
    def social_insurance_base_low(self):
        return self._get_config('JiShuL')

    @property
    def social_insurance_base_high(self):
        return self._get_config('JiShuH')

    @property
    def social_insurance_rate_total(self):
        return sum([
            self._get_config('YangLao'),
            self._get_config('YiLiao'),
            self._get_config('ShiYe'),
            self._get_config('GongShang'),
            self._get_config('ShengYu'),
            self._get_config('GongJiJin')

        ])


config = Config()

class UserData(object):
    def __init__(self):
        self.userdata = self._read_users_data

    @property
    def _read_users_data(self):
        userdata = []
        with open(args.userdata_path,'r') as f:
            for line in f.readlines():
                employ_id, income_string = line.strip().split(',')
                try:
                    income = int(income_string)
                except:
                    print('Parameter Error')
                    exit()
                userdata.append((employ_id,income))
        return userdata

    def __iter__(self):
        """
        实现__iter__魔法方法，使UserData 对象成为可迭代对象

        """
        return iter(self.userdata)
#userdata = UserData()
#userdata = userdata.userdata

class IncomeTaxCalculator(object):

    def __init__(self,userdata):
    #初始化时接收一个UserData对象
        self.userdata = userdata


    @staticmethod
    def calc_social_insurance_money(income):
        #计算保险
        if income <= config.social_insurance_base_low:
            return config.social_insurance_base_low * config.social_insurance_rate_total
        elif config.social_insurance_base_low < income < config.social_insurance_base_high:
            return income * config.social_insurance_rate_total
        else:
            return config.social_insurance_base_high * config.social_insurance_rate_total

    @classmethod
    def calc_income_tax_and_remain(cls,income):
        #计算税后工资
        social_insurance_money = cls.calc_social_insurance_money(income)
        real_income = income - social_insurance_money
        tax_part = income - real_income - INCOME_TAX_START_POINT

        for item in INCOME_TAX_NUM_TABLE:
            if tax_part >= item.start_point:
                tax = tax_part * item.tax_rate - item.minus
                return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)

        return '0.00', '{:.2f}'.format(real_income)

    def cal_for_all_userdata(self):

        result = []
        for employ_id,income in self.userdata:
            social_insurance_money = '{:.2f}'.format(self.calc_social_insurance_money(income))
            tax,remain = self.calc_income_tax_and_remain(income)

            result.append([employ_id,income,social_insurance_money,tax,remain])

        return result

    def export(self):
        result = self.cal_for_all_userdata()
        with open(args.output_path,'w',newline = '') as f:
            writer = csv.writer(f)
            writer.writerows(result)

if __name__ == '__main__':
    calculator = IncomeTaxCalculator(UserData())
    calculator.export()












