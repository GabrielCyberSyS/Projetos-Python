🚀 1) CRIAR UM PROJETO DO ZERO E ENVIAR PARA O GITHUB
PASSO 1 — Criar a pasta
mkdir Projetos-Python
cd Projetos-Python

PASSO 2 — Iniciar o Git
git init

PASSO 3 — Criar repositório no GitHub

No GitHub ➝ New Repository
Nome → Projetos-Python
Crie o repositório sem README ou *.gitignore.

PASSO 4 — Conectar o Git local ao GitHub
git remote add origin https://github.com/GabrielCyberSyS/Projetos-Python.git


(Se já existir algum remote errado:)

git remote remove origin

PASSO 5 — Adicionar arquivos
git add .

PASSO 6 — Commit
git commit -m "Primeiro commit"

PASSO 7 — Enviar para GitHub
git branch -M main
git push -u origin main


Pronto: projeto novo criado e enviado!

🚀 2) ENVIAR UM PROJETO JÁ EXISTENTE PARA O GITHUB

Se você já tem uma pasta no PC e quer mandar para o GitHub:

PASSO 1 — Abrir a pasta no terminal
cd pasta-do-seu-projeto

PASSO 2 — Iniciar Git
git init

PASSO 3 — Conectar ao GitHub
git remote add origin https://github.com/GabrielCyberSyS/NOME-DO-REPO.git

PASSO 4 — Add + Commit + Push
git add .
git commit -m "Projeto inicial"
git branch -M main
git push -u origin main

🚀 3) CLONAR UM PROJETO DO GITHUB PARA SEU PC E EDITAR

Quando o repositório já existe no GitHub e você quer trazer para o VS Code:

PASSO 1 — Clonar
git clone https://github.com/GabrielCyberSyS/Projetos-Python.git

PASSO 2 — Entrar na pasta clonada
cd Projetos-Python

PASSO 3 — Editar arquivos no VS Code

No VS Code:

File → Open Folder → Projetos-Python

PASSO 4 — Depois de editar: Add + Commit + Push
git status
git add .
git commit -m "Alterações feitas"
git push


Pronto, enviou as mudanças!

🚀 4) ATUALIZAR (PULL) + ENVIAR MUDANÇAS (PUSH)

Esse é o fluxo do dia a dia.

✔ Para atualizar seu PC com o que está no GitHub
git pull

✔ Para enviar alterações para o GitHub
git add .
git commit -m "Mensagem das alterações"
git push

🧠 RESUMO GERAL (COLA RÁPIDA)
SITUAÇÃO	COMANDO
Criar repo local	git init
Ver status	git status
Adicionar arquivos	git add .
Fazer commit	git commit -m "mensagem"
Conectar ao GitHub	git remote add origin URL
Remover remote errado	git remote remove origin
Trocar branch para main	git branch -M main
Enviar para GitHub	git push -u origin main
Atualizar do GitHub	git pull
Clonar repo	git clone URL
🎯 Explicação resumida e clara
🔹 Quando o projeto nasce no seu PC → git init + remote + push
🔹 Quando o projeto nasce no GitHub → git clone
🔹 Quando você quiser atualizar → git pull
🔹 Quando você editar algo → add + commit + push