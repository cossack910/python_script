print('リストを入力してください（例: 1,2,3,4,5）:')
numbers = [int(i) for i in input().split(',')]
idx = len(numbers)

print('目標値を入力してください: ')
target = int(input())

pair_set = set()
has_pair = False

for i in range(idx):
    for j in range(i+1, idx):
        if numbers[i] + numbers[j] == target:
            has_pair = True
            pair_set.add((numbers[i], numbers[j]))

if has_pair:
    print('結果')
    for pair in pair_set:
        print(pair)
else:
    print('結果：ペアが見つかりません。')