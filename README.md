# Modelagem de Complexos TCR-pMHC com Boltz-2

Pipeline para modelagem estrutural do pentâmero TCR-pMHC utilizando o Boltz-2 com alinhamento múltiplo automático via servidor ColabFold/MMseqs2.

## Estrutura do Complexo Pentamérico
- **Cadeia A:** Cadeia alfa do MHC classe I (`MHC_seq`)
- **Cadeia B:** Beta-2-microglobulina ($\beta_2\text{M}$ constante)
- **Cadeia C:** Peptídeo antigênico (`peptide`)
- **Cadeia D:** Domínio variável alfa do TCR (`TCR_A_full_variable_seq`)
- **Cadeia E:** Domínio variável beta do TCR (`TCR_B_full_variable_seq`)

## Passo a Passo

### 1. Filtragem da Tabela
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

### Resultados Obtidos (Top 5)
| Caso | iPTM | PTM | Confiabilidade |
| :--- | :--- | :--- | :--- |
| **Complexo 1** | 0.9202 | 0.9426 | Muito Alta |
| **Complexo 2** | 0.9238 | 0.9439 | Muito Alta |
| **Complexo 3** | 0.9036 | 0.9264 | Muito Alta |
| **Complexo 4** | 0.8793 | 0.9095 | Alta |
| **Complexo 5** | 0.9421 | 0.9594 | Muito Alta |
