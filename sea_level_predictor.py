import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Use Pandas to import the data from epa-sea-level.csv.
df = pd.read_csv(r"C:\Users\HP\Desktop\project\datasets\epa-sea-level.csv")

# Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
plt.figure(figsize=(10, 6))
plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Observed Sea Level")

# Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit 
# over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
# Generate x-values for the line of best fit up to 2050
years_extended = pd.Series(range(1880, 2051))
sea_level_pred = intercept + slope * years_extended
# Plot the line of best fit on the entire dataset
plt.plot(years_extended, sea_level_pred, "r", label="Best Fit Line (1880-2050)")

# Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go 
# through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
recent_df = df[df["Year"] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"])
# Predict sea levels for the recent trend up to 2050
sea_level_pred_recent = intercept_recent + slope_recent * years_extended
# Plot the second line of best fit
plt.plot(years_extended, sea_level_pred_recent, "green", label="Best Fit Line (2000-2050)")

# The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()

# Save and display the plots
plt.savefig("sea_level_plot.png")
plt.show()