# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 07:55:15 2024

@author: u23993376
"""

# import matplotlib.pyplot as plt
# import numpy as np

# # Sample data
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# # Create the plot
# plt.figure(figsize=(10, 6), dpi=300)
# plt.plot(x, y, linewidth=2, color='blue')

# # Adjust font size and style
# plt.xlabel('X-axis', fontsize=14)
# plt.ylabel('Y-axis', fontsize=14)
# plt.title('Sine Wave', fontsize=18, fontweight='bold')

# # Customize ticks and grid
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.grid(True, alpha=0.5)

# # Show the plot
# plt.show()


# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Sample lists
# x_values = [1, 2, 3, 4, 5]
# y_values = [2, 4, 5, 4, 5]

# # Create a DataFrame
# df = pd.DataFrame({'x': x_values, 'y': y_values})

# # Create a scatter plot with customizations
# sns.scatterplot(x='x', y='y', data=df, s=100, color='red')
# plt.xlabel('X-axis', fontsize=14)
# plt.ylabel('Y-axis', fontsize=14)
# plt.title('Scatter Plot', fontsize=18)
# plt.grid(True, alpha=0.5)
# plt.figure(figsize=(8, 6), dpi=300)
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load a sample dataset
# tips = sns.load_dataset("tips")

# # Create a Seaborn scatter plot
# sns.scatterplot(x="total_bill", y="tip", data=tips)

# # Customize the Matplotlib background
# plt.figure(figsize=(10, 6), dpi=100)
# plt.gca().set_facecolor('lightgray')  # Set the background color to light gray

# plt.show()

# # Get the current axes
# ax = plt.gca()

# # Set the linewidth of the axes
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['top'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2)   


# # Set the font weight of the axis labels
# plt.xlabel('X-axis', fontsize=14, fontweight='bold')
# plt.ylabel('Y-axis', fontsize=14, fontweight='bold')

# # Set the font weight of the tick labels
# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontweight('bold')
# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_fontweight('bold') 


# Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 5, 4, 5]

# plt.figure(figsize=(10, 6), dpi=300)
# plt.plot(x, y, linewidth=2, color='blue')

# Create the plot
#plt.plot(x, y)

# plt.figure(dpi=300)
# plt.plot(x, y, linewidth=3, color='blue')

# # Get the current axes
# ax = plt.gca()

# # Set the linewidth of the axes
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['top'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2) 


# # Set the font weight of the axis labels
# plt.xlabel('X-axis', fontsize=14, fontweight='bold')
# plt.ylabel('Y-axis', fontsize=14, fontweight='bold')

# # Set the font weight of the tick labels
# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontweight('bold')
# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_fontweight('bold') 
    
# ax.tick_params(axis='both', width=2, length=6)   
    
# # Set the font weight of the axis labels
# plt.xlabel('X-axis', fontsize=14, fontweight='bold')
# plt.ylabel('Y-axis', fontsize=14, fontweight='bold')

# # Show the plot
# plt.show()

# # list_PA_PM25_raw = []
# # list_PA_RH_raw = []
# # list_PA_TEMP_F_raw = []
# # list_PA_TEMP_C_raw = []

# # list_PA_timestamp_utc_raw = []
# # list_PA_timestamp_sast_raw = []

# # list_PA_PM25_timestamp_sast_hour = []
# # list_PA_RH_timestamp_sast_hour = []
# # list_PA_TEMP_C_timestamp_sast_hour = []
# #list_PA_PM25_avg_hour - hourly PM data for PA
# # list_PA_timestamp_sast_hour - timestamp data for PA
# #list_PM - hourly PM data for PA 
# #list_new_timestamp - timestamp for SAAQIS reference


## Wel PA
# x1 = list_PA_timestamp_sast_hour[0:679]
# y1 = list_PA_PM25_avg_hour[0:679]

# ## Wel Ref
# x2 = new_timestamp[0:679]
# y2 = list_PM[0:679]

# x1 = list_PA_timestamp_sast_hour[0:679]
# y1 = list_PA_PM25_avg_hour[0:679]

# ## Wel Ref
# x2 = new_timestamp[0:679]
# y2 = list_PM[0:679]



# plt.figure(figsize=(10, 6), dpi=300)
# plt.plot(x, y, linewidth=2, color='blue')

# Create the plot
#plt.plot(x, y)

# plt.figure(dpi=300)
# plt.plot(x1, y1, linewidth=3, color='blue')
# plt.plot(x2, y2, linewidth=3, color='red')
# #plt.ylim(0, 40)
# #start_date = datetime.datetime(2018, 10, 1, 1)
# #end_date = datetime.datetime(2018, 10, 31, 23)
# #ax.set_xlim(start_date, end_date)

# # Get the current axes
# ax = plt.gca()

# # Set the linewidth of the axes
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['top'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2) 


# # Set the font weight of the axis labels
# plt.xlabel('X-axis', fontsize=14, fontweight='bold')
# plt.ylabel('Y-axis', fontsize=14, fontweight='bold')

# plt.xticks(rotation=45)

# # Set the font weight of the tick labels
# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontweight('bold')
# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_fontweight('bold') 
    
# ax.tick_params(axis='both', width=2, length=6)   
    
# # Set the font weight of the axis labels
# plt.xlabel('X-axis', fontsize=14, fontweight='bold')
# plt.ylabel('Y-axis', fontsize=14, fontweight='bold')

# # Show the plot
# plt.show()

# import matplotlib.pyplot as plt

# # Create a figure and axis
# fig, ax = plt.subplots()

# # Plot a simple line chart (optional)
# x = [1, 2, 3]
# y = [2, 4, 6]
# ax.plot(x, y)

# #plt.xlabel(r'$x_{\mathbf{subscript}}$')
# # Add a text label with bold subscript
# #ax.text(1.5, 5, r'PM$_\mathbf{2.5}$', fontsize=14, fontweight='bold')

# plt.show()
