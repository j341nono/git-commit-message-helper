# Git Commit Message Helper

生成AI用のプロンプトを自動生成するツールです．日本語の作業内容を入力すると，Git のコミットメッセージや Pull Request 用の英語プロンプトを生成し，クリップボードにコピーします．

![Usage Demo](assets/usage.gif)

## 特徴

- 日本語の作業内容から，生成AI用の英語プロンプトを自動生成
- コミットメッセージ用・Pull Request 用の2種類のプロンプトに対応
- 生成したプロンプトを自動的にクリップボードにコピー
- Conventional Commits 形式を指定したプロンプト
- ChatGPT や Claude などにそのまま貼り付けて使用可能

## このツールができること

このツールは**プロンプト生成ツール**です：

✅ 日本語の作業内容 → 英語の指示が含まれたプロンプトを生成  
✅ 生成したプロンプトをクリップボードにコピー  

❌ このツール自体がコミットメッセージを生成するわけではありません  
❌ AI 機能は含まれていません  

生成されたプロンプトを ChatGPT や Claude などの生成AI に貼り付けることで，適切なコミットメッセージや PR 文を作成できます．

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

### コミットメッセージ用プロンプトの生成

**対話モード：**
```bash
gcmh
```
実行後，作業内容の入力を求められます．

**引数で直接指定：**
```bash
gcmh ユーザー認証機能を追加した
```

**出力されるプロンプトの例：**
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

このプロンプトを ChatGPT や Claude に貼り付けると，AI が英語のコミットメッセージを生成します．

### Pull Request 用プロンプトの生成

**対話モード：**
```bash
gcmh --pr
```
実行後，作業内容の入力を求められます．

**引数で直接指定：**
```bash
gcmh --pr APIのレート制限機能を実装した
```

または，作業内容を先に指定することも可能：
```bash
gcmh APIのレート制限機能を実装した --pr
```

**出力されるプロンプトの例：**
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

このプロンプトを ChatGPT や Claude に貼り付けると，AI が英語の PR タイトルと説明文を生成します．

## ワークフロー

1. `gcmh` コマンドを実行して作業内容を日本語で入力
2. 生成されたプロンプトが自動的にクリップボードにコピーされる
3. ChatGPT，Claude などの生成AI に貼り付け
4. AI が生成した英語のコミットメッセージや PR 文を使用

## オプション

| オプション | 説明 |
|-----------|------|
| `message` | 作業内容（省略時は対話モード） |
| `--pr` | Pull Request 用のプロンプトを生成 |
| `-h, --help` | ヘルプを表示 |

## ライセンス

MIT License