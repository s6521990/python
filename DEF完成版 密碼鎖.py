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

def do_count(ans_list = [],ans=[1,1,1,1],):

    def count_input(word = 'Your Input:\n',if_input=[],button_num = [1,2,3,4,5,6,7],bottons = [button1,button2,button3,button4,button5,button6,button7]):
        
        while True:
            i=0        
            for i in range(len(bottons)):           
                if bottons[i].value() == 1:
                    
                    redled.value(1)
                    time.sleep(0.2)
                    redled.value(0)
                    time.sleep(0.2)
                    
                    if_input[len(if_input):] += [button_num[i]]
                    print(word,if_input)
                    return if_input
                
        return count_input
    
    for ii in range(4):
        print('Number',ii+1,'Value')
        ans_list = count_input()
    if ans_list == ans:
        print('\nThanks for watch')
        greenled.duty(1024)
        time.sleep(2)
        greenled.duty(0)
        
    else:
        print('\nERROR,Please try again later')      
    return do_count

redled.value(0)
greenled.duty(0)
do_count()