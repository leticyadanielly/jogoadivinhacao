Projeto de Testes Automatizados — Jogo Python

Este repositório contém a suíte de testes automatizados e a estrutura do projeto em Python, desenvolvida com foco em qualidade de software (QA), utilizando a arquitetura Page Object Model (POM) e o framework Pytest.

🛠️ Tecnologias Utilizadas

Linguagem: Python

Framework de Testes: Pytest

Relatórios: Pytest HTML Report

Padrão de Projeto: Page Object Model (POM)

Shell Scripting: Bash (automação de execução)
📁 Estrutura do Projeto
jogo.py/
├── pages/                    # Camada de Page Objects (Mapeamento de Páginas e Telas)
│   ├── base_game.py          # Classe base com ações genéricas do jogo
│   ├── difficulty_game.py    # Mapeamento e ações das telas de dificuldade
│   └── score_game.py         # Mapeamento da tela de pontuação/score
├── tests/                    # Suíte de Testes Automatizados
│   ├── conftest.py           # Fixtures do Pytest e configurações globais
│   ├── test_nivel1.py        # Cenários de teste para o Nível 1
│   ├── test_nivel2.py        # Cenários de teste para o Nível 2
│   └── test_nivel3.py        # Cenários de teste para o Nível 3
├── reports/                  # Relatórios de execução dos testes (Ignorado pelo Git)
├── main.py                   # Ponto de entrada / Execução do jogo
├── pytest.ini                # Arquivo de configurações do Pytest
├── regressao.sh              # Script Bash para execução do suite de regressão
└── .gitignore                # Regras para ignorar arquivos temporários e caches

⚙️ Pré-requisitos

Python 3.x instalado.

Git instalado.

🚀 Como Executar o Projeto

1- Clone este repositório:
git clone <URL_DO_SEU_REPOSITORIO>
cd jogo.py

2- Crie e ative um ambiente virtual (recomendado):
# Windows (Git Bash / CMD)
python -m venv venv
source venv/Scripts/activate  # Git Bash
# venv\Scripts\activate.bat   # CMD

3- Instale as dependências:
pip install pytest pytest-html

4- Execute a aplicação principal:
python main.py


🧪 Execução dos Testes Automatizados

Executar todos os testes
pytest

Executar um arquivo de teste específico
pytest tests/test_nivel1.py

Executar a suíte de regressão via Script Bash

Você pode rodar o script configurado para gerar relatórios automatizados:
bash regressao.sh

📊 Relatórios de Teste

Após a execução via script ou Pytest HTML, o relatório formatado será gerado na pasta reports/:
reports/relatorio_regressao.html

📝 Boas Práticas Adotadas

Separação de Conceitos: Lógica de navegação e seletores isolados na pasta pages/, e cenários de validação isolados na pasta tests/.;

Rastreabilidade Git: Arquivos de cache (__pycache__, .pytest_cache);

Relatórios locais são mantidos fora do controle de versão via .gitignore.
