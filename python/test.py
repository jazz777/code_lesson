import json
dic={'aize': 'M', 'name': 'nozomi'}
#with open('/home/taiichi930/file1','r+') as fp:
with open('/home/taiichi930/code_lesson/python/file','w+') as fp:
    fp.write(json.dumps(dic,indent=4))

