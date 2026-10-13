import os
import pandas as pd
import yaml

CSV_PATH = "gliph_TCRs_8_1_top5.csv"
OUTPUT_DIR = "boltz_inputs"

# Cadeia constante da beta-2-microglobulina (B2M)
B2M_SEQ = "IQRTPKIQVYSRHPAENGKSNFLNCYVSGFHPSDIEVDLLKNGERIEKVEHSDLSFSKDWSFYLLYYTEFTPTEKDEYACRVNHVTLSQPKIVKWDRDM"

# Sequência do domínio alpha 3 canônico para HLA-A*01:01 (resíduos 181-275)
ALPHA3_HLA_A = "RTDPPKTHMTHHPISDHEATLRCWALGFYPAEITLTWQRDGEDQTQDTELVETRPAGDGTFQKWAAVVVPSGEEQRYTCHVQHEGLPKPLTLR"

os.makedirs(OUTPUT_DIR, exist_ok=True)
df = pd.read_csv(CSV_PATH)

for idx, row in df.iterrows():
    mhc_seq = str(row["MHC_seq"]).strip()

    # Se a sequência contiver apenas alpha1 + alpha2 (~180 resíduos), anexa o domínio alpha3
    if len(mhc_seq) <= 182:
        mhc_full = mhc_seq + ALPHA3_HLA_A
    else:
        mhc_full = mhc_seq

    data = {
        "version": 1,
        "sequences": [
            {"protein": {"id": "A", "sequence": mhc_full}},
            {"protein": {"id": "B", "sequence": B2M_SEQ}},
            {"protein": {"id": "C", "sequence": str(row["peptide"]).strip()}},
            {"protein": {"id": "D", "sequence": str(row["TCR_A_full_variable_seq"]).strip()}},
            {"protein": {"id": "E", "sequence": str(row["TCR_B_full_variable_seq"]).strip()}},
        ],
    }
    with open(os.path.join(OUTPUT_DIR, f"complexo_{idx+1}.yaml"), "w") as f:
        yaml.dump(data, f, sort_keys=False)

print(f"Arquivos YAML gerados com ectodomínio completo (alpha 1, 2 e 3) em '{OUTPUT_DIR}/'.")
