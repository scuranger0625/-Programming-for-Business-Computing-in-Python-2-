# 不可變對象的範例：數字、字符串和元組

# 數字類型
x = 10  # x 是整數，不可變對象
print(f"Original x: {x}")
x += 5  # 試圖修改 x，實際上是創建了一個新對象
print(f"Modified x: {x}")

# 字符串類型
s = "hello"  # s 是字符串，不可變對象
print(f"Original string: {s}")
s += " world"  # 試圖修改 s，實際上是創建了一個新字符串對象
print(f"Modified string: {s}")

# 元組類型
t = (1, 2, 3)  # t 是元組，不可變對象
print(f"Original tuple: {t}")
t += (4, 5)  # 試圖修改 t，實際上是創建了一個新元組
print(f"Modified tuple: {t}")

# 重要事項：
# 1. 不可變對象一旦創建，其內容無法更改。任何修改操作實際上都是創建一個新的對象。
# 2. 不可變對象通常具有更高的內存和運行時效率，因為它們的值不變，因此可以安全地在多個地方共享。
# 3. 不可變對象適合作為字典的鍵，因為它們的哈希值不變。
