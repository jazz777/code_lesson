import json
dic={'name':'ore','age':51}
'''
print(json.dumps(dic))
print(type(json.dumps(dic)))
'''

with open('b','w') as fp2:
    json.dump(dic,fp2)

'''
with open('a','r') as fp:
    s=fp.read()
    print(s)
'''

#print(type(dic))
