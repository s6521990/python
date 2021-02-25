from machine import Pin
import time

class bt: #按鈕的class
    def __init__(self,botton):
        self.botton = botton
        return self.botton
        
    def get_botton(self):
        return self.botton
        
    def set_botton(self,value):
        self.botton = value
        return self.botton
    
class ps(bt): #密碼鎖的class
    def __init__(self,space,botton):
        self.botton_num = super().__init__(botton)                
        self.ps_list = space
        self.pin_botton = []
        self.ans = [1,1,1,1]   
        
    def get_ans(self):
        return self.ans
                                           
    def set_ans(self,value):                                                           
        self.ans = value
        return self.ans
       
    def change(self,pin_value):      
        self.pin_botton = pin_value         
        while True:
            for i in range(len(self.pin_botton)):           
                if self.pin_botton[i].value() == 1:
                    self.ps_list[len(self.ps_list):] += [self.botton_num[i]]
                    return self.ps_list
#主程式開始
#初始化參數
button1 = Pin(16,Pin.IN)
button2 = Pin(14,Pin.IN)
button3 = Pin(12,Pin.IN)
button4 = Pin(13,Pin.IN)
button5 = Pin(15,Pin.IN)
button6 = Pin(5,Pin.IN)
button7 = Pin(4,Pin.IN)
redled = Pin(0,Pin.OUT)
greenled = Pin(2,Pin.OUT)

redled.value(1)
greenled.value(1)
redled.value(0)
greenled.value(0)
#mc物件使用了class類別
#設定mc的屬性
mc_botton_pin = [button1,button2,button3,button4,button5,button6,button7]
mc_botton_num = [1,2,3,4,5,6]
mc_ans = [1,2,3,4]
mc_list = []

mc = ps(mc_list,mc_botton_num)
mc.ans = mc_ans

print('系統啟動,請輸入密碼\
        \n密碼',mc.ans)
for i in range(len(mc.ans)):
    print('輸入第',i+1,'位')
    print(mc.change(mc_botton_pin))
    redled.value(1)
    time.sleep(0.3)
    redled.value(0)
    
if mc_list == mc.ans:         
    print('\nThanks for test')
    greenled.value(1)
    time.sleep(1)
    greenled.value(0)
else:
    print('\nERROR,Please try again later')