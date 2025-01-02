def search_top_node(tree_dict : dict) -> str:
    """辞書からトップノードを検索する"""
    for k in tree_dict:
        flg = True
        for key, value in tree_dict.items():
            if k in value:
                flg = False
                break
        if flg:
            return k
    raise ValueError("ノードの頂点が見つからないぞ☆")

def display_tree(tree_dict: dict, node: str, depth: int = 0):
    """ツリー構造を再起で表示する"""
    print("  " * depth + f"- {node}")
    if node in tree_dict and tree_dict[node][0]:
        display_tree(tree_dict, tree_dict[node][0], depth + 1)
    if node in tree_dict and tree_dict[node][1]:
        display_tree(tree_dict, tree_dict[node][1], depth + 1)
    return False

def tree_list_validation(tree_list: list) -> bool:
    """親子リストの検証（循環構造がないかチェック）"""
    for i in range(len(tree_list)):
        for j in range(i + 1, len(tree_list)):
            if tree_list[i][::-1] == tree_list[j]:
                return False
    return True

def main():
    tree_list = input("親子関係を入力してください（例: A-B,B-C,B-D,A-E）:").strip().split(",")
    if not tree_list_validation(tree_list):
        raise ValueError("階層構造が変だぞ☆")
    tree_dict = {i[0]:[] for i in tree_list}
    for t in tree_list:
        tree_dict[t[0]].append(t[2])
    top_node = search_top_node(tree_dict)
    display_tree(tree_dict, top_node)

if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)