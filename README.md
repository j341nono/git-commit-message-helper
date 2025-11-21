# Git Commit Message Helper

生成AI を活用して，Git のコミットメッセージや Pull Request の文章を簡単に生成するためのツールです

## 特徴

- 日本語の作業内容から英語のコミットメッセージを生成
- Pull Request のタイトルと説明文も生成可能
- 生成したプロンプトを自動的にクリップボードにコピー
- Conventional Commits 形式に対応
- ChatGPT や Claude などの AI チャットに貼り付けるだけで使用可能

## インストール

### 自動セットアップ（推奨）

以下のコマンドを実行するだけで，必要な環境を自動的にセットアップできます：

```bash
curl -sSL https://raw.githubusercontent.com/j341nono/git-commit-message-helper/main/scripts/setup.sh | bash
```

このスクリプトは以下を自動的に行います：
- `uv` のインストール（未インストールの場合）
- 必要な依存関係のインストール
- コマンドエイリアスの設定

### 手動インストール

1. このリポジトリをクローン：
```bash
git clone https://github.com/j341nono/git-commit-message-helper.git
cd git-commit-message-helper
```

2. 依存関係をインストール：
```bash
uv sync
```

3. ツールをインストール
```bash
uv tool install -e .
```

## 使い方

### コミットメッセージの生成

**対話モード：**
```bash
gcmh
```

生成されるプロンプト例：
```
### Instruction
Create an English git commit message based on the following task description.
Please follow the Conventional Commits format (e.g., feat, fix, docs, style, refactor, chore).

Output Format:
git add [file_name]
git commit -m "[message]"

### Task Description
ユーザー認証機能を追加した
```

### Pull Request の生成

**対話モード：**
```bash
gcmh --pr
```

生成されるプロンプト例：
```
### Instruction
Create a Pull Request (PR) title and description in English based on the following task description.
The title should be concise, and the description should explain 'What' was done and 'Why'.

Output Format:
## PR Title
[Title]

## PR Description
[Description]

### Task Description
APIのレート制限機能を実装した
```

## ワークフロー

1. ツールを実行して作業内容を入力
2. 生成されたプロンプトが自動的にクリップボードにコピーされる
3. ChatGPT，Claude などの AI チャットに貼り付け
4. AI が生成した英語のコミットメッセージや PR 文を使用

## オプション

| オプション | 説明 |
|-----------|------|
| `message` | 作業内容（省略時は対話モード） |
| `--pr` | Pull Request 用のプロンプトを生成 |
| `-h, --help` | ヘルプを表示 |


## ライセンス

MIT License
