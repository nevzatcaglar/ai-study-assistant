import pytest
from pathlib import Path

from tools.file_reader import FileReaderTool


def test_read_txt_file(tmp_path):
    sample_file = tmp_path / "sample.txt"
    sample_file.write_text("This is a sample study file.", encoding="utf-8")

    tool = FileReaderTool()
    result = tool.read(str(sample_file))

    assert result == "This is a sample study file."


def test_file_not_found():
    tool = FileReaderTool()

    with pytest.raises(FileNotFoundError):
        tool.read("missing_file.txt")


def test_unsupported_file_type(tmp_path):
    sample_file = tmp_path / "sample.pdf"
    sample_file.write_text("Fake PDF content", encoding="utf-8")

    tool = FileReaderTool()

    with pytest.raises(ValueError):
        tool.read(str(sample_file))
