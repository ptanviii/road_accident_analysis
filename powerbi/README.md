# Power BI setup
1. Open Power BI Desktop.
2. Select Home → Get Data → Text/CSV.
3. Import `data/state_accidents_2020_2024.csv`.
4. In Power Query, select the year columns and choose Transform → Unpivot Columns.
   Keep `state_ut` as the identifier. Rename `Attribute` to `Year` and `Value` to `Accidents`.
5. Load the table and create:
   - Cards: national accident totals (use the national totals table below or add it as a second CSV).
   - Bar chart: State/UT by Accidents, filtered to 2024.
   - Line chart: Year by national accidents.
   - Slicer: Year and State/UT.
6. National totals (MoRTH/PRS table) for a separate CSV:
   Year,Accidents
   2020,372181
   2021,412432
   2022,461312
   2023,480583
   2024,487705

Suggested DAX:
Total State Accidents = SUM('state_accidents_long'[Accidents])
State Count = DISTINCTCOUNT('state_accidents_long'[state_ut])

Important: state-wise values and national totals are sourced from the cited table. Some state-year entries are unavailable (Ladakh 2020); do not treat missing values as zero.
