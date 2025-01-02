print('文字列を入力してください: ')

word = input().strip().replace(' ', '').lower()
if word == word[::-1]:
    print('回文です')
else:
    print('回文ではありません')