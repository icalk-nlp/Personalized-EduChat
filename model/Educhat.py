from typing import Any, Optional, List, Mapping, Dict
import requests
import json
from pathlib import Path
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

from config import Config
from document_store.faiss_store import FaissStore


class Educhat(LLM):
    _url: str = Config().get("SECRET_KEY")
    max_tokens: Optional[int]
    temperature: Optional[float]
    top_p: Optional[float]
    prompt: Optional[str]


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.top_p = kwargs.get('top_p', 0.7)
        self.temperature = kwargs.get('temperature', 0.7)
        self.max_tokens = kwargs.get('max_tokens', 2048)

    @property
    def _llm_type(self) -> str:
        return "educhat"

    def _call(self, prompt, stop: Optional[List[str]] = None, run_manager: Optional[CallbackManagerForLLMRun] = None,
              *args, **kwargs):
        headers = {'Content-Type': 'application/json'}
        messages = [{'role': 'user', 'content': prompt}]
        json = {
            'messages': messages,
            'max_tokens': self.max_tokens,
            'temperature': self.temperature,
            'top_p': self.top_p
        }
        response = requests.post(self._url, headers=headers, json=json)
        response.raise_for_status()
        return response.json()['response']

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {
            "top_p": self.top_p,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }

if __name__ == '__main__':
    llm = Educhat()
    # llm.predict_messages([HumanMessage(content="你好")])
    faiss_store = FaissStore(Path(r'D:\pycharm_work\EduChat\test1.pdf'))
    while True:
        query = input("请输入你的问题：")
        docss=faiss_store.get_relevant_documents(query)
        docs = faiss_store.search(query)
        prompt = f"""你现在是一位优秀的语文教师，你需要用你专业的知识认真分析你的学生提出的问题:“{query}”，然后进行详细并通俗易懂地讲解。
可供你参考的资料如下:
'''
{docs}
'''
如果无法从中得到答案，请说“根据已知信息无法回答该问题”，不允许在答案中添加编造信息。"""
        response = llm(prompt)
        print(response)

