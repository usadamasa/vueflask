vueflask
=====================

S3のバケットの状況を確認するSPAをvuejsとflaskで作る

## TODO

- [x] プロジェクトの雛形を作る
    - [x] vue
        ```
        npm install -g vue-cli
        vue init webpack vue
        npm install
        npm run dev
        ```
    - [x] flask
        ```
        mkdir -p backend/python
        cd backend/python
        pipenv install
        pipenv install Flask
        ```
    - [x] つなぎこみ
- [ ] デプロイできるようにする
    - [x] docker-compose
    - [x] nginx
    - [ ] 動作確認
- [ ] s3に接続する
- [ ] ファイル一覧を取得する
- [ ] vueでテーブル?表示する

## Reference
* [Vue.js(vue-cli)とFlaskを使って簡易アプリを作成する【前半 - フロントエンド編】](https://qiita.com/mitch0807/items/2a93d93adbf6b5fc445c)
* [Vue.js(vue-cli)とFlaskを使って簡易アプリを作成する【後半 - サーバーサイド編】](https://qiita.com/mitch0807/items/c2e84beee6c9a61e86cd)
* [Vue.jsとFlaskのDocker環境を構築してみた](https://qiita.com/kouchanne/items/417bad58633cc4262012)

