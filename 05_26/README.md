# 5/19
## 今週のお告げ
- 締め切りを守る工夫をしよう
    - どうしても人間は忘れてしまう
    - そのためツールを使って補う
    - calendar, Todo, とかとか
    - Mac だと Calendar アプリ、 Reminder アプリとか使うといいかな(icloud で同期したら ios 端末でも見られる)

## Turing complete(チューリング完全)
- これまでに紹介した機能
    - number
    - assignments
    - input/output
    - comparisons
    - looping
- これらの機能でチューリング完全(チューリングマシンを再現できる)
- **チューリングマシン**って?
    - 0, 1を記述できる無限長のテープがある
    - そのテープに対して移動と読み書きする命令をもつ
    - これを表現できるとチューリング完全
- チューリング完全ならこの世に出ている**すべてのプログラム**を書くことが可能

## Keywords Arguments and Default Values
- 関数名はデフォルト値を指定することができる
- 基本的にはデフォルト値を指定しているものは後ろに書く

``` python
# range() 関数
# step はdefault 値を指定している
def myrange(start, stop, step=1):
    result = []
    num = start
    while num<stop:
        result.append(num)
        num += step

    return result

# 実行例
>>> myrange(0, 5)
[0,1,2,3,4]
# ``start =`` みたいに指定することができる
# こうすれば呼び出し元からその関数の引数がなにを取るのかがわかりやすい
>>> myrange(start=0, stop=5)
[0,1,2,3,4]
# デフォルト値は書き換え可能
>>> myrange(0, 5, step = 2)
[0,2,4]
```

## Stack frame と Name Space
- 関数f()の定義
    - コード内部については実行時に作成される、定義時点では関数名のみ(この時点ではtoplevel)
    - stack frame: 1
    - name: f()
- コードの実行
    - ここもまだtoplevel
    - stack frame: 1
    - name: f(), x=3, y=2
- 関数実行(関数呼び出し)
    - 関数呼び出し直前(まだtoplevel)
        - z は保存される
        - stack frame: 1
        - name: f(), x=3, y=2, z
    - 関数実行 ~ return 直前
        - 関数を実行するさいstack frame が変わる
        - name も その時のstack frame を参照する(今回はy,x)
        - stack frame: 1
        - name: y=1, x=4
    - 関数実行結果の代入
        - stack frame 2の関数が終わったので stack frame 1に戻る
        - stack frame: 1
        - name: f(), x=3, y=2, z=4

``` python
def f(x):
    y = 1
    x = x + y
    print('f(x): x = {0}'.format(x))
    print('f(x): y = {0}'.format(y))
    return(x)

x = 3
y = 2
z = f(x)

print('x = {0}'.format(x))
print('y = {0}'.format(y))
print('z = {0}'.format(z))

def g():
    print('z = {0}'.format(z))g()
```

## Stack Frame のポイント
- 関数が呼び出されるたびに新しいstack frame ができる
- 個々の処理はスコープ外にあるスタックフレームには影響を及ぼさない(例外あり)
- 関数が終了するとスタックフレームは廃棄(pop)される(残ってるとメモリを圧迫してしまうため)
- 現スタックフレームに記録されていない名前が参照されると「呼び出し元のスタックフレーム」を検索する。
    - この検索をトップレベルまで繰り返しでも見つからない場合、NameError となる

## Specification(仕様、ドキュメント)
- コメント文
    - ``#`` から後の文
- docstring形式によるコメント
    - ``"""~"""`` で囲った、複数行に渡るコメント
    - インデントでブロックを揃えること
    - 簡易ドキュメントとして使える
    - pydoc3 コマンド、pythonインタプリタのhelp コマンド を使うと簡易ドキュメントが見える(引数は**モジュール名**なので注意)

```
% pydoc3 week6_doctest
# -w を付けると html を生成する
% pydoc3 -w week6_doctest
```

- 実際は下のコードのようになっている
- 上のコメントはモジュールの **DESCRIPTION**  になる
- ``def add`` のあとに書いているコメントは **FUNCTIONS** のドキュメントになる

