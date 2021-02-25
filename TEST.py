from machine import Pin
import time

ans = (1,2,3)
input_num={'first_num':0,
           'second_num':0,
           'third_num':0}

botton = {'button1':Pin(16,Pin.IN),
          'button2':Pin(14,Pin.IN),
          'button3':Pin(12,Pin.IN),
          'button4':Pin(13,Pin.IN),
          'button5':Pin(15,Pin.IN),
          'button6':Pin(5,Pin.IN),
          'button7':Pin(4,Pin.IN)
          }

def first_side():

    if botton['button1'].value() == 1:
        print('first_side 1 ')
        input_num['first_num'] = 1
        return 'fs'
        
    elif botton['button2'].value() == 1:
        print('first_side 2 ')
        input_num['first_num'] = 2
        return 'fs'

                
def second_side():

    if botton['button1'].value() == 1:
        print('second_side 1 ')
        input_num['second_num'] = 1
        return 'ss'
    elif botton['button2'].value() == 1:
        print('second_side 2 ')
        input_num['second_num'] = 2
        return 'ss'
    
def third_side():

    if botton['button1'].value() == 1:
        print('third_side 1 ')
        input_num['third_num'] = 1
        return 'ts'
    elif botton['button2'].value() == 1:
        print('third_side 2 ')
        input_num['third_num'] = 2
        return 'ts'
    
        
def end_ans():
    if ans == input_num :
        print('答對')
    elif ans != input_num:
        print('答錯')
        input_num={'first_num':0,'second_num':0,'third_num':0}
    
def input_count():
    print('進入input_count')
    while True :
        time.sleep(1)
        print('aaa')
        if input_num['first_num'] == 0:
            print('請輸入first_num')
            first_side()
            time.sleep(0.2)
            
           
        if first_side() == 'fs':
            print('請輸入second_num')
            second_side()
            time.sleep(0.2)
            
        if second_side() == 'ss':
            print('請輸入third_num')
            third_side()
            time.sleep(0.2)
            
        if input_num['third_num'] != 0: #end_ans()
            if ans == input_num:
                print('fnish')
                break
            else:
                print('wrong')
                break
print(ans)
while (ans) == (input_num):
    input_count()

print(input_num)
print('恭喜破關')
time.sleep(1)