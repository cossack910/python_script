# 親子関係の階層ツリー構造を構築

ユーザーが入力した「親 - 子」の関係をもとに、階層的なツリー構造を構築し、表示するプログラムを作成してください。

## 要件:

1. ユーザーにカンマ区切りで「親-子」のペアを複数入力させます。
   例: "A-B,B-C,B-D,A-E"
1. 入力されたデータをもとに、親子関係の階層ツリーを構築します。
1. 構築されたツリーを視覚的に表示します。

### サンプル出力

入力例:

```
親子関係を入力してください（例: A-B,B-C,B-D,A-E）: A-B,B-C,B-D,A-E
ツリー構造:
- A
  - B
    - C
    - D
  - E
```
