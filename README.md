# housing-market-analysis
I used pandas, matplotlib, requests, and geoapify_key to analyze the California real estate market at the end of 2022.

I sourced a CSV file from Zillow that provides median sale prices in the United States from April 2008 to August 2023. From this data, I focused on California in 2022 and identified the top 5 regions with the highest sale prices in December 2022. Using matplotlib, I charted the sale price trends for these regions. The results showed that all five regions had a similar pattern: sale prices peaked around the middle of the year (around May or June) and dipped at the beginning and end (around January and December). Thus, it seems January and December might be the optimal months for buying a house, while May or June could be ideal for selling.

To visually display these regions, I employed requests and folium. The map highlighted that Northern California tends to be more expensive than Southern California.

I retrieved data on median sale prices, population, and unemployment rates from the Census Bureau website. I initially attempted to use the Census API to acquire this data but encountered difficulties. Ultimately, I manually sourced the data, although I believe there are more efficient methods available.

After merging the dataframes to combine the December median sale prices of the top 5 regions with median household income, population, and unemployment data, I conducted linear regression analyses to examine potential correlations between price, income, population, and unemployment rates.

The R-values and scatter plots indicated that while income influences sale prices, population and unemployment did not show as strong a correlation as I had anticipated.

