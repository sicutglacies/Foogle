from pathlib import Path


class Config:
    # Loader config
    ALLOWED_FILES_FORMAT = {'.txt', '.doc', '.docx', '.pdf', ".csv", '.rtf', '.rst', '.tsv', '.ppt', '.pptx', ".xlsx", '.epub', '.md'}
    TEXT_LOADER_KWARGS = {'autodetect_encoding': True}

    # Splitter config
    CHUNK_SIZE: int = 400
    CHUNK_OVERLAP: int = 50

    # Retriever parameters
    K_TO_RETRIEVE = 5

    # Files path
    FILES_PATH: Path = Path('data')


config = Config()
