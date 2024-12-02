import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df = pd.read_csv("C:\\Users\\HP\\Desktop\\Metro Tech Hub Training\\fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
lower_bound = df["value"].quantile(0.025)
upper_bound = df["value"].quantile(0.975)
df_cleaned = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]

# Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be 
# Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page 
# Views.
def draw_line_plot():
    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot the data
    ax.plot(df_cleaned.index, df_cleaned["value"], color="tab:blue")
    
    # Title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    # Show the plot
    plt.show()

# Generate the line plot
draw_line_plot()

# Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views 
# for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis 
# should be Years and the label on the y axis should be Average Page Views.
def draw_bar_plot():
    # Prepare the data for bar plot
    df_bar = df_cleaned.copy()
    df_bar["Year"] = df_bar.index.year
    df_bar["Month"] = df_bar.index.month_name()
    
    # Group the data by year and month, then calculate the mean for each group
    df_bar = df_bar.groupby(["Year", "Month"])["value"].mean().unstack()
    
    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    df_bar.plot(kind="bar", ax=ax, legend=True, cmap="tab10")
    
    # Title and labels
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")
    
    # Show the plot
    plt.show()

# Generate the bar plot
draw_bar_plot()

# Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots 
# should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart 
# should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the 
# month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.
def draw_box_plot():
    # Prepare the data for box plot
    df_box = df_cleaned.copy()
    df_box["Year"] = df_box.index.year
    df_box["Month"] = df_box.index.month_name()
    df_box["Month"] = pd.Categorical(df_box['Month'], 
    categories=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], 
    ordered=True)
    
    # Set up the figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Year-wise Box Plot
    sns.boxplot(x="Year", y="value", data=df_box, ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    
    # Month-wise Box Plot
    sns.boxplot(x="Month", y="value", data=df_box, ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    
    # Show the plot
    plt.show()

# Generate the box plot
draw_box_plot()