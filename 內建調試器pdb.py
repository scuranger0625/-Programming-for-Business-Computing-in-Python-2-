def divide(a, b):
    # 當除數為0時，拋出異常
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def process_numbers(numbers):
    total = 0
    for i in range(len(numbers)):
        # 設置一個調試斷點，程式會在這裡暫停
        import pdb; pdb.set_trace()

        # 使用 `p` 命令檢查變量 `numbers[i]` 和 `i` 的值
        # 例如，p numbers[i] 和 p i

        total += divide(numbers[i], i)
        # 如果 `i` 為 0，divide 函數將拋出除零異常

        # 使用 `n` 命令單步執行代碼，或 `c` 命令繼續運行程序
    return total

def main():
    numbers = [10, 20, 30, 40, 50]
    
    # 開始處理數字列表
    result = process_numbers(numbers)
    
    # 打印最終結果
    print(f"The final result is: {result}")

if __name__ == "__main__":
    # 使用 `pdb` 調試時，程序會在 `pdb.set_trace()` 處暫停，
    # 你可以使用各種命令來檢查和調試代碼
    main()
