import re


def clean_cv_underlines_with_space(text: str) -> str:
    if not isinstance(text, str) or text == '':
        return ''

    text = re.sub(r'\-', " – ", text)
    text = re.sub(r'\–', " – ", text)
    text = re.sub(r'\  -  ', " – ", text)
    text = re.sub(r'\  –  ', " – ", text)
    text = re.sub(r'\   -   ', " – ", text)
    text = re.sub(r'\   –   ', " – ", text)
    return text


def clean_cv_paratenses_with_space(text: str) -> str:
    if not isinstance(text, str) or text == '':
        return ''

    text = re.sub(r'\)', ") ", text)
    text = re.sub(r'\(', " (", text)
    text = re.sub(r'\)  ', ") ", text)
    text = re.sub(r'  \(', " (", text)
    text = re.sub(r'\)   ', ") ", text)
    text = re.sub(r'   \(', " (", text)
    return text

