
favorites='arukuma' 
def scope_test():

    favorites='palkuma' #関数内で定義した変数
    
    def do_local():
        favorites='coffee:local'
    
    
    def do_nonlocal():
        nonlocal favorites
        favorites='chrome'
    
    def do_global():
        global favorites
        favorites='nozomi'
    


    #do_local() #   favorites(ローカル変数)の上書き
    do_nonlocal()#  favorites(ノンローカル変数)の上書き
    #do_global()#   favorites(グローバル変数)の上書き

scope_test()



#変数の確認
print(favorites)