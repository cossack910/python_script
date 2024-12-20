input_arr = [int(i) for i in input("リストを入力してください（例: -1,0,1,2,-1,-4）：").strip().split(',')]
set_arr = list(set(input_arr))
sort_arr = sorted(set_arr)

l = len(sort_arr)

zero_combination_list = []
for s_i in range(l):
    for s_j in range(l):
        if s_j == s_i:
            continue
        for s_k in range(l):
            if s_k == s_j or s_k == s_i:
                continue
            if sort_arr[s_i] + sort_arr[s_j] + sort_arr[s_k] == 0:
                zero_combination_list.append(sorted([sort_arr[s_i], sort_arr[s_j], sort_arr[s_k]]))

ans = [tuple(i) for i in zero_combination_list]
print(f"ゼロになるくみあわせ:{list(set(ans))}")