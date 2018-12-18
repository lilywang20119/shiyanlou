#!/usr/bin/env python3
class UserData:
    def __init__(self,id,name):
        self.id = id
        self._name = name
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.id,self.name)
class NewUser(UserData):
    group = 'shiyanlou-louplus'
#    def get_name(self):
 #       return self.name
  #  def set_name(self,value):
   #

#self.name = value
    def __call__(self):
        print("{}'s id is {} ".format(self._name,self.id))

        #return self.format_userdata(id,name)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if len(value) >3:
            self._name = value
        else:
            print('ERROR')

    @classmethod
    def get_group(cls):
        return cls.group
    @staticmethod
    def format_userdata(id,name):
        return "{}'s id is {} ".format(name,id)
    



if __name__ == '__main__':
    #user1 = NewUser(101,'Jack')
    #user1.name = 'Lou'
    #user1.name = 'Jackie'
    user = NewUser(101,'Jack')
    user()

    #print(user.format_userdata)
    #user1.set_name('Jackie')
    #user2 = NewUser(102,'Louplus')
    #print(user1.name)
    #print(user2.name)
    #print(NewUser.get_group())
    #print(NewUser.format_userdata(109,'Lucy'))

