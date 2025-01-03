def expand_center(s, left, right):
    """中心を指定して左右に拡大して回文を確認"""
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def find_longest_palindrome(s):
    """最長の回文部分文字列を探す"""
    if not s:
        return ""
    
    longest = ""
    for i in range(len(s)):
        # 奇数長の回文を探索
        odd_palindrome = expand_center(s, i, i)
        # 偶数長の回文を探索
        even_palindrome = expand_center(s, i, i + 1)

        # 現在の最長回文を更新
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    
    return longest

input_string = input("文字列を入力してください: ").strip()
result = find_longest_palindrome(input_string)
print(f"最長の回文部分文字列: {result}")
