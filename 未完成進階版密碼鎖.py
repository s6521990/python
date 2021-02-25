from machine import Pin, PWM
import time

class word_machine:
    
    def __init__(self,site):
        self.site = site
        print("長度:",site)    
    @property
    def site(self):
        return self.__site

    
    @site.setter
    def site(self, value):
        if value < 4 :
            raise ValueError("長度至少為4")    
        self.__site = value

class ans_list:
    def __init__(self,ans):
        self.ans = ans
        print("密碼",ans)
    @property
    def ans(self):
        return self.__ans
    @ans.setter
    def ans(self, value):
        print(value)
        if value > 6:
            raise ValueError("字元過大")
        if value < 0:
            raise ValueError("字元過小")
        self.__ans = value
    def add_ans(self,ans_value):
        self.ans += value
        return ans
    

    
a = word_machine(4)
print('請輸入密碼')
b = ans_list(5)

print(b)


