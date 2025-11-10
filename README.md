# sample-python-gemini

PythonでGemini APIを呼び出すサンプルです。

このリポジトリをcloneし、`.env.sample` をコピーして `.env` ファイルを作成し、内容を書き換えてください。

```
GEMINI_API_KEY=APIキー
```

次に、dockerを使用して起動してください。

```bash
docker compose up
```

APIキーが正しければ、http://localhost:8000 にブラウザでアクセスすると、Geminiからの応答が表示されます。

また、以下のコマンドで、コンテナを起動して中に入り、手動でPythonプログラムを起動することもできます。

```
docker compose run --rm app bash
python test_chat.py
```
