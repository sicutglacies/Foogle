from pathlib import Path

class Config:
    # Loader config
    ALLOWED_FILES_FORMAT = {'.txt', '.doc', '.docx', '.pdf'}
    TEXT_LOADER_KWARGS = {'autodetect_encoding': True}

    # Splitter config
    CHUNK_SIZE: int = 300
    CHUNK_OVERLAP: int = 50

    # Retriever parameters
    K_TO_RETRIEVE = 5

    # Files path
    FILES_PATH: Path = Path('data/')


config = Config()
