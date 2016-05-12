# 5/12
## 今週のお告げ
    - 「コピー機になるな」

## ミニテスト
    - 1レポート1分眺める * 4回
    - ベストだと思ったレポート1件をセレクト
    - これをペアに見せていいところを教える
    - お互いやった後にどちらかいいものを紹介

## 演習や課題についての補足
    - 設問分の意図がわからないよ！
        - どんどん聞こう
    - 出力結果を読もう
        - エラーが出たまま次に進んでいるケースがあるらしい
    - 報告書
        - 学籍番号、氏名を書く
    - 変数名
        - 命名規則を参考に、適切な変数名を付ける
    - 個別コメント

## 関数定義について
- 一連の手続きに名前をつける
- コード的には def 名前
- x, y, a, b は関数内での呼び名(ローカル変数と呼ばれる)
    - 引数に名前をつけただけ
- 局所的にしか使えない(関数内など)変数をローカル変数と呼ぶ

``` python
def add(x,y)
    answer = x + y
    return answer

# ↑ と動作は同じ
def add(a,b)
    answer = a + b
    return answer
```

## 2.4 Iteration, looping
- if は True なら True block, False なら False block を実行
- Loop は **True** なら **Loop ブロック を実行し**、 その後に条件判断し、 True ならまた Loop ブロックを実行
- **False** になると **Loop ブロックを実行せず**、次の処理に移る

``` python
import random

# HP 3~7を取る敵を用意する関数
def encount_enemy(): 
    hitpoint = random.randint(3, 7) # ここで3~7をランダムに用意
    return hitpoint # hitpoint を返す

enemy_hitpoint = encount_enemy() # encount_enemy を呼び出して戻り値を enemy_hitpoint に代入
print('スライムに遭遇した。 (敵HP = ', enemy_hitpoint, ')')

# enemy_hitpoint が 0より大きいなら block (その後の3行) を繰り返し実行
# つまり今回の場合、 enemy_hitpoint を減らす演算(enemy_hitpoint - attack) があるためそれの結果が 0 より小さくなったら
# ループブロックを実行せずに次の処理に移る
while(enemy_hitpoint > 0): # while 構文(この条件が True なら その後のblock を繰り返す)
    attack = random.randint(2,4) # ランダム に 2~4 を用意
    enemy_hitpoint = enemy_hitpoint - attack # 敵の hitpoint と attack の差を取る
    print('あなたの攻撃! スライムに', attack, 'のダメージ! (敵HP =', enemy_hitpoint, ')')

print('スライムを倒した!')
```

## レポートの取り組み方
- 問題を分割する
    - わかる所から手を付ける
    - わからないところは更に分割
        - それでもわからないなら 先生, TA, 先輩を尋ねる
- 個々のサブ問題を個別に解く
    - これ以上分割できない状態なら教科書や授業でやっているはず
    - 該当部分を復習
    - サブ問題の方をレポートで解説してもよいかも(report1 の場合、 **if文**とはとか **関数定義** とはとか)
- 最後に分割したものを結合

