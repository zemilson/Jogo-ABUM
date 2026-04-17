# Santuário Manager: Sistema de Gerenciamento de Igreja

## Visão Geral

O Santuário Manager é um software desktop desenvolvido em Python, utilizando a biblioteca `tkinter` para a interface gráfica e `sqlite3` para o banco de dados local. Ele foi projetado para auxiliar igrejas na gestão de membros, finanças e eventos de forma simples e eficiente.

## Funcionalidades Atuais

*   **Dashboard:** Visão geral com estatísticas rápidas sobre membros e finanças.
*   **Gestão de Membros:** Cadastro, listagem e atualização de informações de membros.
*   **Gestão Financeira:** Registro de entradas e saídas (dízimos, ofertas, despesas) com categorização.
*   **Gestão de Eventos:** Cadastro e listagem de eventos da igreja.

## Estrutura do Projeto

O projeto é organizado nos seguintes arquivos:

*   `main.py`: Ponto de entrada principal da aplicação.
*   `database.py`: Módulo responsável pela conexão e criação das tabelas no banco de dados SQLite (`igreja.db`).
*   `models.py`: Contém as funções de interação com o banco de dados (CRUD) para membros, finanças e eventos.
*   `ui.py`: Define a interface gráfica do usuário, construída com `tkinter`.
*   `requirements.txt`: Lista as dependências do projeto.

## Como Executar o Projeto (VS Code)

Siga os passos abaixo para configurar e executar o Santuário Manager em seu ambiente VS Code:

### 1. Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu sistema. O `tkinter` e `sqlite3` são bibliotecas padrão do Python e geralmente vêm pré-instaladas.

### 2. Clonar o Repositório (se aplicável)

Se você recebeu o projeto via GitHub, clone-o para sua máquina local:

```bash
git clone https://github.com/zemilson/Jogo-ABUM.git # Substitua pelo link correto do repositório, se houver
cd Jogo-ABUM/church_manager # Ajuste o caminho se o projeto estiver em um subdiretório
```

Se você recebeu os arquivos diretamente, navegue até a pasta `church_manager`.

### 3. Instalar Dependências

Abra o terminal no VS Code (Terminal > New Terminal) e navegue até o diretório raiz do projeto (`church_manager`). Em seguida, instale as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

No mesmo terminal, execute o arquivo `main.py`:

```bash
python main.py
```

Isso iniciará a interface gráfica do Santuário Manager. O banco de dados `igreja.db` será criado automaticamente na primeira execução, se ainda não existir.

## Desenvolvimento e Contribuição

Este projeto está em desenvolvimento contínuo. Sinta-se à vontade para explorar o código, sugerir melhorias ou adicionar novas funcionalidades. As principais áreas para expansão incluem:

*   Funcionalidades de edição e exclusão para finanças e eventos.
*   Relatórios e gráficos mais detalhados (usando `matplotlib` e `pandas`).
*   Funcionalidades de busca e filtragem avançadas.
*   Exportação de dados.

---

**Desenvolvido por:** Manus AI
**Data:** 17 de Abril de 2026
