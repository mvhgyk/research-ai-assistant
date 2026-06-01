from pathlib import Path


def write_markdown(path: str | Path, title: str, body: str) -> Path:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"# {title}\n\n{body}\n", encoding="utf-8")
    return output_path
