print('１つ目の文字列を入力してください')
s1 = input().replace(" ", "").lower()

print('２つ目の文字列を入力してください')
s2 = input().replace(" ", "").lower()


def is_anagram(s1: str, s2: str):
    return sorted(s1) == sorted(s2)

if is_anagram(s1, s2):
    print('結果：アナグラムです')
else:
    print('結果：アナグラムではありません')