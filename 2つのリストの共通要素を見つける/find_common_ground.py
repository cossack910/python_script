l1 = input('リスト1を入力してください（例: 1,2,3,4）：').split(',')
l2 = input('リスト1を入力してください（例: 3,4,5,6）：').split(',')

s1 = set([int(i) for i in l1])
s2 = set([int(i) for i in l2])

# 積集合
print(f'共通要素: {list(s1 & s2)}')