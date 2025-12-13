# Análise de Uso de Memória

Este documento apresenta a **análise de uso de memória** do projeto *Visualizador de Algoritmos de Grafos*.

---

## Análise do Arquivo: `prim.py`

---

### 1. **Uso Excessivo de Estruturas Temporárias**

* **Arquivo**: `prim.py`
* **Linhas**: 44–67
* **Descrição**: A estrutura `work_queue` é constantemente recriada, reorganizada e expandida durante a execução do algoritmo de Prim.
* **Severidade**: Média
* **Problemas Específicos**:

  * Uso contínuo de memória temporária
  * Aumento do consumo de heap em grafos densos
* **Técnica de Análise**: Inspeção de código
* **Status**: Parcialmente otimizado

---

### 2. **Duplicação de Estruturas de Grafo**

* **Arquivo**: `prim.py`
* **Linhas**: 69–78
* **Descrição**: O grafo de saída (MST) é criado como uma nova estrutura independente, duplicando parte das informações do grafo original.
* **Severidade**: Baixa
* **Problemas Específicos**:
  * Consumo adicional de memória
  * Necessário apenas para visualização
* **Status**: Aceito (trade-off funcional)

---

### 3. **Uso de Conjuntos para Controle de Nós Visitados**

* **Arquivo**: `prim.py`
* **Linhas**: 46
* **Descrição**: Uso de `set` para armazenar nós já visitados.
* **Severidade**: Baixa
* **Justificativa**:
  * Estrutura eficiente
  * Operações O(1)
* **Status**: Adequado

---

### 4. **Construção Manual de Strings no Exportador**

* **Arquivo**: `prim.py`
* **Linhas**: 72–75
* **Descrição**: Construção manual de strings para labels das arestas.
* **Severidade**: Baixa
* **Problema**:
  * Alocação desnecessária de listas temporárias
* **Status**: Otimizado

---

## Impacto Geral no Consumo de Memória

* Consumo proporcional a **O(V + E)**
* Pico de memória concentrado durante a execução do algoritmo de Prim
* Uso aceitável para fins educacionais e visualização

---

## Conclusão

A análise demonstra que o projeto possui **uso de memória controlado e previsível**, com pequenos trade-offs aceitáveis devido ao foco em visualização.
