def modify_list(input_list):
    """
    接收一個列表並修改其內容，返回修改後的列表。
    此函數展示了函數傳入值、傳回值以及指定傳入法（Call by Assignment）。

    參數:
    input_list (list): 傳入的列表

    返回:
    list: 修改後的列表
    """
    # 修改傳入的列表（因為列表是可變對象，函數內部的改動會影響到外部）
    input_list.append(4)
    input_list[0] = 100
    return input_list  # 傳回值為修改後的列表

# 定義一個初始列表
my_list = [1, 2, 3]

# 傳入值：將 my_list 傳入函數 modify_list
modified_list = modify_list(my_list)

print("Original list:", my_list)        # 輸出：Original list: [100, 2, 3, 4]
print("Modified list:", modified_list)  # 輸出：Modified list: [100, 2, 3, 4]

# 重要事項：
# 1. 傳入值（Arguments）：
#    函數 modify_list 接收一個參數 input_list，這個參數在呼叫函數時由外部傳入的列表 my_list 提供。
# 2. 傳回值（Return Value）：
#    函數通過 return 語句返回一個列表，這是函數的傳回值。在這個範例中，傳回值是修改後的列表。
# 3. 指定傳入法（Call by Assignment）：
#    在 Python 中，變數在傳遞給函數時，實際上是將變數的引用（即記憶體地址）傳遞給函數參數。
#    對於可變對象（如列表），函數內對該對象的修改會反映在外部，因為內部和外部都引用同一個對象。
