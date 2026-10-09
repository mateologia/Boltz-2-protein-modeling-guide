import glob
import json
import os

files = sorted(glob.glob("boltz_results/**/confidence*.json", recursive=True))

print(f"{'Caso':<30} | {'iPTM':<8} | {'PTM':<8}")
print("-" * 50)
for f in files:
    name = os.path.basename(f).replace(".json", "")
    with open(f) as j:
        d = json.load(j)
        iptm = d.get("iptm", "N/A")
        ptm = d.get("ptm", "N/A")
        print(f"{name:<30} | {float(iptm):<8.4f} | {float(ptm):<8.4f}")
