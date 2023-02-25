BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    syn = ['.', ',', '!', '?', ':', ';']
    many = text[start:(start + size + 1)]
    if many.endswith('.'):
        part = text[start:(start + size - 2)]
    else:
        part = text[start:(start + size)]

    while part[-1] not in syn:
        part = part[:-1]

    return part, len(part)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as file:
        text = file.read()
    st = 0
    for i in range(1, (len(text)//PAGE_SIZE + 2)):
        tup = _get_part_text(text, st, PAGE_SIZE)
        st += tup[1]
        page = tup[0].lstrip(' \n\t')
        book[i] = page

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
print(book)
