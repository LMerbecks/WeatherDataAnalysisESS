# WeatherDataAnalysisESS
Analysis of hystorical weather data for the city of Essen, Germany. Goal: Find pdf of four different weather parameters.

# Detailed Decription
The goal of this project is to analyse data from the Climate Data Center (CDC, [link](cdc.dwd.de/portal))  of the German weather service (Deutscher Wetterdienst, DWD, [link](dwd.de)) for a weather station in Essen Germany[^WeatherDataSource]. Four weather parameters should get investigated:

1. Percipation in [mm]
2. cloud coverage in [Okta]
3. sunshineduration in [min]
4. air temperature in [°C]

The investigation aims on a yearly statistical forecast of the parameters. For percipation the analysis should result in a bar graph, that plots the average percipation for a selected timespan. A problem with the underlying data set is that it will have some "drift" due to climate change. The ultimate goal is to estimate probability density functions (pdf) for all of the named parameters from the dataset.

# (Planned) Process
- [x] open github repository
- [ ] run following steps for sunshine duration first
- [ ] read data from raw csvs
- [ ] postprocess data, a timescale that is independent of actual year the data was recorded must be found probably based on the number 12, also faulty data must be filtered
- [ ] calculate mean for lowest time resolution (hours)
- [ ] plot data as a bar graph, this is a preliminary result
- [ ] estimate probability density function in two dimensions
- [ ] adapt to other parameters


# References

[^WeatherDataSource]: Daten extrahiert vom DWD Climate Data Center (CDC): Stündliche Stationsdaten, CDC-v2.1.b22.09, 17.05.2023.
