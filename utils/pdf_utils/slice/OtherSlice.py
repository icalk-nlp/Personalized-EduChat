# 作者:lxb
from utils.pdf_utils.slice.Slice import Slice


class OtherSlice(Slice):

    def __str__(self):
        return self._text

    def merge(self, another):
        self._text += another.get_text()
