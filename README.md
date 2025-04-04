# 🤖 LeetCode GPT Solver (Stealth Mode)

Este é um assistente inteligente que **lê problemas do LeetCode diretamente da sua tela** e gera uma **solução automática usando a OpenAI (GPT-4)** — tudo isso rodando em **modo invisível**, sem mostrar nada na tela, nem durante espelhamento.

---

## 🚀 Funcionalidades

✅ Ativado por atalho de teclado (`Ctrl + Alt + L`)  
✅ Detecta se você está com uma aba do LeetCode ativa  
✅ Copia o problema da tela  
✅ Envia para o ChatGPT (usando API da OpenAI)  
✅ Copia a resposta para o clipboard  
✅ Funciona totalmente em segundo plano  
✅ Invisível mesmo em gravação de tela ou espelhamento  
✅ Compatível com **Windows**

---

## 🧠 Requisitos

- Python 3.8+
- Conta na OpenAI com chave de API válida

---

## 📦 Instalação

1. **Clone ou baixe o repositório:**



Crie um ambiente virtual (opcional):

bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Adicione sua chave da OpenAI em gpt_solver.py:

python
Copiar
Editar
openai.api_key = "SUA_CHAVE_AQUI"
🧪 Uso
Abra o LeetCode em qualquer navegador (Chrome recomendado)

Acesse um problema (ex: https://leetcode.com/problems/two-sum)

Execute o script:

bash

python main.py
Pressione Ctrl + Alt + L

A solução será copiada automaticamente para o seu clipboard

Cole a resposta onde quiser com Ctrl + V ✅

🛠️ Compilar para .EXE (modo totalmente invisível)
Se quiser gerar um .exe para rodar sem console visível:

bash

pip install pyinstaller
pyinstaller --noconsole --onefile main.py
O executável será criado na pasta dist/.

