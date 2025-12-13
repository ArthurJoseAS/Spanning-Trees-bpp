# Relatório de Testes Automatizados

Este documento descreve a **estratégia, execução e resultados** dos testes automatizados do projeto *Visualizador de Algoritmos de Grafos*.

---

## Estratégia de Testes

Os testes foram desenvolvidos com foco em:

* Funções puras
* Algoritmos centrais
* Casos normais e de borda
* Robustez contra entradas inválidas

---

## Estrutura de Testes

```
tests/
└── unit/
    └── test_prim.py
```

---

## Casos de Teste Implementados

### 1. **Testes de Estrutura do Grafo**

* Preenchimento correto da lista de nós
* Ausência de duplicatas
* Construção adequada da lista de adjacência

---

### 2. **Testes do Algoritmo de Prim**

* Geração correta da MST
* Validação do peso total
* Comportamento com grafo desconectado
* Execução com grafo contendo apenas um nó

---

### 3. **Testes de Exportação**

* Criação correta do grafo de saída
* Verificação de labels e pesos

---

## Princípios FIRST

Os testes seguem os princípios FIRST:

* **Fast**: Execução rápida
* **Independent**: Testes independentes entre si
* **Repeatable**: Resultados consistentes
* **Self-validating**: Uso de assertivas claras
* **Timely**: Desenvolvidos junto ao código

---

## Resultados

* Todos os testes executam com sucesso
* Nenhuma falha detectada após refatorações
* Base sólida para regressão futura

---

## Conclusão

A suíte de testes implementada garante confiabilidade ao projeto.
