from PyPDF2 import PdfReader


def test_pdf_check_number_of_pages():
    # Проверяем сколько страниц в тексте
    reader = PdfReader('resources/pytest.pdf')
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    # Проверяем, что в тексте есть текст который нам нужен
    page = reader.pages[0]
    text = page.extract_text()
    print(text)
    assert "holger krekel, trainer and consultant" in text


