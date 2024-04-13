# Foogle
Educational project for UrFU Python class


## FAQ

- Supported formats: '.txt', '.doc', '.docx', '.pdf', '.csv', '.rtf', '.rst', '.tsv', '.ppt', '.pptx', '.xlsx', '.epub', '.md'

- BM25 search enhancement via preprocessing availiable for ENG and RUS

- OCR for image-pdfs only availiable for ENG

## Configuration

Project has several important variables that affect the payload you get. They can be changed in src/config.py  
1. Document parsing
    1. ALLOWED_FILES_FORMAT - formats that can be parsed, consult with unstructed library to add more
    2. CHUNK_SIZE - basically maximum number of characters that you want to get in single response. Affects focument parsing.
    3. CHUNK_OVERLAP - number of characters that can overlap between chunks
    4. PDF_STRATEGY - 'hi-res' uses ocr for detecting doc layout, can extract text from image-based pdfs (only for eng and rather slow). 'fast' extracts text from standard pdfs.
2. Retrieve
    1. K_TO_RETRIEVE - number of chunks to be retrieved. Note that if chunk has zero BM25 score or it doesn't comply with search conditions, it will be retrieved but won't be shown to user. (aka post filtering)
    2. K_TO_SHOW - number of results that comply with search conditions to be shown to the user


## Launch

1. Change volume path in docker-compose to the folder you want to search
2. Run **make build**
3. Run **make run**
4. Go to http://localhost:8501/


## Example usage
1. Entering the query without any parameters  
    Example: Публичное акционерное общество
2. Filtering file type (works with every supported format, multiple formats can be used)  
    Examples:  
    1. Публичное акционерное общество .docx  
    2. Публичное акционерное общество .docx .txt
3. Logic expressions
    Search supports logic expressions using curly parentheses and special symbols - & (and), | (or), ! (not). Spaces between symbols are mandatory.  
    Examples:  
    1. ПАО & МТС
    2. ПАО & МТС & ! АФК
    3. ( Microsoft | AI | Apple ) & subscription
4. Combination  
    Example: ( Microsoft | AI | Apple ) & subscription .pdf
