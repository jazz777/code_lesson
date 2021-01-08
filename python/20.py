
'''
global 変数　恐るべし

関数内でも　global 宣言すれば、関数外の変数の書き換えが可能危なっかしい。。
'''
my_favorites = "arukuma"

def hack():
    #global my_favorites
    nonlocal my_favorites
    my_favorites = "gudetama"

hack()
print('私の好きなものは',my_favorites,'です')