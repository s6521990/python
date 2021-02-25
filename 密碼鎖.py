from machine import Pin, PWM
import time

ans = [1,2,3,4]
redled = Pin(0,Pin.OUT)
greenled = PWM(Pin(2, Pin.OUT))
button1 = Pin(16,Pin.IN)
button2 = Pin(14,Pin.IN)
button3 = Pin(12,Pin.IN)
button4 = Pin(13,Pin.IN)
button5 = Pin(15,Pin.IN)
button6 = Pin(5,Pin.IN)
button7 = Pin(4,Pin.IN)
bottons = [button1,button2,button3,button4,button5,button6,button7]
button_num = [1,2,3,4,5,6,7]
input_num = []
redled.value(0)
greenled.duty(0)
print("歡迎主人回家\n請輸入密碼:(提示:三個字)\n1~6輸入鍵 7刪除鍵\n")
# 15 13 12 14 16 2 0 4 5
#b = b[ (b[0] : b[0]+1)] = 1
def in_bt(input_num):
    a = (input_num[len(input_num):] + [button_num[0]])
    return a


#     input_num[len(input_num):] = [button_num[i]]
def bt():
        print( '\n--------------\n現在輸入值:\n',input_num)        
        print('答案ans:\n',ans)
        redled.value(1)
        time.sleep(0.2)
        redled.value(0)
        time.sleep(0.2)

print(in_bt(input_num))

while True:
    i = 0
    for i in range(len(bottons)):
        
        if bottons[i].value() == 1:     
            input_num[len(input_num):] = [button_num[i]]
            bt()
            
        if bottons[6].value() == 1:
            print('len(input_num):',len(input_num))
            del input_num[len(input_num)-1:len(input_num)]
            print("刪除",input_num)        
            bt()
    
    if len(input_num) > len(ans):
       
        del input_num[len(input_num)-1:]
        print("輸入值溢出")
        time.sleep(0.5)

    if input_num == ans :
        print("已解鎖")
        redled.value(0)
        greenled.duty(0)
        for ii in range(0,1024,8):
            time.sleep(0.02)
            greenled.duty(ii)
            for ii in range(1024,-1,-8):
                time.sleep(0.02)
                greenled.duty(ii)
            break
        break

