# import csv
# 能够读出第一行的内容
# # 打开文件，用with打开可以不用去特意关闭file了，python3不支持file()打开文件，只能用open()
# with open("names.csv", "r") as csvfile:
#      # 读取csv文件，返回的是迭代类型
#      read = csv.reader(csvfile)
#      for i in read:
#          print(i)


import csv
# 不要读出第一行的内容
csvFile = open("names.csv", "r")
dict_reader = csv.DictReader(csvFile)
for row in dict_reader:
    print(row)