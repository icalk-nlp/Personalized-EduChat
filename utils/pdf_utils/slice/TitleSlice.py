# 作者:lxb
from pdfminer.layout import LTText

from utils.pdf_utils.slice.Slice import Slice


class TitleSlice(Slice):

    def __init__(self, text_box: LTText, lever: int):
        super().__init__(text_box)
        self._lever = lever

    def get_lever(self):
        return self._lever if self._lever is not None else 0

    def __str__(self):
        return self._text

    def merge(self, another):
        self._text += another.get_text()
