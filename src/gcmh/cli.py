import pyperclip
import sys


PROMPT_TEMPLATE = (
    "### Instruction\n"
    "Create an English git commit message based on the following task description.\n"
    "Please follow the Conventional Commits format (e.g., feat, fix, docs, style, refactor, chore).\n\n"
    "Output Format:\n"
    "git commit -m \"[message]\"\n"
    "### Task Description\n"
    "{user_input}"
)

def get_user_input():
    """ユーザーからの入力を受け取る関数"""
    print(">> 作業内容を入力してください（終了するには Ctrl+C）：")
    
    while True:
        try:
            user_input = input("Input: ").strip()
            if user_input:
                return user_input
            print(">> 作業内容が空です。もう一度入力してください。")
        except KeyboardInterrupt:
            print("\n>> プログラムを終了します。")
            sys.exit(0)

def main():
    user_input = get_user_input()

    message = PROMPT_TEMPLATE.format(user_input=user_input)

    try:
        pyperclip.copy(message)
        print("-" * 30)
        print(">> 成功: プロンプトをクリップボードにコピーしました！")
        print(">> チャットAI（ChatGPTやClaudeなど）に貼り付けてください。")
        print("-" * 30)
        print(f"(コピーされた内容のプレビュー):\n{message[:100]}...")
    except pyperclip.PyperclipException:
        print(">> エラー: クリップボードへのコピーに失敗しました。")
        print(">> 以下の内容を手動でコピーしてください：")
        print(message)


if __name__ == "__main__":
    main()