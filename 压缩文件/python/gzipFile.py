import gzip

f_in = open("data.txt", "rb") #打开文件

f_out = gzip.open("data.txt.gz", "wb")#创建压缩文件对象

f_out.writelines(f_in)

f_out.close()

f_in.close()