---
marp: true
---

# OR-Toolsで巡回セールスマン問題を解く

---

# 数理最適化とは

いくつかの制約のもとで、あるパラメータについて最もよい値を与える変数を見つけること

## 数理最適化の問題の例

- ナップサック問題
- 巡回セールスマン問題
- 乗り換え案内
- シフト決め

---

# 巡回セールスマン問題

セールスマンがいくつかの都市を1度ずつ巡るとき、総コストが最小の巡回路を求める問題

---

# メタヒューリスティクス

巡回セールスマン問題はNP困難

大規模な問題で厳密解を求めることはできないので近似解を求める

## 貪欲法

とりあえず目先の効率を優先して解を求める方法

---

## Nearest Neighbor

1. 適当な都市から出発する
2. 一番近い都市に移動する
3. 2を繰り返す

![bg right](https://cdn-ak.f.st-hatena.com/images/fotolife/y/y_uti/20171104/20171104101740.gif)

---

## Insertion

1. 2都市を部分巡回路とする
2. 都市を選び、部分巡回路の最も近い2都市の間に挿入する
3. 2を繰り返す

2での都市の選び方はランダムのものや部分巡回路に最も近いものなどがある

![bg right](https://cdn-ak.f.st-hatena.com/images/fotolife/y/y_uti/20171104/20171104134800.gif)

---

# 経路の改善

貪欲法で得られる経路には明らかに非効率的なものがある

経路を局所的に修正して結果を改善する

---

## 2-opt法

1. 巡回路から適当な2辺を選択する
2. 2辺を入れ替えて結果が改善すれば入れ替える

![bg right](https://cdn-ak.f.st-hatena.com/images/fotolife/y/y_uti/20171111/20171111102707.gif)

---

# OR-Toolsとは

Googleが開発しているオープンソースの数理最適化ツール
無料、高性能、幅広い問題に対応

## OR-Toolsで巡回セールスマン問題を解く

Python 3.6+

```
python -m venv venv
venv/scripts/activate
pip install ortools matplotlib
python tsp.py
```

---

# 参考文献

[OR-Tools | Google Developers](https://developers.google.com/optimization)

[巡回セールスマン問題の近似解法を眺める - y_uti のブログ](https://y-uti.hatenablog.jp/entry/2017/11/04/135809)

[巡回セールスマン問題の近似解法と 2-opt 改善法 - y_uti のブログ](https://y-uti.hatenablog.jp/entry/2017/11/11/115549)

## サンプルコード

[Traveling Salesperson Problem | OR-Tools | Google Developers](https://developers.google.com/optimization/routing/tsp)
