# 重要事項：
# 1. abs() 是 Python 的內建函數，用於計算數字的絕對值。
# 2. 絕對值是指數字與零的距離，因此結果總是非負的。
# 3. abs() 可以應用於整數、浮點數以及複數。
#    - 對於整數和浮點數，返回該數字的非負值。
#    - 對於複數，abs() 返回的是複數的模，即該複數在複數平面上到原點的距離。

# 範例 1: 計算整數的絕對值
number = -10
absolute_value = abs(number)
print(f"The absolute value of {number} is {absolute_value}.")  # 輸出：The absolute value of -10 is 10.

# 範例 2: 計算浮點數的絕對值
float_number = -3.14
absolute_float_value = abs(float_number)
print(f"The absolute value of {float_number} is {absolute_float_value}.")  # 輸出：The absolute value of -3.14 is 3.14.

# 範例 3: 計算零的絕對值
zero = 0
absolute_zero_value = abs(zero)
print(f"The absolute value of {zero} is {absolute_zero_value}.")  # 輸出：The absolute value of 0 is 0.

# 範例 4: 計算複數的絕對值
complex_number = 3 - 4j
absolute_complex_value = abs(complex_number)
print(f"The absolute value of {complex_number} is {absolute_complex_value}.")  # 輸出：The absolute value of (3-4j) is 5.0.
