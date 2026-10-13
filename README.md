# Modelagem de Complexos TCR-pMHC com Boltz-2

Pipeline para modelagem estrutural do pentâmero TCR-pMHC utilizando o Boltz-2 com alinhamento múltiplo automático via servidor ColabFold/MMseqs2.

## Estrutura do Complexo Pentamérico
- **Cadeia A:** Ectodomínio completo do MHC classe I ($\alpha_1 + \alpha_2 + \alpha_3$)
- **Cadeia B:** Beta-2-microglobulina ($\beta_2\text{M}$ constante)
- **Cadeia C:** Peptídeo antigênico (`peptide`)
- **Cadeia D:** Domínio variável alfa do TCR (`TCR_A_full_variable_seq`)
- **Cadeia E:** Domínio variável beta do TCR (`TCR_B_full_variable_seq`)

> **Nota sobre o domínio $\alpha_3$:** A tabela original continha apenas os domínios $\alpha_1$ e $\alpha_2$ (~180 resíduos). O script `gerar_yamls.py` anexa automaticamente o domínio $\alpha_3$ canônico do alelo HLA-A*01:01 (resíduos 181–275) para que o ectodomínio do MHC fique completo e emparelhe corretamente com a $\beta_2\text{M}$.

## Pipeline de Execução

### 1. Filtragem dos Casos de Interesse
```bash
head -n 6 gliph_TCRs_8_1.csv > gliph_TCRs_8_1_top5.csv
```

### 2. Geração dos Manifestos YAML
```bash
python gerar_yamls.py
```

### 3. Predição com Boltz-2
```bash
boltz predict boltz_inputs/ \
    --use_msa_server \
    --out_dir boltz_results
```

### 4. Leitura dos Resultados
```bash
python parse_results.py
```

## Resultados Obtidos (Ectodomínio Completo)

| Caso | Peptídeo | Alelo MHC | Cadeia $\alpha$ do TCR | Cadeia $\beta$ do TCR | iPTM | PTM | Confiabilidade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Complexo 1** | `VTEHDTLLY` | A*01:01 | TRAV9-2*01 | TRBV7-9*01 | **0.9527** | **0.9639** | Muito Alta |
| **Complexo 2** | `VTEHDTLLY` | A*01:01 | TRAV9-2*01 | TRBV5-1*01 | **0.8946** | **0.9180** | Alta |
| **Complexo 3** | `VTEHDTLLY` | A*01:01 | TRAV9-2*01 | TRBV13*01 | **0.9195** | **0.9371** | Muito Alta |
| **Complexo 4** | `VTEHDTLLY` | A*01:01 | TRAV9-2*01 | TRBV7-6*01 | **0.8998** | **0.9182** | Alta |
| **Complexo 5** | `VTEHDTLLY` | A*01:01 | TRAV9-2*01 | TRBV7-9*01 | **0.9505** | **0.9619** | Muito Alta |
