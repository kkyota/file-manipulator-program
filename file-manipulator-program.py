import sys
import os

def reverse(inputpath, outputpath):
    with open(inputpath, 'r') as file:
        content = file.read()
    reversed_content = content[::-1]
    with open(outputpath, 'w') as file:
        file.write(reversed_content)

def copy(inputpath, outputpath):
    with open(inputpath, 'rb') as source_file:
        with open(outputpath, 'wb') as target_file:
            target_file.write(source_file.read())

def duplicate_contents(inputpath, outputpath, n):
    with open(inputpath, 'r') as file:
        content = file.read()
    duplicated_content = content * n
    with open(outputpath, 'w') as file:
        file.write(duplicated_content)

def replace_string(inputpath, needle, newstring):
    with open(inputpath, 'r') as file:
        content = file.read()
    replaced_content = content.replace(needle, newstring)
    with open(inputpath, 'w') as file:
        file.write(replaced_content)

def validate_file_path(file_path):
    if not os.path.exists(file_path):
        print(f"エラー: {file_path} は存在しません")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("エラー: 引数が不足しています")
        sys.exit(1)

    command = sys.argv[1]
    inputpath = sys.argv[2]
    validate_file_path(inputpath)

    if command == 'reverse':
        if len(sys.argv) < 4:
            print("エラー: 出力パスが指定されていません")
            sys.exit(1)
        outputpath = sys.argv[3]
        reverse(inputpath, outputpath)
    elif command == 'copy':
        if len(sys.argv) < 4:
            print("エラー: 出力パスが指定されていません")
            sys.exit(1)
        outputpath = sys.argv[3]
        copy(inputpath, outputpath)
    elif command == 'duplicate-contents':
        if len(sys.argv) < 5:
            print("エラー: 複製回数が指定されていません")
            sys.exit(1)
        n = int(sys.argv[3])
        outputpath = sys.argv[4]
        duplicate_contents(inputpath, outputpath, n)
    elif command == 'replace_string':
        if len(sys.argv) < 5:
            print("エラー: 置換文字列が指定されていません")
            sys.exit(1)
        needle = sys.argv[3]
        newstring = sys.argv[4]
        replace_string(inputpath, needle, newstring)
    else:
        print("エラー: 無効なコマンド")
        sys.exit(1)
