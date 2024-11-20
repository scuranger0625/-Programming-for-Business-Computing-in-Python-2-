# lambda_examples.py

"""
這個檔案介紹了 Python 中 lambda 的基本用法和常見場景。
"""

# 1. 基本用法
# lambda 表達式是用於定義簡短的匿名函數的關鍵字。

# 1.1 簡單加法
add = lambda x, y: x + y
print("加法運算:")
print(f"3 + 5 = {add(3, 5)}")  # 輸出 8

# 1.2 平方運算
square = lambda x: x ** 2
print("\n平方運算:")
print(f"4 的平方是 {square(4)}")  # 輸出 16

# 1.3 無參數函數
greet = lambda: "Hello, World!"
print("\n無參數函數:")
print(greet())  # 輸出 Hello, World!

# 2. lambda 與高階函數結合
# 2.1 與 map 結合
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print("\n使用 map 對數字進行倍數化:")
print(list(doubled))  # 輸出 [2, 4, 6, 8, 10]

# 2.2 與 filter 結合
even = filter(lambda x: x % 2 == 0, numbers)
print("\n使用 filter 過濾偶數:")
print(list(even))  # 輸出 [2, 4]

# 2.3 與 sorted 結合
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print("\n使用 sorted 按字串長度排序:")
print(sorted_words)  # 輸出 ['apple', 'cherry', 'banana']

# 3. lambda 在資料結構中的應用
items = [("apple", 3), ("banana", 2), ("cherry", 5)]
sorted_items = sorted(items, key=lambda x: x[1])
print("\n使用 lambda 對資料進行排序:")
print(sorted_items)  # 輸出 [('banana', 2), ('apple', 3), ('cherry', 5)]

# 4. lambda 作為臨時函數
def calculate(operation, x, y):
    return operation(x, y)

result = calculate(lambda a, b: a * b, 3, 4)
print("\n使用 lambda 作為函數參數:")
print(f"3 * 4 = {result}")  # 輸出 12

# 5. lambda 的注意事項
# lambda 只能用於單行表達式，複雜邏輯應使用普通函數。

"""
try:
    # lambda 不支援多行邏輯
    invalid_lambda = lambda x: if x > 0: x  # 這行會報錯
except SyntaxError:
    print("\nlambda 無法處理多行邏輯。請使用普通函數。")

"""

"""
總結:
lambda 適用於簡短的匿名函數需求，例如 map、filter 和 sorted 等場景。
如果邏輯較複雜，應優先使用普通函數以提高可讀性。
"""
