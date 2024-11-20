# try_except_demo.py

"""
這個檔案介紹了 Python 中的 try-except 機制，主要用來處理程式執行過程中可能出現的錯誤。
"""

# 1. 基本語法

# 基本的 try-except 範例
try:
    # 嘗試執行一段可能引發錯誤的程式碼
    num = int(input("請輸入一個數字: "))
    print("你輸入的數字是:", num)
except ValueError:
    # 當發生 ValueError 例外時，會執行這段程式
    print("輸入無效！請輸入一個整數。")

# 2. 捕捉不同類型的例外

# 多層例外處理範例
try:
    num = int(input("請輸入一個整數: "))
    result = 10 / num
    print("計算結果:", result)
except ValueError:
    print("輸入無效！請輸入整數。")
except ZeroDivisionError:
    print("無法除以零！")
except Exception as e:
    print(f"發生其他錯誤: {e}")

# 3. 使用 finally 釋放資源

# 使用 finally 確保檔案被關閉
try:
    file = open("example.txt", "r")
    # 進行檔案操作
    data = file.read()
    print("檔案內容:", data)
except FileNotFoundError:
    print("檔案未找到！")
finally:
    try:
        file.close()  # 確保檔案被關閉
        print("檔案已關閉")
    except NameError:
        print("未能開啟檔案，無需關閉檔案。")

# 4. 不要濫用 try-except

# 範例：不應該用 try-except 來處理預期的情況
# 不建議這樣做：
try:
    num = 10
    if num > 0:
        print("正數")
except:
    print("錯誤")  # 這是不必要的錯誤處理

# 5. 總結
"""
try-except 是 Python 用來捕捉錯誤並進行處理的重要機制。正確使用能提高程式的穩定性和可讀性。

使用建議：
- 使用 try-except 處理那些不確定是否會發生錯誤的情況。
- 捕捉具體的例外，而不是使用通用的 Exception。
- 若沒有必要捕捉錯誤，應避免使用 try-except。
- 若有需要，使用 finally 來釋放資源或執行清理工作。
"""
