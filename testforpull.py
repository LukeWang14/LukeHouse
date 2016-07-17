#LukeHouse test

import sys
Onedimensionlist = []
Twodimensionlist = []
while True:
    message = sys.stdin.readline()
    if message == '\n':
        break
    else:
        message.rstrip() #去除多余的括号
        partlist = message.split()   #根据空格分裂成列表
        Twodimensionlist.append(partlist)
         #读取列表字符串并将字符串转换成列表
for x in Twodimensionlist:
    for y in x:
        y = int(y) #二维列表中的元素转换成整数
        Onedimensionlist.append(y) 
print(Onedimensionlist)
//试一试
