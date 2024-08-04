# -*- coding: utf-8 -*-

# Import libraries ======================================================================

import pandas as pd # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

# Read and transform the data ===========================================================

# Read and transform the data of Consumer Price Index (CPI)
cpi_data = pd.read_excel("data/WEO_Data_CPI.xlsx")
cpi_data_long = cpi_data.melt(id_vars=["Country"], var_name="Year", value_name="CPI")

# Read and transform the data of Central Bank Independence (CBI)
cbi_data = pd.read_excel("data/CBI_Database.xlsx")
cbi_data_long = cbi_data.melt(id_vars=["Year"], var_name="Country", value_name="CBI")

# Plot to analyse the data ==============================================================

sns.relplot(data=cpi_data_long,
            x="Year",
            y="CPI",
            kind="line",
            hue="Country")

plt.ylabel("Average Consumer Price Index")

# Save our plot

plt.savefig("output/CPI for selected countries.png")

# Plot each countries Consumer Price Index ==============================================

cpi_peru = cpi_data_long[cpi_data_long["Country"] == "Peru"]
cpi_peru.head()

cpi_chile = cpi_data_long[cpi_data_long["Country"] == "Chile"]
cpi_chile.head()

cpi_colombia = cpi_data_long[cpi_data_long["Country"] == "Colombia"]
cpi_colombia.head()

cpi_mexico = cpi_data_long[cpi_data_long["Country"] == "Mexico"]
cpi_mexico.head()

fig = sns.relplot(data=cpi_peru,
            x="Year",
            y="CPI",
            kind="line",
            color="darkred")

plt.ylabel("Average Consumer Prices (% change)")

plt.title("CPI for Peru")
fig.tight_layout(pad=1.0)
plt.savefig("output/CPI for Peru.png")

fig = sns.relplot(data=cpi_chile,
            x="Year",
            y="CPI",
            kind="line",
            color = "orange")

plt.ylabel("Average Consumer Prices (% change)")

plt.title("CPI for Chile")
fig.tight_layout(pad=1.0)
plt.savefig("output/CPI for Chile.png")

fig = sns.relplot(data=cpi_colombia,
            x="Year",
            y="CPI",
            kind="line",
            color = "yellow")

plt.ylabel("Average Consumer Prices (% change)")

plt.title("CPI for Colombia")
fig.tight_layout(pad=1.0)
plt.savefig("output/CPI for Colombia.png")

fig = sns.relplot(data=cpi_mexico,
            x="Year",
            y="CPI",
            kind="line",
            color = "green")

plt.ylabel("Average Consumer Prices (% change)")

plt.title("CPI for Mexico")
fig.tight_layout(pad=1.0)
plt.savefig("output/CPI for Mexico.png")

# Plot to analyse the data ==============================================================

sns.relplot(data=cbi_data_long,
            x="Year",
            y="CBI",
            kind="line",
            hue="Country")

plt.ylabel("Central Bank Independence Index")

# Save our plot  

plt.savefig("output/CBI for selected countries.png")

# Merge our data into a single dataframe ================================================

cbi_cpi = pd.merge(cpi_data_long, cbi_data_long, on=["Country", "Year"])

# Convert the 'Year' column to datetime
cbi_cpi["Year"] = pd.to_datetime(cbi_cpi["Year"], format='%Y')

cbi_cpi.head()

fig, ax = plt.subplots()

# Plot both CPI and CBI in a single graph for each country ==============================

ax.set_title('CBI and CPI for Chile')
ax.plot(cbi_cpi[cbi_cpi["Country"] == "Chile"].Year, cbi_cpi[cbi_cpi["Country"] == "Chile"].CPI, linewidth = 1.5, color = 'darkblue')
ax.set_xlabel('Time (years)')
ax.set_ylabel('Consumer Price Index (% change)', color = 'darkblue')
ax.tick_params('y', colors = 'darkblue')

ax2 = ax.twinx()
ax2.plot(cbi_cpi[cbi_cpi["Country"] == "Chile"].Year, cbi_cpi[cbi_cpi["Country"] == "Chile"].CBI, linewidth = 1.5, color = 'darkred')
ax2.set_xlabel('Time (years)')
ax2.set_ylabel('Central Bank Independence Index', color = 'r')
ax2.tick_params('y', colors = 'darkred')

fig.tight_layout(pad=1.0)
plt.savefig("output/CPI and CBI for Chile.png")
plt.show()

fig, ax = plt.subplots()

ax.set_title('CBI and CPI for Peru')
ax.plot(cbi_cpi[cbi_cpi["Country"] == "Peru"].Year, cbi_cpi[cbi_cpi["Country"] == "Peru"].CPI, linewidth = 1.5, color = 'darkblue')
ax.set_xlabel('Time (years)')
ax.set_ylabel('Consumer Price Index (% change)', color = 'darkblue')
ax.tick_params('y', colors = 'darkblue')

