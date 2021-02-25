from machine import Pin
import time

ans = (1,2,3)
b = 0
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
def botton_count():
    
    botton_count_num = 1

    if botton['button2'].value() == 1:  #botton['button1'].value():
        b+=1
        print('if成立 輸出框:'    )
        
        print('booton1:',botton['button1'].value())
        print('input_num現在',
              input_num['first_num'],
              input_num['second_num'],
              input_num['third_num'])
        print(input_num['first_num'])
 
        print('-------',b,'-------\n')
        time.sleep(0.2)
        print ('botton return值:','\n')



while True:
    print(input_num['first_num'])
    print("進入while True:")
    #print('botton_count() return值:',botton_count(),'\n')
    time.sleep(0.2)
    

