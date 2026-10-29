# Road Accident Analysis in India
A student data analytics project using Python, R, Power BI and a web dashboard.

## Run the website
1. Install Python 3.10+.
2. In a terminal, from this folder:
   `python -m pip install -r requirements.txt`
3. Run:
   `python python/app.py`
4. Open `http://127.0.0.1:5000`.

## Regenerate analysis tables
`python python/analysis.py`

## R forecast (exploratory only)
From the `r` folder run `Rscript forecast.R`. Ensure the `forecast` package is installed.
The annual series contains only five observations, so forecasts are illustrative and should not be presented as a dependable prediction.

## Data
State/UT accidents for 2020–2024 and official national totals are transcribed from the PRS India road transport brief's Table 15, citing MoRTH's *Road Accidents in India* report. Source link:
https://prsindia.org/budgets/parliament/demand-for-grants-2026-27-analysis-road-transport-and-highways
The 2024 MoRTH dataset collection is also available at:
https://data.opencity.in/dataset/road-accidents-in-india-2024

## Important limitations
- Counts are reported accidents, not a population-normalized risk rate.
- State-level counts are not directly comparable without considering population, vehicle numbers, road length and travel exposure.
- The project does not contain individual crash records, hour-of-day, month, or causal factors. Those charts require additional compatible source datasets.
- Missing values remain missing; they are not zero.
