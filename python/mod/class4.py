class Rajiko:
    def __init__(self):
        self.name_housoukyoku=''
        self.band=0
        self.volume=10
        self.dic={'日本放送':1242,'TBS':954}

    def set_band(self,name_housoukyoku):
        self.name_housoukyoku=name_housoukyoku
        self.band=self.dic[name_housoukyoku]


"""
oreraji=Rajiko()
oreraji.set_band('日本放送')
print(oreraji.name_housoukyoku,oreraji.band,'メガヘルツを選択しました')


def abc():
    print('abc')

"""
"""
データ
 放送局名 list_company= {'日本放送':1242,'TBS':954}
 音量　　 volume=10

操作
 放送局を選択する set_band(放送局)
 再生する　　　　 start_radio()
 停める　　　　　 stop_radio
 音量を＊＊にする set_volume(ボリューム)
 """
