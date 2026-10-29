# Exploratory annual forecast. Only five annual observations are available;
# this is a classroom demonstration, not a reliable operational prediction.
if (!requireNamespace("forecast", quietly = TRUE)) {
  install.packages("forecast", repos = "https://cloud.r-project.org")
}
library(forecast)

years <- 2020:2024
accidents <- c(372181, 412432, 461312, 480583, 487705)
series <- ts(accidents, start = 2020, frequency = 1)
fit <- ets(series)
pred <- forecast(fit, h = 2, level = 80)

out <- data.frame(
  year = 2025:2026,
  forecast = as.numeric(pred$mean),
  lower_80 = as.numeric(pred$lower[,1]),
  upper_80 = as.numeric(pred$upper[,1])
)
write.csv(out, "../output_forecast.csv", row.names = FALSE)
print(pred)
cat("Caution: annual series contains only five observations; forecasts are exploratory.\n")
