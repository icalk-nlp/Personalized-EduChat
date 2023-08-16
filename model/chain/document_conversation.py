# 作者:lxb
import pprint
from pathlib import Path
from typing import Any, Optional, Dict

from langchain import PromptTemplate, LLMChain, BasePromptTemplate, OpenAI
from langchain.callbacks.base import Callbacks
from langchain.chains.conversational_retrieval.base import BaseConversationalRetrievalChain, \
    ConversationalRetrievalChain
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import BaseRetriever
from langchain.chains import StuffDocumentsChain, RetrievalQA

from document_store.document import Document
from document_store.faiss_store import FaissStore
from model.Educhat import Educhat

from typing import Any, Dict, List, Optional

from pydantic import Extra

from langchain.schema.language_model import BaseLanguageModel
from langchain.callbacks.manager import (
    AsyncCallbackManagerForChainRun,
    CallbackManagerForChainRun,
)
from langchain.chains.base import Chain
from langchain.prompts.base import BasePromptTemplate

from prompt_template.prompt_template import CONDENSE_QUESTION_PROMPT, answer_prompt

if __name__ == '__main__':
    llm = Educhat()
    faiss_store = FaissStore(Path(r'D:\pycharm_work\EduChat\test2.pdf'))
    from langchain.memory import ConversationBufferMemory

    #     condense_question_template = """根据所给的历史聊天记录和后续提问，请你在保持其原意不变的前提下，将其转化为一个独立的问题，并用其文字的原始语言进行表述，即中文。
    # 你需要先判断后续提问与聊天记录是否有关，如果后续提问与聊天记录无关，说明这是一个新的提问，后续提问即为独立问题。
    # 如果后续提问与聊天记录有关，说明这是一个追问，需要先转化为独立问题。
    # 聊天记录：
    # {chat_history}
    # 后续提问：{question}
    # 独立问题："""
    #     condense_question_prompt = PromptTemplate.from_template(condense_question_template)

    # question_generator_chain = LLMChain(llm=llm, prompt=condense_question_prompt)
    #
    # document_prompt = PromptTemplate(
    #     input_variables=["page_content"],
    #     template="{page_content}"
    # )
    #
    # document_variable_name = 'context'
    # context_prompt = PromptTemplate.from_template(
    #     "请你总结这个内容: {context}"
    # )
    # llm_chain = LLMChain(llm=llm, prompt=context_prompt)
    # combine_docs_chain = StuffDocumentsChain(llm_chain=llm_chain, document_prompt=document_prompt,
    #                                          document_variable_name=document_variable_name)

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

        # content = faiss_store.search(query)
        # docs = faiss_store.get_relevant_documents(query)
        # result=chain.run(input_documents=docs, question=query, return_only_outputs=True)
        # print(result)

        # qa = DocumentConversationalRetrievalChain.from_llm(
        #     llm=llm,
        #     combine_docs_chain=combine_docs_chain,
        #     retriever=faiss_store.get_retriever(),
        #     question_generator=question_generator_chain,
        #     max_tokens_limit=2048,
        #     memory=memory,
        # )
        # result = qa({"question": query})
        # print(result["answer"])

        # chain = ConversationalRetrievalChain(
        #     combine_docs_chain=combine_docs_chain,
        #     retriever=faiss_store.get_retriever(),
        #     question_generator=question_generator_chain,
        #     max_tokens_limit=2048,
        #     memory=memory,
        # )
        # result = chain({"question": query})
        # print(result["answer"])
