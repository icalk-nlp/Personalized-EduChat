# 作者:lxb

from utils.pdf_utils.slice.Slice import Slice


class ContentSlice(Slice):
    # 判断是否要合并内容content
    def should_merge(self, another):
        this_text = self.get_text().strip()
        that_text = another.get_text().strip()

        if this_text.endswith(('.','。','!','?','...')) or that_text.startswith(('[','(','【','（')):
            return False
        return True

    # 合并内容
    def merge(self, another):
        self._text += another.get_text()



    def __str__(self):
        return self._text
