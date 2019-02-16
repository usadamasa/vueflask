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
    - [ ] つなぎこみ
- [ ] デプロイできるようにする
    - [ ] docker-compose
    - [ ] nginx
- [ ] s3に接続する
- [ ] ファイル一覧を取得する
- [ ] vueでテーブル?表示する
