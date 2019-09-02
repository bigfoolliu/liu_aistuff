"""
1. 读取JSON

loads()方法将JSON文本字符串转为JSON对象
"""
# import json
#
# # JSON的数据需要双引号包围，否则报错
# str1 = """
# [
#     {
#         "name":"bob",
#         "gender":"male",
#         "birthday":"1990-1-1"
#     },
#     {
#         "name":"susan",
#         "gender":"female",
#         "birthday":"1991-1-1"
#     }
# ]
# """
#
# print(type(str1))
#
# # 将str转为了JSON对象，因为str最外层是[],所以转为list类型
# data = json.loads(str1)
# print(type(data), data, '\n\n')
#
# # 通过中括号加0索引，可以得到第一个字典元素，然后再调用其键名即可得到相应的
# # 键值。获取键值时有两种方式，一种是中括号加键名，另一种是通过get()方法传入
# # 键名。这里推荐使用get()方法，这样如果键名不存在，则不会报错，会返回None。
# # 另外，get()方法还可以传入第二个参数（即默认值，不存在原有键名的时候传入）
# print(data[0])
# print(data[0]['name'])
#
# print(data[0].get('gender'))
#
# print(data[0].get('age'))
# print(data[0].get('age', 10), '\n\n')
#
# # 从文本文件中读取
# with open('json_test.json', 'r') as json_test_file:
# 	json_test_object = json_test_file.read()
# 	json_test_data = json.loads(json_test_object)
#
# 	print(json_test_data)


"""
2. 输出JSON

dumps()方法将JSON对象转为文本字符串
"""
# import json
#
# data = [
# 	{
# 		"name": "tony",
# 		"gender": "male",
# 		"birthday": "1990-1-1",
# 		"爱好": "编程"
# 	}
# ]
#
# with open('json_test2.json', 'a', encoding='utf-8') as file:  # 包含中文字符，因此规定输出编码
# 	file.write(json.dumps(data))
# 	file.write(json.dumps(data, indent=2))  # indent代表缩进字符个数
# 	file.write(json.dumps(data, indent=2, ensure_ascii=False))
