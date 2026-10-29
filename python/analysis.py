"""Create Power BI-friendly summary tables from the source CSV."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "state_accidents_2020_2024.csv")
long = df.melt(id_vars="state_ut", var_name="year", value_name="accidents")
long["year"] = pd.to_numeric(long["year"])
long["accidents"] = pd.to_numeric(long["accidents"], errors="coerce")
long.to_csv(ROOT / "output_state_year.csv", index=False)

totals = pd.DataFrame({
    "year":[2020,2021,2022,2023,2024],
    "accidents":[372181,412432,461312,480583,487705]
})
totals["change_from_previous_pct"] = totals["accidents"].pct_change() * 100
totals.to_csv(ROOT / "output_national_trend.csv", index=False)

latest = long[long["year"] == 2024].dropna().sort_values("accidents", ascending=False)
latest.to_csv(ROOT / "output_state_ranking_2024.csv", index=False)
print("Created output_state_year.csv, output_national_trend.csv, output_state_ranking_2024.csv")
