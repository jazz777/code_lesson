# write関数
def wr(file,str):
  with open(file,'w') as f:
    f.write(str)

# read関数
def rd(file):
  with open(file,'r') as f:
    print(f.read())
