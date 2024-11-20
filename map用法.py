# map_examples.py

"""
這個檔案展示了 Python 中 map() 的各種用法和應用場景。
"""

# 1. 使用內建函數
print("1. 使用內建函數將整數轉換為字串:")
numbers = [1, 2, 3, 4, 5]
result = map(str, numbers)
print(list(result))  # 輸出 ['1', '2', '3', '4', '5']

# 2. 使用自訂函數
print("\n2. 使用自訂函數將數字平方:")
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)
print(list(result))  # 輸出 [1, 4, 9, 16, 25]

# 3. 使用 lambda 表達式
print("\n3. 使用 lambda 表達式將每個數加 10:")
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x + 10, numbers)
print(list(result))  # 輸出 [11, 12, 13, 14, 15]

# 4. 多個可迭代物件
print("\n4. 同時處理兩個列表，計算相加結果:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # 輸出 [5, 7, 9]

# 5. 實際應用場景
print("\n5. 將攝氏溫度轉換為華氏溫度:")
celsius = [0, 20, 30, 40]
result = map(lambda c: c * 9 / 5 + 32, celsius)
print(list(result))  # 輸出 [32.0, 68.0, 86.0, 104.0]

# 6. 使用 map 處理字串長度
print("\n6. 計算每個字串的長度:")
words = ["apple", "banana", "cherry"]
result = map(len, words)
print(list(result))  # 輸出 [5, 6, 6]

# 7. 使用 map 將浮點數取整
print("\n7. 將浮點數取整:")
floats = [3.14, 2.71, 1.41]
result = map(int, floats)
print(list(result))  # 輸出 [3, 2, 1]

"""
總結:
- map() 是高效處理可迭代物件的工具，適用於批量數據處理。
- 它可以搭配內建函數、自訂函數或 lambda 表達式進行操作。
- 適合處理單個或多個可迭代物件，如列表、元組等。
"""
