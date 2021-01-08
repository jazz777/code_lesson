def scope_test():
    
    
    def do_local():
        favorites='coffee_local'

    def do_nonlocal():
        nonlocal favorites
        favorites='chrome_nonlocal'
    
    def do_global():
        global favorites
        favorites='nozomi_global'

    favorites='arukuma' #関数内で定義した変数
    print('親関数のfavorite変数=',favorites)

    do_local() #   favorites(ローカル変数)の上書き
    print('親関数のfavorite変数=',favorites,'  子関数上でローカル変数をchrome_nonlocalに設定')
    
    do_nonlocal()#  favorites(ノンローカル変数)の上書き
    print('親関数のfavorite変数=',favorites,'  子関数上でノンローカル変数をchrome_nonlocalに設定')

    #do_global()#   favorites(グローバル変数)の上書き
    print('親関数のfavorite変数=',favorites,'  子関数上でglobal変数をnozomi_globalに設定')
   

scope_test()


'''
グローバル-- 関数 scope_test()  ......関数 do_local()
                              |
                              ......関数 do_nonlocal()
                              |
                              ......関数 do_global()

グローバル変数
グローバルスコープでは、定義、変更が自在にできる　関数からは参照できるが、更新は出来ない

ローカル変数

関数内で定義したもの、その関数からしか操作できない

明示的に nonnlocalと指定すると、親関数の変数を更新できる

明示的に global と指定すると、グローバル変数を更新できる

'''




