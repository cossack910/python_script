try:
    numbers = [int(i) for i in input("リストを入力してください（例: 10,20,30,40）：").strip().split(',')]
    
    if len(numbers) < 2:
        print("リストは２つ以上入力してください")
        raise ValueError("エラー: 入力はカンマ区切りの整数である必要があります。")
    else:
        max_num = max(numbers)
        second_numbers = [i for i in numbers if max_num > i]
        print(f"２番目に大きい数：{max(second_numbers)}")
except ValueError as e:
    print(e)