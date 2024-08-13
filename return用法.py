def calculate_area(radius):
    """
    計算圓的面積並返回結果。

    參數:
    radius (float): 圓的半徑

    返回:
    float: 圓的面積
    """
    # 計算圓的面積
    area = 3.14159 * radius * radius
    return area  # 返回單個值（圓的面積）

def calculate_statistics(a, b):
    """
    計算兩個數字的和與差並返回這些值。

    參數:
    a (int, float): 第一個數字
    b (int, float): 第二個數字

    返回:
    tuple: 兩數之和及差的元組
    """
    # 計算和
    sum_result = a + b
    # 計算差
    difference = a - b
    return sum_result, difference  # 返回多個值（和與差的元組）

# 呼叫 calculate_area 函數並傳遞引數 5.0
# 該函數將返回單個值，即圓的面積
area_result = calculate_area(5.0)
print(f"Area of the circle: {area_result}")  # 輸出圓的面積

# 呼叫 calculate_statistics 函數並傳遞引數 10 和 4
# 該函數將返回多個值，即和與差
sum_result, difference_result = calculate_statistics(10, 4)
print(f"Sum: {sum_result}, Difference: {difference_result}")  # 輸出和與差

# 重要事項：
# 1. 返回單個值：
#    函數可以通過 return 語句返回單個值，例如 calculate_area 函數返回圓的面積。
# 2. 返回多個值：
#    函數可以返回多個值，這些值會被打包成一個元組，呼叫函數時可以解包這些值，
#    例如 calculate_statistics 函數返回兩數之和和差。
# 3. return 的作用：
#    return 語句不僅用於返回值，還會立即結束函數的執行。
# 4. return 的默認行為：
#    如果函數沒有 return 語句或 return 沒有跟隨任何值，函數會返回 None。
