import sys
import markdown

# 判定ロジック定義
def main():

    with open(sys.argv[1], encoding="utf-8") as f1:
        with open(sys.argv[2], "w", encoding="utf-8") as f2:
            f2.write(markdown.markdown(f1.read()))


if __name__ == "__main__":
    main()


# python3 md_to_html.py <input.md> <output.html>