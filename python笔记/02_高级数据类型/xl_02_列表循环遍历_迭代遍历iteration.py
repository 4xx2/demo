num_list = [1, 2, 3, 4, 7, 0, 10, 234, 1234, 32, 234]

# 使用迭代遍历列表
"""
顺序地从列表中依次获取数据，每次循环，数据都会保存在num这个变量中。
从而在循环体内部可以访问到当前这一次获取的数据。
"""
for num in num_list:
    print(num)
