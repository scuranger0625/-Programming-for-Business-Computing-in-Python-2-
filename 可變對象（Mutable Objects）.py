# 可變對象的範例：列表、字典和集合

# 列表類型
l = [1, 2, 3]  # l 是列表，可變對象
print(f"Original list: {l}")
l.append(4)  # 修改列表內容
print(f"Modified list: {l}")
l[0] = 100  # 修改列表中的元素
print(f"List after changing first element: {l}")

# 字典類型
d = {"a": 1, "b": 2}  # d 是字典，可變對象
print(f"Original dictionary: {d}")
d["c"] = 3  # 添加新鍵值對
print(f"Dictionary after adding an item: {d}")
d["a"] = 100  # 修改已存在的鍵值對
print(f"Dictionary after modifying an item: {d}")

# 集合類型
s = {1, 2, 3}  # s 是集合，可變對象
print(f"Original set: {s}")
s.add(4)  # 添加新元素
print(f"Set after adding an element: {s}")
s.remove(2)  # 移除元素
print(f"Set after removing an element: {s}")

# 重要事項：
# 1. 可變對象的內容可以在創建後被修改，修改操作會影響到原對象。
# 2. 可變對象不應作為字典的鍵，因為其哈希值在對象變更後可能改變。
# 3. 可變對象需要注意同步和一致性問題，特別是在多線程環境中。
# 4. 可變對象的修改是就地進行的，不會創建新對象，因此可以節省內存。
