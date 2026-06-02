from pathlib import Path


def read_text_file(file_path: str) -> str:
    """
    读取一个文本文件，并返回里面的全部内容。
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")


def write_text_file(file_path: str, content: str) -> None:
    """
    把 content 写入到指定文件。
    如果上级文件夹不存在，会自动创建。
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")