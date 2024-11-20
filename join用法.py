# join_examples.py

"""
這個檔案展示了 Python 中 join() 方法的各種用法和應用場景。
"""

# 1. 使用空格將列表中的字串連接
print("1. 使用空格將列表中的字串連接:")
words = ['Hello', 'World']
result = ' '.join(words)
print(result)  # 輸出 'Hello World'

# 2. 使用不同的分隔符
print("\n2. 使用不同的分隔符:")
fruits = ['apple', 'banana', 'cherry']
comma_separated = ', '.join(fruits)
print(comma_separated)  # 輸出 'apple, banana, cherry'

hyphen_separated = '-'.join(fruits)
print(hyphen_separated)  # 輸出 'apple-banana-cherry'

# 3. 空分隔符將字元合併
print("\n3. 空分隔符將字元合併:")
chars = ['P', 'y', 't', 'h', 'o', 'n']
result = ''.join(chars)
print(result)  # 輸出 'Python'

# 4. 將列表數字轉為字串並用逗號分隔
print("\n4. 將列表數字轉為字串並用逗號分隔:")
numbers = [1, 2, 3, 4]
result = ', '.join(map(str, numbers))  # 必須轉換為字串
print(result)  # 輸出 '1, 2, 3, 4'

# 5. 合併日誌條目
print("\n5. 合併日誌條目:")
log_parts = ['INFO', '2024-11-20', 'Task completed']
log_entry = ' | '.join(log_parts)
print(log_entry)  # 輸出 'INFO | 2024-11-20 | Task completed'

# 6. 處理空列表
print("\n6. 處理空列表:")
empty_list = []
result = ', '.join(empty_list)
print(f"空列表結果: '{result}'")  # 輸出 ''

# 7. 使用 join 合併字串取代 for 迴圈的 + 操作
print("\n7. 使用 join 合併字串取代 for 迴圈的 + 操作:")
words = ['This', 'is', 'Python']
# 使用 + 方式
result = ''
for word in words:
    result += word + ' '
print(result.strip())  # 輸出 'This is Python'

# 使用 join
result = ' '.join(words)
print(result)  # 輸出 'This is Python'

"""
總結:
- join() 是一個用於將可迭代物件（如列表或元組）中的元素連接為字串的方法。
- 它能高效處理大量字串連接，適用於各種格式化輸出或數據處理場合。
"""
