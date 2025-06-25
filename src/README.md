# Projeto: Pipeline de Dados com Python – Estrutura Simples

**Disciplina:** Linguagens de Programação  
**Curso:** Engenharia de Dados – UNIFOR  
**Professor:** Ms. Alex Lima  
**Aluno:** ANDERSON DE OLIVEIRA SILVA

---

## 🎯 Objetivo

Construir uma pipeline de dados utilizando Python com foco em:

- Orientação a objetos e modularização
- Registro de logs e tempo de execução
- Tratamento de exceções
- Boas práticas de estrutura de projeto
- Organização em pacotes reutilizáveis

---

## 🧱 Estrutura do projeto


```
src/
├── AirbnbOpenData.csv               # Dados brutos
├── AirbnbOpenDataOutput.csv         # Dados processados
├── etl.py                           # Lógica da pipeline ETL
├── logs.py                          # Funções de logging
├── logs.txt                         # Arquivo de log da execução
├── main.py                          # Script principal
└── __pycache__/                     # Cache do Python (ignorado)
```

---


## 🚀 Execução do projeto

1. Certifique-se de ter o `AirbnbOpenData.csv` dentro da pasta `src/`
2. No terminal, a partir do diretório raiz do projeto, execute:

```bash
python /src/main.py
```

---

## 🧪 Saída esperada

```
Executando tarefa: Extrair
Tarefa Extrair finalizada com sucesso.
Executando tarefa: Transformar
Tarefa Transformar finalizada com sucesso.
Executando tarefa: Carregar
Tarefa Carregar finalizada com sucesso.
```

---
## 📦 Dependências

Instalar as bibliotecas: pandas e forex-python


## 📌 Observações finais

- A pipeline segue a ordem: Extrair → Transformar → Carregar
- Cada etapa registra logs com tempo e status
- O projeto foi desenvolvido com base na proposta da disciplina