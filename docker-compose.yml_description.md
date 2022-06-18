```docker-compose.yml
1   version: "3"
2   services:
3     raitochinyu:
4       container_name: RaitochinyuBot
5       build: .
6       tty: true
7       command: python3.9 main.py
```


> 1行目

気にしないでください。詳細を知りたいなら[こちら](https://google.com/search?q=docker+version+とは)

> 2行目

気にしない

> 3行目

dockerのコンテナ名の指定？だったはずです。好きなように決めてください。

> ４行目

ここでコンテナ名を新たに？決めてます。

> 5行目

buildするときになんちゃらのやつです、多分

> 6行目

ずっと動き続けるようにします。PC閉じたら止まりますよ。

> ７行目

`python3.9 main.py`というコマンドを実行させてます。
