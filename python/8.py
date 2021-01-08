
with open('non','r') as a:
    s=a.read()
    print(type(s))
    print(s)


#s='nozomi ha kawaii\nore ha chiisai\nrukuma mo kawaii'

print('##############')
import re
lst=re.findall('.*m',s)
print(re.findall('.*m',s))
print(type(re.findall('.*m',s)))
print((lst[9]).center(100))
