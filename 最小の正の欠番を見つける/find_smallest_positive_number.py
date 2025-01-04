input_list = [int(i) for i in input("リストを入力してください（例: 3,4,-1,1）").strip().split(",")]

for i in range(1, len(input_list) + 2):
    if i not in input_list:
        print(f"最小の欠番: {i}")
        break