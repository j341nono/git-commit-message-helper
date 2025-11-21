import pyperclip
import sys
import argparse


TEMPLATE_COMMIT = (
    "### Instruction\n"
    "Create an English git commit message based on the following task description.\n"
    "Please follow the Conventional Commits format (e.g., feat, fix, docs, style, refactor, chore).\n\n"
    "Output Format:\n"
    "git commit -m \"[message]\"\n\n"
    "### Task Description\n"
    "{user_input}"
)

TEMPLATE_PR = (
    "### Instruction\n"
    "Create a Pull Request (PR) title and description in English based on the following task description.\n"
    "The title should be concise, and the description should explain 'What' was done and 'Why'.\n\n"
    "Output Format:\n"
    "## PR Title\n"
    "[Title]\n\n"
    "## PR Description\n"
    "[Description]\n\n"
    "### Task Description\n"
    "{user_input}"
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate AI prompts for Git Commits or Pull Requests.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        'message', 
        nargs='*', 
        help='Task description (if omitted, interactive mode starts)'
    )
    
    parser.add_argument(
        '--pr', 
        action='store_true', 
        help='Generate a prompt for Pull Request (Title & Body) instead of a commit message'
    )

    return parser.parse_args()


def get_interactive_input():
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
    args = parse_args()

    if args.message:
        user_input = " ".join(args.message)
    else:
        mode_str = "Pull Request" if args.pr else "Commit Message"
        print(f"[{mode_str} Mode]")
        user_input = get_interactive_input()

    if args.pr:
        prompt = TEMPLATE_PR.format(user_input=user_input)
        mode_name = "Pull Request用プロンプト"
    else:
        prompt = TEMPLATE_COMMIT.format(user_input=user_input)
        mode_name = "Commit用プロンプト"

    try:
        pyperclip.copy(prompt)
        print("-" * 30)
        print(f">> 成功: {mode_name}をクリップボードにコピーしました！")
        print(">> チャットAI（ChatGPTやClaudeなど）に貼り付けてください。")
        print("-" * 30)
        preview = '\n'.join(prompt.split('\n')[:10]) 
        print(f"(Preview):\n{preview}...\n")
        
    except pyperclip.PyperclipException:
        print(">> エラー: クリップボードへのコピーに失敗しました。")
        print(prompt)


if __name__ == "__main__":
    main()