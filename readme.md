# discord-channel-sync

複数のDiscordチャンネルでメッセージを同期させるツール

## 環境
- Python 3.8 or higher

## 導入
1. configファイルを作成する．
    ```sh
    cp config.yaml.sample config.yaml
    ```

1. config.yamlにBotのtokenを記述する．

1. config.yamlにチャンネルIDとwebhookのURLを記述する．(チャンネルを増減させたいときは項目の数を増減させる．)

1. ライブラリをインストールする
    ```sh
    pip install install -U py-cord pyyaml aiohttp
    ```

1. 実行する
    ```sh
    ch
    ./app.py
    ```
