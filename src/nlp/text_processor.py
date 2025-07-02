import spacy
from typing import List, Dict
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

class TextProcessor:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_lg')
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        self.embeddings = HuggingFaceEmbeddings()
        self.vector_store = None

    def process_text(self, text: str) -> Dict:
        doc = self.nlp(text)
        
        entities = []
        for ent in doc.ents:
            entities.append({
                'text': ent.text,
                'label': ent.label_,
                'start': ent.start_char,
                'end': ent.end_char
            })
        
        return {
            'entities': entities,
            'tokens': [token.text for token in doc],
            'sentences': [sent.text for sent in doc.sents]
        }

    def create_vector_store(self, texts: List[str]):
        chunks = self.text_splitter.split_text('\n'.join(texts))
        self.vector_store = Chroma.from_texts(
            texts=chunks,
            embedding=self.embeddings
        )

    def search_similar(self, query: str, k: int = 5) -> List[str]:
        if not self.vector_store:
            raise ValueError("Vector store not initialized")
        
        results = self.vector_store.similarity_search(query, k=k)
        return [doc.page_content for doc in results]