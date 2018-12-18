#!/usr/bin python3
def copyfile(src,dst):
    line1=[] 
    with open(src,'r') as srcfile:
        lines = srcfile.readlines()
        print(lines)
        for i,line in enumerate(lines):
            line = str(i+1)+' '+line
            print(line)
        #    for line in lines:
         #       print(lines)   
        #for i,x in enumerate(srcfile.readlines()):
            line1.append(line)
            with open(dst,'w') as dstfile:
                dstfile.writelines(line1)
       # with open(dstfile,'r') as dstfile1:

        #    for i,x in enumerate(dstfile1.readlines()):
         #       print(i,x,end ='')
if __name__ == '__main__':
    src = '/home/shiyanlou/shiyanlou.txt'
    dst = '/home/shiyanlou/shiyanlou_copy.txt'
    copyfile(src,dst)
#    with open(dst,'r') as dstfile:
 #       for i, x in enumerate(dstfile.readlines()):
  #          print(i,x,end= ' ')
