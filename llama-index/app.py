import os
import hashlib
import json
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.schema import Document
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PDFReader

# Configura LLM e embeddings
Settings.llm = Ollama(model="llama3")
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

data_dir = "data"
storage_dir = "storage"

# Usa leitor para PDF
reader = SimpleDirectoryReader(
    data_dir,
    recursive=True,
    file_extractor={".pdf": PDFReader()},
)

# Gera doc ID baseado no caminho do arquivo
def generate_docs_with_id():
    docs_raw = reader.load_data()
    docs = []
    for doc in docs_raw:
        file_path = doc.metadata.get("file_path") or doc.metadata.get("filename", "")
        doc_id = hashlib.md5(file_path.encode()).hexdigest()
        docs.append(Document(text=doc.text, id_=doc_id, metadata=doc.metadata))
    return docs

# Carrega ou cria índice
if os.path.isdir(storage_dir) and os.listdir(storage_dir):
    print("🔁 Carregando índice existente...")
    storage_ctx = StorageContext.from_defaults(persist_dir=storage_dir)
    index = load_index_from_storage(storage_ctx)
else:
    print("🆕 Criando novo índice...")
    docs = generate_docs_with_id()
    index = VectorStoreIndex.from_documents(docs)
    index.storage_context.persist()

# Atualiza o índice com novos arquivos
docs = generate_docs_with_id()
updated = index.refresh(documents=docs)
if any(updated):
    print(f"🔄 Atualizado/Inserido docs: {sum(updated)}")
    index.storage_context.persist()
else:
    print("✅ Sem alterações no índice.")

# Prompt e resposta
prompt = 'Quem toma café? Qual a quantidade de café ele toma? Me fale um pouco sobre o café presente nos documentos? Responda em português brasileiro.'
qe = index.as_query_engine()
resp = qe.query(prompt)

# Output formatado
print(json.dumps({
    "query": prompt,
    "response": str(resp)
}, ensure_ascii=False, indent=2))
