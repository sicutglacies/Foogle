import time


# Streamed response emulator
def response_generator(scores, responses):
    text = "# Answers: \n"

    for n, (score, response) in enumerate(zip(scores, responses)):
        text += f'{n+1}. Relevancy: {round(score, 4)} \n\n'
        text += f"{' '.join(response.page_content.split())} \n\n"
    
    for char in text:
        yield char
        time.sleep(0.01)