ax2 = ax.twinx()
ax2.plot(cbi_cpi[cbi_cpi["Country"] == "Peru"].Year, cbi_cpi[cbi_cpi["Country"] == "Peru"].CBI, linewidth = 1.5, color = 'darkred')
ax2.set_xlabel('Time (years)')
ax2.set_ylabel('Central Bank Independence Index', color = 'r')
ax2.tick_params('y', colors = 'darkred')

fig.tight_layout(pad=1.0)
plt.savefig("output/CPI and CBI for Peru.png")
plt.show()

fig, ax = plt.subplots()

ax.set_title('CBI and CPI for Colombia')
ax.plot(cbi_cpi[cbi_cpi["Country"] == "Colombia"].Year, cbi_cpi[cbi_cpi["Country"] == "Colombia"].CPI, linewidth = 1.5, color = 'darkblue')
ax.set_xlabel('Time (years)')
ax.set_ylabel('Consumer Price Index (% change)', color = 'darkblue')
ax.tick_params('y', colors = 'darkblue')

ax2 = ax.twinx()
ax2.plot(cbi_cpi[cbi_cpi["Country"] == "Colombia"].Year, cbi_cpi[cbi_cpi["Country"] == "Colombia"].CBI, linewidth = 1.5, color = 'darkred')
ax2.set_xlabel('Time (years)')
ax2.set_ylabel('Central Bank Independence Index', color = 'r')
ax2.tick_params('y', colors = 'darkred')

fig.tight_layout(pad=1.0)
plt.savefig("output/CPI and CBI for Colombia.png")
plt.show()

fig, ax = plt.subplots()

ax.set_title('CBI and CPI for Mexico')
ax.plot(cbi_cpi[cbi_cpi["Country"] == "Mexico"].Year, cbi_cpi[cbi_cpi["Country"] == "Mexico"].CPI, linewidth = 1.5, color = 'darkblue')
ax.set_xlabel('Time (years)')
ax.set_ylabel('Consumer Price Index (% change)', color = 'darkblue')
ax.tick_params('y', colors = 'darkblue')

ax2 = ax.twinx()
ax2.plot(cbi_cpi[cbi_cpi["Country"] == "Mexico"].Year, cbi_cpi[cbi_cpi["Country"] == "Mexico"].CBI, linewidth = 1.5, color = 'darkred')
ax2.set_xlabel('Time (years)')
ax2.set_ylabel('Central Bank Independence Index', color = 'r')
ax2.tick_params('y', colors = 'darkred')

fig.tight_layout(pad=1.0)
plt.savefig("output/CPI and CBI for Mexico.png")
plt.show()

# Plot all countries into a single graph =================================================

# Define the plotting functions

def plot_time_series(axes, x, y, color, xlabel, ylabel):
    ''' This function plots a time series. It takes the axes, x-axis values, y-axis values, color, and axis labels. '''
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params(axis='y', colors=color)

def plot_time_series_max(axes, x, y, color, xlabel, ylabel):
    ''' This function plots a time series. It additionally indicates the timestamp with the highest value of the series. '''
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params(axis='y', colors=color)

    # Find the highest point in the data series
    max_point = (x.iloc[np.argmax(y)], max(y))

    max_date = pd.to_datetime(max_point[0])
    
    # Add an arrow and text to the highest point of the CPI
    axes.annotate('Max Point',
                  xy=(max_date, max_point[1]),  # Coordinates of the maximum point
                  xytext=(max_date + pd.Timedelta(days=10), max_point[1] - 0.1),  # Text offset (3 days and 10 units down)
                  textcoords='data',  # Text coordinates
                  arrowprops=dict(arrowstyle='->', color='darkblue'))

# Countries
Countries = ["Peru", "Chile", "Mexico", "Colombia"]

# Plot the picture
fig, axs = plt.subplots(2, 2, figsize=(15, 15))
fig.suptitle('CPI and CBI index for countries of the Pacific Alliance', y=1.02, fontsize=16)

for i, country in enumerate(Countries):
    row = i // 2
    col = i % 2

    ax = axs[row, col]
    ax.set_title(country)

    cbi_cpi_country = cbi_cpi[cbi_cpi["Country"] == country]
    
    plot_time_series(ax, cbi_cpi_country["Year"], cbi_cpi_country["CPI"], 
                        "darkblue", 'Year', 'Consumer Price Index (% change)')
    
    ax2 = ax.twinx()

    plot_time_series_max(ax2, cbi_cpi_country["Year"], cbi_cpi_country["CBI"], 
                        "darkred", 'Year', 'Central Bank Independence Index')

# Save our plot
fig.tight_layout(pad=1.0)
plt.savefig("CPI_CBI_Pacific_Alliance.png", bbox_inches='tight', dpi=300)
plt.show()