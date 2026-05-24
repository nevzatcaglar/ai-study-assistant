from pathlib import Path


class FileReaderTool:
    """
    Tool for reading input files.

    This tool currently supports .txt files. The design allows future extension
    for PDF or other document formats.
    """

    SUPPORTED_EXTENSIONS = {".txt"}

    def read(self, file_path: str) -> str:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {path.suffix}. "
                f"Supported types: {', '.join(self.SUPPORTED_EXTENSIONS)}"
            )

        return path.read_text(encoding="utf-8")
