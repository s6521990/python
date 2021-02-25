from machine import Pin, PWM
import time
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

redled.value(0)
greenled.duty(0)
ans_list = []
ans = [1,1,1,1]

def do_count(input_count=[],button_num = [1,2,3,4,5,6,7]):
    
    while True:
        i=0        
        for i in range(len(bottons)):           
            if bottons[i].value() == 1:               
                redled.value(1)
                time.sleep(0.2)
                redled.value(0)
                time.sleep(0.2)
                input_count[len(input_count):] += [button_num[i]]
                print(input_count)         
                return input_count

for a in range(4):
    print('請輸入第',a+1,'個數字')
    ans_list = do_count()
    time.sleep(0.3)

if ans_list == ans:
    print('\nENTER')
else:
    print('\nERROR')        