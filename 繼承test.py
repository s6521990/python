class bt:
    def __init__(self,bt_list):
        self.bt_list = bt_list
        print ('我是按鈕',self.bt_list)
        
    def get_bt_list(self):
        print('bt')
        return '123'

        
    def set_bt_list(self,value):
        '''請給一個list'''
        self.bt_list = value
        print('你好')
        return self.bt_list

class ps(bt):
    def __init__(self,bt_list):
        super().__init__(bt_list)
        self.pslist = [1,1,1,1]
                                    #密碼預設 四個1 用list容器 
                                #button.value()預先存放在類別裡面因為是python
        self.input = []                     #為了方便測試程式碼在此把按鈕的value存放在容器模擬
        print('請輸入密碼 ')
        
    def get_list(self):
        super().get_bt_list()
        print('我是ps方法')    #get_list方法 顯示self.pslist這個預設名單(密碼)
                                           
    def set_list(self,value):              #set_list方法 設定參數修改類別的self.pslist                                              
        self.value = value
        value = []
        self.pslist = self.value            #把輸入的值(value)等於self.pslist
        print ('*設定* ',self.pslist)
b = 111
bb = bt(b)
bb.get_bt_list()
print('***************')
a = ps(b)
a.get_list()