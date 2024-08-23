import os


def list_dir(root, indentation=2, show_hidden=False, level=0, content=''):
    folders = []

    content += f'{" " * level * indentation}{os.path.basename(root)}/\n'

    for item in os.listdir(root):
        if item.startswith('.') and not show_hidden:
            continue

        path = os.path.join(root, item)

        if os.path.isdir(path):
            folders.append(path)
        else:
            content += f'{" " * (level + 1) * indentation}{item}\n'

    for folder in folders:
        content = list_dir(folder, indentation, show_hidden, level + 1, content)

    return content


def print_content(root, indentation=2, show_hidden=False):
    content = list_dir(root, indentation, show_hidden)
    print(content)


if __name__ == '__main__':
    print_content('/home/viniciuspm/Desenvolvimento/Projects/my_game')
