def my_studio(**args):
    print('test')
    for k in args:
        print(k,':',args[k])
        
my_studio(名稱='pppp', 項目='aaaa')
print('********')
my_studio(ans='1234')