import os
import pandas as pd
import yaml

CSV_PATH = "gliph_TCRs_8_1_top5.csv"
OUTPUT_DIR = "boltz_inputs"

B2M_SEQ = "IQRTPKIQVYSRHPAENGKSNFLNCYVSGFHPSDIEVDLLKNGERIEKVEHSDLSFSKDWSFYLLYYTEFTPTEKDEYACRVNHVTLSQPKIVKWDRDM"

os.makedirs(OUTPUT_DIR, exist_ok=True)
df = pd.read_csv(CSV_PATH)

for idx, row in df.iterrows():
    data = {
        "version": 1,
        "sequences": [
            {"protein": {"id": "A", "sequence": str(row["MHC_seq"]).strip()}},
            {"protein": {"id": "B", "sequence": B2M_SEQ}},
            {"protein": {"id": "C", "sequence": str(row["peptide"]).strip()}},
            {"protein": {"id": "D", "sequence": str(row["TCR_A_full_variable_seq"]).strip()}},
            {"protein": {"id": "E", "sequence": str(row["TCR_B_full_variable_seq"]).strip()}},
        ],
    }

    yaml_path = os.path.join(OUTPUT_DIR, f"complexo_{idx + 1}.yaml")
    with open(yaml_path, "w") as f:
        yaml.dump(data, f, sort_keys=False)

print(f"Arquivos YAML gerados com sucesso em '{OUTPUT_DIR}/'.")
