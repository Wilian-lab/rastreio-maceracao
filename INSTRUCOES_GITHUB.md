# 🚀 Como Publicar no GitHub Pages

## 📋 Passo a Passo Completo

### 1️⃣ Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name**: `rastreio-maceracao` (ou outro nome)
   - **Description**: "Análise de Temperatura e Tempo de Maceração"
   - ✅ Marque: **Public** (para GitHub Pages grátis)
   - ❌ NÃO marque: "Add a README file" (já temos um)
3. Clique em: **Create repository**

---

### 2️⃣ Configurar Git Local (Se ainda não tem)

Abra o terminal no VS Code (Ctrl + ') e execute:

```powershell
# Configurar seu nome e email (apenas primeira vez)
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

---

### 3️⃣ Subir os Arquivos para o GitHub

No terminal, execute os comandos:

```powershell
# Ir para a pasta do projeto
cd "c:\Users\wiill\Documents\Rastreio-masceracao"

# Inicializar repositório Git
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "🎉 Primeira versão: Análise completa Temperatura x Tempo"

# Conectar ao GitHub (substitua SEU-USUARIO pelo seu nome de usuário)
git remote add origin https://github.com/SEU-USUARIO/rastreio-maceracao.git

# Renomear branch para main
git branch -M main

# Enviar para o GitHub
git push -u origin main
```

**⚠️ IMPORTANTE**: Substitua `SEU-USUARIO` pelo seu nome de usuário do GitHub!

---

### 4️⃣ Ativar GitHub Pages

1. Vá para o repositório no GitHub
2. Clique em: **Settings** (Configurações)
3. No menu lateral, clique em: **Pages**
4. Em **Source**, selecione:
   - **Branch**: `main`
   - **Folder**: `/ (root)`
5. Clique em: **Save**

⏱️ **Aguarde 1-2 minutos** para o site ficar pronto!

---

### 5️⃣ Acessar o Relatório Online

Seu relatório estará disponível em:

```
https://SEU-USUARIO.github.io/rastreio-maceracao/
```

**Exemplo**: Se seu usuário for `joaosilva`, o link será:

```
https://joaosilva.github.io/rastreio-maceracao/
```

---

## 📤 Como Atualizar o Relatório no Futuro

Quando gerar um novo relatório:

```powershell
# Adicionar novos arquivos
git add .

# Fazer commit com mensagem descritiva
git commit -m "📊 Atualização: Dados de [mês/ano]"

# Enviar para o GitHub
git push
```

O site será atualizado automaticamente em 1-2 minutos! 🚀

---

## 🔗 Compartilhar com Seu Chefe

Depois de publicado, você pode:

1. ✅ Enviar o **link direto** (não precisa baixar nada!)
2. ✅ Funciona em **qualquer dispositivo** (PC, celular, tablet)
3. ✅ **Sempre atualizado** (basta dar git push)
4. ✅ **Profissional** e fácil de compartilhar

---

## ❓ Precisa de Ajuda?

Se tiver algum erro, me mostre a mensagem e eu te ajudo! 😊

**Comandos úteis:**

```powershell
# Ver status dos arquivos
git status

# Ver histórico de commits
git log --oneline

# Ver repositórios remotos configurados
git remote -v
```

---

**🎯 Após seguir estes passos, seu relatório estará online e acessível por qualquer pessoa com o link!**
