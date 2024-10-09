# Automation: Product-Register
[![NPM](https://img.shields.io/github/license/BalbinaRaquel/automationProduct-Register
)](https://github.com/BalbinaRaquel/automationProduct-Register/blob/main/LICENSE) 

# Sobre o Projeto

Projeto de automação de tarefas em Python, realizado durante o evento **Jornada Python**, de 07 a 11 de outubro de 2024, organizado pela [Hashtag Programação](https://blp.hashtagtreinamentos.com/links-instagram-hashp?origemurl=hashtag_yt_org_bio_hashp) 

A automação utiliza uma base de dados de produtos - dados referentes a marca, tipo, categoria, preço e custo, etc -, para cadastrar os produtos no site de uma empresa fictícia fornecido pela Hashtag Programação: [Site de cadastro](https://dlp.hashtagtreinamentos.com/python/intensivao/login).
No processo automatizado, realiza-se o login no site, com user name e senha, para entrar no formulário de cadastro de produtos a partir de uma base de dados em formato .csv. 
Os produtos são cadastrados em sequência, e salvos na base de dados do site de forma automatizada. Imagens de evidências da automação são criadas ao longo do processo. 

## Estrutura do processo de automação

Use-Case: Automatizar Cadastro de produtos
Step 01: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
Step 02: Fazer login
Step 03: Importar a base de dados
Step 04: Cadastrar todos os produtos da lista do banco de dados

## Layout do site de cadastro **Hashtag Progração**
![Sistema Python PowerUp](https://github.com/BalbinaRaquel/automationProduct-Register/blob/main/assets/credenciais.png)

![Formulário de Cadastro de Produtos](https://github.com/BalbinaRaquel/automationProduct-Register/blob/main/assets/cadastro_produtos.png)

# Tecnologias utilizadas
- Python
- Poetry (gerenciar projeto com ambiente virtual)
- Pyautogui
- pandas

## tool Poetry

- name = "python-powerup"
- version = "0.1.0"
- description = "Case: Automatizar Cadastro de produtos no site da empresa"
- authors = ["BalbinaRaquel <balbina.rakell@outlook.com>"]

## Poetry dependencies
- python = versão 3.11
- pandas = versão 2.2.3
- pyautogui = versão 0.9.54.

```bash
# clonar repositório
git clone https://github.com/BalbinaRaquel/automationProduct-Register.git

```
# Autor
**Balbina Raquel Correia**

###

<div align="left">
 
  <a href="eng.balbinacorreia@gmail.com" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="gmail logo"  />
  </a>
  <a href="https://www.linkedin.com/in/engbalbinacorreia/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="linkedin logo"  />
  </a>
  <a href="balbinacorreia@hotmail.com" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Outlook&logo=microsoft-outlook&label=&color=0078D4&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="microsoft-outlook logo"  />
  </a>
</div>


###

<img align="right" height="150" src="https://i.imgflip.com/65efzo.gif"  />

###







