class bt:
    def __init__(self,bt_list):
        self.bt_list = bt_list
        return self.bt_list
        
    def get_bt_list(self):
        print ('-------我是按鈕--------\n',self.bt_list,'\n')
        return self.bt_list
        
    def set_bt_list(self,value):
        '''請給一個list'''
        self.bt_list = value
        print('-------按鈕設定--------\n',self.bt_list,'\n')
        return self.bt_list
        
class ps(bt):
    """value is list
    """
    def __init__(self,bt_list):
        self.bottons = super().__init__(bt_list)    #button.value()預先存放在類別裡面因為是python
        self.pslist = [1,1,1,1]             #密碼預設 四個1 用list容器      
        self.input = []                     #為了方便測試程式碼在此把按鈕的value存放在容器模擬
        print('系統啟動,請輸入密碼 ')
        print('預設密碼:',self.pslist)
        print('-------我是按鈕--------\n',self.bottons,'\n')

    def get_list(self):
        print ('-------密碼是--------\n',self.pslist,'\n')    #get_list方法 顯示self.pslist這個預設名單(密碼)
                                           
    def set_list(self,value):              #set_list方法 設定參數修改類別的self.pslist                                              
        self.value = value
        self.pslist = self.value            #把輸入的值(value)等於self.pslist
        print ('-------密碼設定--------\n',self.pslist,'\n')
    
    def selet_1_enter(self,value):      #selet_1_enter方法 每一次如果有值要輸入(1或0),bt_num(值)
        #value = super().get_bt_list()
        self.ps_bottons = value         #會取代 類別bt的self.input屬性,每一次取代一個值     
        for i in range(len(self.bottons)):           
            if self.ps_bottons[i] == 1:
                self.input[len(self.input):] += [self.bottons[i]]
                print(self.input,)
                return self.input
        
#情境(本來想打esp8266但是比較想摸按鈕面板直接程式控制= =)
#有一個機器，螢幕顯示器最多可以有四個數字(pslist)
#功能1 按下確認鍵(selet_1_enter)比對此機器名單(a.pslist)上的數字是否跟輸入的按鈕數字相符
      #符合顯示Thanks for test
      #錯誤顯示ERROR,Please try again later
#-----------主程式---------------------------------------------------------------
b_list = [1,2,3,4,5,6]      #按鈕值總4個
ans_list = [1,1,1]      #使用者設定密碼 #使用方法selet_1_enter輸出結果必須符合ans_list(使者自設)
#注意 (docs我不會打><)(白話解釋) #根據使用者所設定按鈕的值,在下面程式碼模擬高低電位時應做調整輸出才會符合預期
                            #因為ps類別的方法selet_1_enter會len(selet_1_enter)
bt_highlow1 = [1,0,0,0,0,0]     #模擬第一個位置接收的按鈕值
bt_highlow2 = [1,0,0,0,0,0]     #第二次第二個位置
bt_highlow3 = [1,0,0,0,0,0]     #第三次第三個位置

psmachine = ps(b_list)            #psmachine是物件 ps 類別
psmachine.set_list(ans_list)    #psmachine是物件 使用set_list方法設定密碼list
psmachine.set_bt_list(b_list)#psmachine是物件 使用繼承的bt類別的set_bt_num_list方法設定按鈕list

psmachine.selet_1_enter(bt_highlow1)    #第一次#因為再輸入密碼的狀況下
psmachine.selet_1_enter(bt_highlow2)    #第二次#是按下一個按鈕就顯示第一次按鈕值所以
psmachine.selet_1_enter(bt_highlow3)    #第三次#不需要for x in range(i)代替次數了(已結構化)
                                        #使用者設定幾位數密碼就使用幾次ps類別的selet_1_enter方法
if psmachine.input == ans_list:         #如果psmachine等於使用者設定的密碼ans_list
    print('\nThanks for test')      
else:
    print('\nERROR,Please try again later')
