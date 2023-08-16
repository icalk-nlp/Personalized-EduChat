# 作者:lxb
import pprint
from pathlib import Path
from langchain.chains.question_answering import load_qa_chain

from document_store.faiss_store import FaissStore
from model.Educhat import Educhat

from prompt_template.prompt_template import CONDENSE_QUESTION_PROMPT, answer_prompt

if __name__ == '__main__':
    llm = Educhat()
    faiss_store = FaissStore(Path(r'D:\pycharm_work\EduChat\test2.pdf'))
    from langchain.memory import ConversationBufferMemory
    memory = ConversationBufferMemory(memory_key="chat_history",
                                      input_key="human_input",
                                      return_messages=True)
    chain = load_qa_chain(
        llm, chain_type="stuff", memory=memory, prompt=answer_prompt, verbose=True
    )
    while True:
        query = input("请输入你的问题：")
        docs = faiss_store.get_relevant_documents(query)
        result = chain({"input_documents": docs, "human_input": query}, return_only_outputs=True)
        pprint.pprint(chain.memory.buffer)
