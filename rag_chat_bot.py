import os

from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain.docstore.document import Document
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from Control.models import Info


class RAGChatBot:
    def __init__(self, model_name: str = "gpt-4o"):
        # API kalitini yuklash
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")

        # LLM va embedding
        self.embeddings = OpenAIEmbeddings(openai_api_key=self.api_key)
        self.llm = ChatOpenAI(openai_api_key=self.api_key, model_name=model_name)

        # Kontekstni yuklash va bo'lish
        self.documents = self._load_and_split_text()

        # FAISS vektor bazasini yaratish
        self.vectorstore = FAISS.from_documents(self.documents, self.embeddings)

        # RetrievalQA zanjirini tayyorlash
        self.qa = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(),
            chain_type="stuff"
        )

    @staticmethod
    def _load_and_split_text():
        raw_text = Info.objects.get_texts()
        if not raw_text:
            raw_text = "Barchasini mukammal bajar!"
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        texts = splitter.split_text(raw_text)
        return [Document(page_content=t) for t in texts]

    def ask(self, question_text: str) -> str:
        return self.qa.run(question_text)


if __name__ == '__main__':
    bot = RAGChatBot()

    while True:
        question = input("\n❓ Savolingiz: ")
        if question.lower() in ["exit", "quit", "stop"]:
            print("✅ Dasturdan chiqildi.")
            break
        answer = bot.ask(question)
        print("💬 Javob:", answer)
