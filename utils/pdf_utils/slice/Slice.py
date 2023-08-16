# 作者:lxb
from pdfminer.layout import LTText


class Slice:
    _text: str

    def __init__(self, text_box: LTText):
        self._text = text_box.get_text()

    def get_text(self):
        return self._text

    def __str__(self):
        return self._text

    def __len__(self):
        return len(self._text)