``` python
"""This is "week6_doctest" module.

This module supplies one function, add(). For example,

>>> add(1, 2)
3

Note:
    If you want to do testing by doctest,
    type "python3 week6_doctest.py -v".

"""

def add(arg1, arg2):
    """Return the added value for arg1 and arg2.

    Args:
        arg1 (int or float): a number of int- or float-object.
        arg2 (int or float): a number of int- or float-object.

    Returns:
        int or float: the added value arg1 and arg2

    >>> add(-1, 3)
    2
    >>> add(0, 0.5)
    0.5
    """
    return arg1 + arg2


if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

```
% pydoc3 week6_doctest

Help on module week6_doctest:

NAME
    week6_doctest - This is "week6_doctest" module.

DESCRIPTION
    This module supplies one function, add(). For example,

    >>> add(1, 2)
    3

    Note:
        If you want to do testing by doctest,
        type "python3 week6_doctest.py -v".

FUNCTIONS
    add(arg1, arg2)
        Return the added value for arg1 and arg2.

        Args:
            arg1 (int or float): a number of int- or float-object.
            arg2 (int or float): a number of int- or float-object.

        Returns:
            int or float: the added value arg1 and arg2

        >>> add(-1, 3)
        2
        >>> add(0, 0.5)
        0.5

FILE
```

## Module(モジュール、部品)
- ``import モジュール名`` で自作モジュールを読み込む
    - この際**モジュール名.py**を探してimportする
- ``モジュール名.関数名(引数1, 引数2,...)`` とすることでモジュール内の部品(関数)を利用可能

``` python
>> import week6_doctest
>> week6_doctest.add(1,2)
3
```

- ``import モジュール名 as 別名`` とするとモジュール名に別名を付けることができる
- 別名を付けると部品を使う際 ``別名.関数名`` で呼び出すことが可能

``` python
>> import week6_doctest as wd
>> add(1,2)
3
```

- ``from week6_doctest import 部品名``  とするとモジュール内の部品を指定して読み込むことができる
    - 部品名の部分に``\*``を指定するとすべての部品を読み込む
- こうすることで部品を使う際にモジュール名や別名を付けなくても良い
- ただし既存の関数などを**上書きする可能性**があるので注意

``` python
>>> from week6_doctest import *
>>> add(1,2)
3
```

- 読み込んだモジュールは``help()`` で簡易ドキュメントを参照できる

``` python
>>> import week6_doctest as wd
>>> help(wd)
```

## doctest によるユニットテスト
- ユニットテスト
    - 今までは実際に実行してみてあってるかどうかを``print()``なりを使って目視で確認していた
    - ユニットテストは目視では無く、関数が**想定した入力を与えたら想定した結果が得られること** を確認できる
- doctest によるユニットテスト
    - 実行できるドキュメント(**docstring**)
    - 通常のスクリプト処理
        - `` % python3 week_doctest.py``
    - ユニットテストの処理
        - ``% python3 week6_doctest -v``
- doctest は docstring の中でインタプリタっぽく書かれている

``` python
"""Return the added value for arg1 and arg2.

Args:
    arg1 (int or float): a number of int- or float-object.
    arg2 (int or float): a number of int- or float-object.

Returns:
    int or float: the added value arg1 and arg2

ここからdoctestとして読み込まれる
>>> add(-1, 3)
2
>>> add(0, 0.5)
0.5
"""
```

```
% python week6_doctest.py -v
Trying:
    add(1, 2)
Expecting:
    3
ok
Trying:
    add(-1, 3)
Expecting:
    2
ok
Trying:
    add(0, 0.5)
Expecting:
    0.5
ok
2 items passed all tests:
   1 tests in __main__
   2 tests in __main__.add
3 tests in 2 items.
3 passed and 0 failed.
Test passed.
```

- doctest の注意点として返り値の部分に**スペースやインデント**を入れると失敗する
- このように癖が強い所もあるが、このテストが簡易ドキュメントにも表示されるので、実行例の表示とtest が両方できる(とても便利)

## 宿題
- 教科書読み
- レポート
    - [レポート課題2](https://ie.u-ryukyu.ac.jp/~tnal/2016/prog1/report2.html)
    - 提出は2週間後の授業開始前
