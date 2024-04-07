from pathlib import Path


class Config:
    # Loader config
    ALLOWED_FILES_FORMAT = {'.txt', '.doc', '.docx', '.pdf', ".csv", '.rtf', '.rst', '.tsv', '.ppt', '.pptx', ".xlsx", '.epub', '.md'}
    TEXT_LOADER_KWARGS = {'autodetect_encoding': True}

    # Splitter config
    CHUNK_SIZE: int = 200
    CHUNK_OVERLAP: int = 30

    # Retriever parameters
    K_TO_RETRIEVE = 3

    # Files path
    FILES_PATH: Path = Path('data')


config = Config()
