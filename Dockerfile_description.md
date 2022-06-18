```Dockerfile
1   FROM python:3.9.5
2   WORKDIR /raitochinyu/
3
4   RUN apt-get update
5   ENV LANG ja_JP.UTF-8
6   ENV LANGUAGE ja_JP:ja
7   ENV LC_ALL ja_JP.UTF-8
8
9   COPY .env /.env
13  COPY requirements.txt /raitochinyu/
14  RUN pip install --upgrade pip
15  RUN pip install -r /raitochinyu/requirements.txt
16
17  COPY main.py /raitochinyu/
```


> 1行目

pythonのバージョンを指定してます。必ずしもそのバージョンをPCに入れないといけないわけではないので大丈夫です。

> 2行目

忘れた。好きなような名前にすればなんとかなるでしょ（適当）

> 4~7行目

気にしなくていいい。

> 6~13行目
> 
`.env`と`requirement.txt`を`/raitochinyu/`にコピってる。必要なファイルは必ずコピろう

> 14~15行目

14：`pipをアップグレードさせてる`
<br>
15：`requirements.txt`に書いてるものをインストールする。

> 17行目

6~7行目と同様。`main.py`をコピってる
