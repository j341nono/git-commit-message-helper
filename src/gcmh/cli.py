import pyperclip


prompt = (
    "### 指示"
    "以下の作業内容に関しての英語のコミットメッセージを作成してください．\n"
    "出力形式は，以下の形式で出力してください．\n"
    "git add [file_name]\\n\n"
    "git commit -m [message]"
    "\n\n### 作業内容\n"
    "{user_input}"
)

def main():
    print(">> 作業内容を入力してください：")
    user_input = ""
    while not user_input:
        user_input = input()
        user_input = user_input.rstrip()
        if not user_input:
            print(">> 作業内容を入力してください：（空文字や空白のみは不可）")

    message = prompt.format(user_input=user_input)
    pyperclip.copy(message)
    print(f">> プロンプトをクリップボードにコピーしました．")


if __name__ == "__main__":
    main()
