# Exploratory Data Analysis of the U.S. Opioid Epidemic

## Technologies used:
- Python
- Pandas
- Matplotlib
- Plotly
- Seaborn
- pingouin
- scipy.stats

## Primary Research Questions:

1. What are the trends in opioid mortality across the U.S.?
2. How accessible are treatment centers across the country?
3. Who are those most affected by opioid mortalities in the U.S.?
4. Which regions have the higest prescription rates?

## Variables:
1. Opioid Mortality Rate
2. Prescription Rates
3. Age
4. Gender
5. Drug Type
6. Treatment Prevention Centers

## Data Sources:

GitHub search: “opioid epidemic data analysis”
Source 1: Opioid Environment Policy Scan (OEPS) Data Warehouse
https://github.com/GeoDaCenter/opioid-policy-scan
Health04_C
Health04_S

Google Search: “opioid mortality rate by gender in U.S.”
Source 2: National Safety Council Injury Facts
https://injuryfacts.nsc.org/home-and-community/safety-topics/drugoverdoses/data-details/

Google Search: “substance abuse treatment services survey”
Source 3: National Survey of Substance Abuse Treatment Services (N-SSATS)
https://www.samhsa.gov/data/data-we-collect/n-ssats-national-survey-substance-abuse-treatment-services
NSSATS_PUF_2020
N-SSATS-2020 Codebook


## Plots per Notebook:

### demographics.ipynb

### examining the demographics surrounding drug and opioid-specific death rates

### Plotting drug deaths and only opioid-specific deaths

### Opioid mortality rate based across age groups

### Opioid mortality rates for 24-35 year olds broken down by gender

### Male deaths by opioid type

## Choropleth.ipynb

### U.S. Color Map of:
- Opioid Mortality Rate (per 100,000)
- Number of Substance Abuse Treatment Facilities
- Opioid Treatment Programs : Opioid Mortality

## TFQ_analysis.ipynb

- Scatterplot: Regional Opioid Mortality Rate by Percent -OTP-Offering Facilities
- Histogram of Treatment Facility (TFQ) (N=15955)
- Boxplot of Treatment Facility Quality grouped by U.S. Region
- Scatterplot: State Average Treatment Facility Quality by State Average Opioid Mortality Rate
- Seaborn Scatterplot: Opioid Mortality Rate by Treatment Facility Quality

TFQ_pairwise_ttest_results.csv

## ANOVA_odMortRtAv.ipynb

Boxplot of State Opioid Mortality Rate by Region

odMortRtAv_regional_pairwise_gameshowell_results.csv
odMortRtAv_regional_pairwise_ttest_results.csv

## Powerpoint presentation

Google slides:
https://docs.google.com/presentation/d/17T2JVdQYNJ88yuzpvdLqhR-1VcwnK_MU8-BpknB8m9A/edit#slide=id.g237397f7d59_0_6

## Summary
- Opioid-related deaths constitute ~50% of all drug deaths
- Age Group 25-34 is the most affected age group in terms of annual opioid-related mortalities
- Men of 25-34 are disproportionately affected by the opioid epidemic
- Fentanyl-related deaths among Men
- Opioid-related death rates were higher in the Northeast and Midwest regions
- There is a significant Regional difference in Opioid - Mortality Rate (OMR) and these regions p values being .0006 and .012, respectively.
- State OMR  Ranges: 9.75 in Nebraska to 48.52 in West Virginia  (100k per capita)
- A strong correlation between quality treatment facilities and opioid mortality rates of almost 0.8 (0.79).

## Limitations

- Initial Complex data
- More Research
- Correlation between Opioid Mortality Rate by Quality - Treatment Facilities and Region
- Timeframe 2014-2019 & 2020
- Point: COVID Impact
- Univariate Regression
- These data really require more complex modelling


## Team Members:
- Ethan Wright
- Avis Randle
- Melissa Prax
- Nigan Marin
- Alex Valerio
