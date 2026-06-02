from file_utils import read_text_file, write_text_file
from markdown_writer import build_paper_note


def main():
    input_path = "data/papers/test_abstract.txt"
    output_path = "data/outputs/test_paper_note.md"

    abstract = read_text_file(input_path)

    note = build_paper_note(
        title="Test Paper",
        abstract=abstract
    )

    write_text_file(output_path, note)

    print(f"Markdown note generated: {output_path}")


if __name__ == "__main__":
    main()