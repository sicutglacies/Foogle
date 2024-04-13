from pathlib import Path


class Config:
    # Loader config
    ALLOWED_FILES_FORMAT = {'.txt', '.doc', '.docx', '.pdf', ".csv", '.rtf', '.rst', '.tsv', '.ppt', '.pptx', ".xlsx", '.epub', '.md'}
    TEXT_LOADER_KWARGS = {'autodetect_encoding': True}

    # Splitter config
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

    # Retriever parameters
    K_TO_RETRIEVE: int = 10
    K_TO_SHOW: int = 5

    # Files path
    FILES_PATH: Path = Path('data')

    # PDF loading strategy
    PDF_STRATEGY: str = 'fast' # change to hi_res for image-based pdfs


config = Config()
