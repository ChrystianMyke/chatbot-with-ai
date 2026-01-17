# 🤖 Chatbot with OpenAI

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-red)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Um chatbot simples e elegante desenvolvido com Streamlit e OpenAI GPT-4.

## 📋 Descrição

Este projeto implementa uma interface de chat interativa que utiliza a API da OpenAI para gerar respostas inteligentes. Ideal para:
- Assistente virtual
- Suporte ao cliente
- Educação e tutoria
- Experimentação com IA

## ✨ Funcionalidades

- ✅ Interface moderna e responsiva
- ✅ Histórico de conversação
- ✅ Integração com GPT-4o
- ✅ Limpar conversa com um clique
- ✅ Contador de mensagens
- ✅ Tratamento de erros
- ✅ Configuração segura via variáveis de ambiente

## 🛠️ Tecnologias

- **Streamlit** - Framework web para Python
- **OpenAI API** - Modelo de linguagem GPT-4
- **Python 3.8+**
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 📦 Instalação

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/chatbot-openai.git
cd chatbot-openai
```

### 2️⃣ Criar Ambiente Virtual

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Chave da API

1. Obtenha sua chave da API em: [OpenAI Platform](https://platform.openai.com/api-keys)

2. Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

3. Edite o arquivo `.env` e adicione sua chave:

```env
OPENAI_API_KEY=sk-proj-sua-chave-aqui
```

⚠️ **IMPORTANTE:** Nunca compartilhe sua chave de API!

## 🚀 Como Usar

### Executar a Aplicação

```bash
streamlit run main.py
```

A aplicação abrirá automaticamente no navegador em: `http://localhost:8501`

### Usar o Chatbot

1. Digite sua mensagem no campo de entrada
2. Pressione Enter ou clique no botão de enviar
3. Aguarde a resposta da IA
4. Continue a conversa naturalmente!

### Limpar Conversa

Clique no botão "🗑️ Limpar Conversa" na barra lateral.

## 📁 Estrutura do Projeto

```
chatbot-openai/
│
├── main.py                 # Aplicação principal
├── requirements.txt        # Dependências Python
├── .env.example           # Template de configuração
├── .env                   # Suas configurações (não versionado)
├── .gitignore             # Arquivos ignorados pelo Git
├── README.md              # Este arquivo
└── venv/                  # Ambiente virtual (não versionado)
```

## ⚙️ Configurações

### Modelos Disponíveis

No arquivo `main.py`, você pode alterar o modelo:

```python
model="gpt-4o"           # GPT-4 Optimized (padrão)
model="gpt-4"            # GPT-4
model="gpt-3.5-turbo"    # GPT-3.5 Turbo (mais barato)
```

### Personalização

Customize a aplicação editando `main.py`:

- **Título da página:** `st.set_page_config(page_title="...")`
- **Ícone:** `page_icon="🤖"`
- **Layout:** `layout="centered"` ou `"wide"`

## 💰 Custos

A API da OpenAI é paga por uso:

- **GPT-4o:** ~$5.00 por 1M tokens de entrada
- **GPT-3.5 Turbo:** ~$0.50 por 1M tokens

Configure limites de gastos em: [OpenAI Usage](https://platform.openai.com/account/usage)

## 🐛 Solução de Problemas

### Erro: "Chave da API não encontrada"

**Solução:**
1. Verifique se o arquivo `.env` existe
2. Confirme que a chave está correta
3. Reinicie a aplicação

### Erro: "Erro ao conectar com OpenAI"

**Possíveis causas:**
- Chave de API inválida
- Sem créditos na conta OpenAI
- Problema de conexão com internet

**Solução:**
1. Verifique sua chave em: https://platform.openai.com/api-keys
2. Confirme se há créditos disponíveis
3. Teste sua conexão

### Erro: "ModuleNotFoundError"

**Solução:**
```bash
# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstalar dependências
pip install -r requirements.txt
```

## 🔒 Segurança

### ⚠️ Nunca faça:
- ❌ Commitar arquivos `.env` ou `chave.py`
- ❌ Compartilhar sua chave de API
- ❌ Expor chaves em código público

### ✅ Sempre faça:
- ✅ Use variáveis de ambiente (`.env`)
- ✅ Adicione `.env` ao `.gitignore`
- ✅ Gere novas chaves se houver exposição
- ✅ Configure limites de gasto na OpenAI

## 📝 Comandos Úteis

```bash
# Ativar ambiente virtual
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# Desativar ambiente virtual
deactivate

# Atualizar dependências
pip install --upgrade -r requirements.txt

# Executar aplicação
streamlit run main.py

# Gerar novo requirements.txt
pip freeze > requirements.txt
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit: `git commit -m 'Adiciona nova funcionalidade'`
4. Push: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Seu Nome**
- GitHub: ChrystianMyke(https://github.com/ChrystianMyke)
- LinkedIn: Chrystian Myke (https://linkedin.com/in/seu-perfil)
- Email: miaymoto13k@gmail.com

## 🙏 Agradecimentos

- [OpenAI](https://openai.com/) - Pela API GPT-4
- [Streamlit](https://streamlit.io/) - Pelo framework web
- Comunidade Python Brasil

## 📞 Suporte

Se encontrar problemas:

1. Verifique a [Documentação do Streamlit](https://docs.streamlit.io/)
2. Consulte a [Documentação da OpenAI](https://platform.openai.com/docs)
3. Abra uma [Issue](https://github.com/seu-usuario/chatbot-openai/issues)

---

**⭐ Se este projeto foi útil, considere dar uma estrela no GitHub! ⭐**