import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv(r"C:\Users\HP\Desktop\project\datasets\medical_examination.csv")

# Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight 
# in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT 
# overweight and the value 1 for overweight.
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value
# is more than 1, set the value to 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    # Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the
    #  df_cat variable.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the
    #  columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Convert the data into long format and create a chart that shows the value counts of the categorical features using the following
    # method provided by the seaborn library import: sns.catplot().
    fig = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")
    fig.set_axis_labels("Variable", "Total")
    fig.set_titles("Cardio = {col_name}")
    fig.despine(left=True)

    # Do not modify the next two lines
    # output the figure
    return fig
    
cat_plot_fig = draw_cat_plot()

# Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
    # diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
    # height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    # height is more than the 97.5th percentile
    # weight is less than the 2.5th percentile
    # weight is more than the 97.5th percentile
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix and store it in the corr variable.
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle and store it in the mask variable.
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(12, 12))

    # Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().
    sns.heatmap(corr, annot=True, mask=mask, square=True, fmt='.1f', center=0, vmin=-0.1, vmax=0.25, cmap='coolwarm')

    # Do not modify the next two lines.
    return fig

heat_map_fig = draw_heat_map()


# Display the figures
cat_plot_fig.savefig("C:\\Users\\HP\\Desktop\\project\\charts\\categorical_plot.png")
heat_map_fig.savefig("C:\\Users\\HP\\Desktop\\project\\charts\\heat_map.png")
    