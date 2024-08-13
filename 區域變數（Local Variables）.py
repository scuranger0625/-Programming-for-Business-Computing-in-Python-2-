def example_function():
    # 定義：區域變數是在函數內部定義的變數，其作用範圍僅限於該函數內部。
    local_var = "I'm a local variable"  
    
    # 作用域：區域變數只能在定義它們的函數內部使用。
    print(local_var)  # 可以在函數內部訪問區域變數

    # 一旦函數執行完畢，這些變數就不再存在。
    # 生存期：區域變數的生存期從它們被創建（通常是在函數調用時）到函數執行完畢之間。
    # 在這之後，這些變數將被銷毀。

example_function()

# print(local_var)  # 這行會報錯，因為 local_var 只在函數內部有效
