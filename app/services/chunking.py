from fastapi import Request
from kiwipiepy import Kiwi
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunking(self, text, request:Request):
        # 형태소 분해 전처리 - kiwipiepy
        kiwi = Kiwi()

        result = kiwi.split_into_sents(text)

        sent_result = [s.text.strip() for s in result if s.text.strip()]
        normalized = "\n".join(sent_result)

        # chunking 준비 - langchain-text-splitters
        tokenizer = request.app.state.tokenizer

        splitter = RecursiveCharacterTextSplitter(
            tokenizer=tokenizer,
            chunk_size=300,
            chunk_overlap=60
        )

        chunked = splitter(normalized)

        return chunked