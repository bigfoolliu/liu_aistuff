'''
1. csv文件写入

单行写入用writer()方法
多行写入用writerows()方法
'''
'''
import csv
 
with open('csv_test.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')# delimiter参数使输出结果每一列以空格分隔
    
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

    writer.writerows([['10004', 'sam', '23'], ['10005', 'jane', 21]])

    # 爬虫爬取的为结构化数据，用字典表示，用字典写入
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
'''




'''
2. csv文件读取

reader()方法读取
或pandas库中的read_csv()方法
'''

import csv
import pandas

with open('csv_test.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)


# 此种方法用的更多，更方便
csv_file = pandas.read_csv('csv_test.csv')
print(csv_file)
