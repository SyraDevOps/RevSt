# Revista SYN — Gerador Automatizado

Sistema completo para gerar revistas digitais em PDF de forma automatizada e configurável, com layout personalizável e QR Codes dinâmicos. Projetado para ser modular, elegante e extensível.

---

## 🧠 Visão Geral

Este projeto permite construir revistas digitais utilizando conteúdos estruturados em JSON e temas visuais definidos em YAML. Ele gera um PDF final com páginas como:

- 📖 Capa
- ✍️ Artigos
- 📚 Glossário
- 🖼️ Galeria (opcional)
- 🔚 Contracapa

Tudo isso usando o poder do [ReportLab](https://www.reportlab.com/opensource/) e Python puro.

---

## 🗂 Estrutura do Projeto

```

revista\_syn/
├── core/                  # Núcleo da aplicação
│   ├── builder.py         # Motor de construção do PDF
│   ├── config\_loader.py   # Carregador de configurações
│   └── qr.py              # Geração de QR Codes
│
├── templates/             # Templates de cada tipo de página
│   ├── capa.py
│   ├── contracapa.py
│   ├── artigo.py
│   ├── glossario.py
│   └── galeria.py
│
├── styles/
│   └── temas.yaml         # Temas alternativos: syra, futurista, minimal
│
├── assets/
│   └── fontes/            # (opcional) Fontes personalizadas
│
├── data/
│   └── conteudo.json      # Conteúdo da edição
│
├── output/
│   └── revista\_SYN\_Ed01.pdf  # Revista gerada
│
├── config.yaml            # Configuração base da edição
├── main.py                # Ponto de entrada
└── requirements.txt       # Dependências do projeto

````

---

## 🚀 Como Usar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
````

### 2. Prepare seu conteúdo

Edite o arquivo `data/conteudo.json` com os dados da sua edição (veja exemplo abaixo).

### 3. Execute o gerador

```bash
python main.py
```

O PDF será salvo em `output/`.

---

## 🧪 Exemplo de conteúdo (`conteudo.json`)

```json
[
  {
    "tipo": "capa",
    "titulo": "SYN",
    "subtitulo": "Revista Técnica e Criativa",
    "edicao": "Edição Nº 01 // 2025",
    "slug": "ed01"
  },
  {
    "tipo": "artigo",
    "secao": "Tecnologia",
    "titulo": "Inteligência Artificial e o Futuro",
    "texto": "A IA está transformando o mundo...",
    "citar": "A IA não substituirá você. Alguém usando IA, sim.",
    "fundo_escuro": true
  },
  {
    "tipo": "glossario",
    "titulo": "Termos Técnicos",
    "termos": {
      "IA": "Inteligência Artificial...",
      "LLM": "Large Language Model..."
    }
  },
  {
    "tipo": "contracapa",
    "mensagem": "Obrigado por ler a edição 01!",
    "redes": "@SyraDevOps  •  github.com/SyraDevOps",
    "site": "syradevops.com",
    "slug": "ed01"
  }
]
```

---

## 🎨 Troca de Tema

Para usar outro tema visual (`futurista`, `minimal`), basta modificar seu `config.yaml` manualmente com os valores de `styles/temas.yaml`, ou podemos automatizar isso via código.

---

## 📦 Dependências

* `reportlab`
* `qrcode`
* `pyyaml`

Instaladas via `requirements.txt`.

---

## 📄 Licença

MIT. Feito com 💜 por [SyraDevOps](https://syradevops.com)

---

## ✨ Roadmap futuro

* [ ] Suporte a múltiplos artigos/páginas
* [ ] Galeria com scroll e mosaico
* [ ] Exportação HTML + EPUB
* [ ] Painel web para edição visual

