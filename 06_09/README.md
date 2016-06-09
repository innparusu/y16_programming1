# 6/9
## 今週のお告げ
- 「**機械翻訳後の買得に苦労しても得られるものは少ない**」
- 機械翻訳された謎の文章中心で見るとあまり意味がない
- 英文を読むようにしよう
- 英英辞書を使おう

## 復習
- KISS原則
    - Keep it simple, stupid
    - なるべる小さくつくり、組み合わせる
- DRY 原則
    - Don't repeat yourself
    - 繰り返しを避ける
- 2つの原則もなるべく関数化して、組み合わせる

## 4.6 Files
- FileI/O
    - File input/output
- ファイルを読み書きするには
    1. ファイルハンドラ(file handle) を準備
    2. ハンドラに対して読み書きする
    3 読み書きし終えたらハンドラを閉じる

- ``open`` 関数でファイルハンドラを準備する
    - 第一引数にファイル目
    - 第二引数で指定したモードによってハンドラを容易
        - ``'w'`` を渡すと上書きモードでアクセスする
        - ``'r'`` を渡すと読み込みモード(default)
- ``write()`` でハンドラに対して書き出す
- ``close()`` でハンドラを閉じる
    - 閉じることを忘れないようにする
    - なぜならファイルに書き込むということはCPUに比べて遅い命令のため、わざわざ``write``の度にファイルに書き込まない(CPUとの兼ね合いがある)
    - ``close``を忘れてしまうと書き出すタイミングを逃す場合がある

``` python
name_handle = open('kinds', 'w')
for i in range(2):
    name = input('Enter name:')
    name_handle.write(name+'\n')

name_handle.close()
```

## with構文
- with文で操作したいファイル名とモードを指定することでブロックの処理が終わると自動でclose()する
    - 途中でエラーになっても閉じる

``` python
# ファイルへ書き込む
with open('spam.txt', 'w') as file:
    file.write('Spam and eggs!')
    file.write('hogege')
```

## 代表的なFileI/O操作
- 行ごとに書き込む場合はそれぞれ
    - ``fh.readlines()``
    - ``fh.writelines(S)``
- を使う

## 5.1 Tuples
- tupleは文字列と同様に順序のあるシーケンス集合
- 要素が文字である必要はない
- 文字列と同様にtupleは変更できない(immutableな)オブジェクト

``` python
>>> t1 = ()
>>> t2 = (1, 'two', 3)
>>> print(t1)
()
>>> print(t2)
(1, 'two', 3)
>>> t2[0]
1
>>> t2[0] = 0 # 変更しようとするとエラー
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

## タプルの補足
- どこで使われるの?
    - 関数の戻り値
    - リストよりも高速
    - 変更を許可したくない場合
    - 辞書型オブジェクトのキーとして使える
- 1個の要素をもつタプル
    - ``(1)``ではその一つのオブジェクトになってしまう
    - ``(1,)`` と定義する必要がある
