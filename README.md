# Foogle
Educational project for UrFU Python class


## FAQ

- Supported formats: '.txt', '.doc', '.docx', '.pdf', '.csv', '.rtf', '.rst', '.tsv', '.ppt', '.pptx', '.xlsx', '.epub', '.md'

- BM25 search enhancement via preprocessing availiable for ENG and RUS

- OCR for image-pdfs only availiable for ENG


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
