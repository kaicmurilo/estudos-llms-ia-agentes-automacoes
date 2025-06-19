# 📄 LlamaIndex com Ollama (Local LLM)

Este projeto utiliza o [LlamaIndex](https://llamaindex.ai) com o modelo local via [Ollama](https://ollama.com/) para realizar **indexação inteligente de documentos locais** e permitir **consultas em linguagem natural**, com suporte a arquivos `.pdf`.

---

## ✅ Funcionalidades

- Suporte a documentos `.pdf` (e expansível para `.txt`, `.docx`, etc.)
- Indexação persistente com verificação de arquivos novos
- LLM local usando Ollama (sem depender da OpenAI)
- Consulta com respostas estruturadas em JSON
- Detecção automática de documentos alterados ou adicionados

---

## 🚀 Como rodar

### 1. Instale o [Ollama](https://ollama.com/)
> Ex: `ollama run llama3`

### 2. Clone o repositório e crie o ambiente

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Crie a pasta data/ e adicione seus arquivos

```bash
mkdir data
# coloque seus PDFs ou outros arquivos aqui
```

4. Execute o app

```bash
python app.py
```

🧠 Exemplo de Consulta

```bash
{
  "query": "Quem toma café? Qual a quantidade de café ele toma?",
  "response": "Kaic toma de 3 a 4 copos por dia..."
}
```

📦 Requisitos

Python 3.10+

Ollama (com modelo baixado, ex: llama3)

Linux/MacOS (ou WSL no Windows)


✍️ Expansões futuras

Suporte a .docx, .csv, .md

UI com Streamlit

Cache de respostas para acelerar consultas repetidas

