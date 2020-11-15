table={'orange':150,'apple':200,'banana':100}
for n,h in table.items():
#    print('{0:10}>>>>{1:10}'.format(n,h))
    print('{0:<10}>>>{1:>5}'.format(n,h))
"""
桁数の違う文字列や、数字を表示すると、レイアウトが崩れる
なので、桁数を予め定義しておく　
決めた桁数の中で、左よせしたければ　＜
右寄せしたければ　＞
中央寄せしたければ、^
と表現する。
"""
print()
print()
print()

for a in range(10):
#    print(a)
    print('{:5d}{:5d}{:5d}'.format(a,a**2,a**3))

print()
print()
print()

for a in range(10):
#    print(a)
    print('{:5}{:5}{:5}'.format(a,a**2,a**3))