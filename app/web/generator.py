import time
from pathlib import PosixPath


def posix_to_string(pos_path: PosixPath) -> str:
    return '/'.join(str(pos_path).split('/')[2:])

# Streamed response emulator
def response_generator(scores, responses):
    text = "# Answers: \n"
    no_answers = True

    for n, (score, response) in enumerate(zip(scores, responses)):
        if score != 0:
            text += f'{n+1}. Relevancy: {round(score, 4)} \n\n'
            text += f"{' '.join(response.metadata['original_text'].split())} \n\n"
            text += f'Source: {posix_to_string(response.metadata["source"])} \n\n'
            no_answers = False

    if no_answers:
        text += 'No information found'
    
    for char in text:
        yield char
        time.sleep(0.01)
