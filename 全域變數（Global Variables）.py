# 定義：全域變數是在函數外部定義的變數，其作用範圍在整個程式中。
global_var = "I'm a global variable"

def example_function():
    # 作用範圍：全域變數可以在程式的任何地方使用，包括函數內部和外部。
    print(global_var)  # 可以在函數內部訪問全域變數

def modify_global():
    global global_var  # 使用 global 關鍵字聲明要修改的全域變數
    # 修改全域變數的值
    global_var = "Global variable modified!"

example_function()  # 輸出: I'm a global variable

# 生存期：全域變數在整個程式的執行期間都存在，直到程式終止或顯式地刪除這些變數。
print(global_var)  # 輸出: I'm a global variable

modify_global()
print(global_var)  # 輸出: Global variable modified!
