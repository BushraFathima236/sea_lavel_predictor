import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read the data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Predict through 2050
    years = pd.Series(range(df["Year"].min(), 2051))
    predicted_sea_level = slope * years + intercept

    # Plot first line
    plt.plot(years, predicted_sea_level)

    # Use data from 2000 onward
    recent_df = df[df["Year"] >= 2000]

    slope_2000, intercept_2000, r_value, p_value, std_err = linregress(
        recent_df["Year"],
        recent_df["CSIRO Adjusted Sea Level"]
    )

    # Predict from 2000 through 2050
    years_2000 = pd.Series(range(2000, 2051))
    predicted_sea_level_2000 = (
        slope_2000 * years_2000 + intercept_2000
    )

    # Plot second line
    plt.plot(years_2000, predicted_sea_level_2000)

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return
    plt.savefig("sea_level_plot.png")
    return plt.gca()
