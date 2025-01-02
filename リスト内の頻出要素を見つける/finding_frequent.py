from collections import Counter

input_list = [int(i) for i in input("リストを入力してください（例: 1,2,2,3,3,3,4）:").strip().split(",")]
count = Counter(input_list)

max_count(count.values())
most_frequent = min(key for key, val in count.items() if val == max_count)
print(f"最も頻出する要素: {most_frequent} (出減回数: {max_count} )")