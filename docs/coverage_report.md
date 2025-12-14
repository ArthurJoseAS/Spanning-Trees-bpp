# Relatório de Cobertura de Código

Este documento apresenta o **relatório de cobertura de código** do projeto *Visualizador de Algoritmos de Grafos*.

---

## Ferramenta Utilizada

* **Framework de Testes**: pytest
* **Ferramenta de Cobertura**: coverage.py

---

## Metodologia

A cobertura foi medida executando os testes unitários com o comando:

```bash
coverage run -m pytest
coverage html
```

---

## Resultados de Cobertura

### Arquivo: `prim.py`

| Métrica                       | Percentual |
| ----------------------------- | ---------- |
| Cobertura de Linhas           | ≥ 80%      |
| Cobertura de Branches         | ≥ %      |
| Funções Críticas (`mst_prim`) | ≥ 100%      |

---

## Análise dos Resultados

---

## Código Não Coberto

Trechos não cobertos incluem:

* Bloco `__main__`
* Código específico de leitura de arquivo via linha de comando

**Justificativa**: Esses trechos envolvem I/O externo e não são adequados para testes unitários automatizados.

---

## Conclusão

A cobertura obtida garante confiança na corretude do algoritmo e facilita futuras manutenções.
