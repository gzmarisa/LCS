# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 05:46:30 2024

@author: u23993376
"""


import matplotlib.pyplot as plt
import numpy as np

# '--': Dashed line
# ':': Dotted line
# '-.': Dash-dot line


## Wel PA
## Wel Ref 

# merge_timestamp
# merge_PA_PM
# merge_PA_RH 
# merge_PA_TEMP_C 
# merge_SAAQIS_PM  
# merge_PA_PM_correction

# #full time range 

# # Wel PA - uncorrected
# x0 = merge_timestamp
# y0 = merge_PA_PM

# # Wel PA - corrected 
# x1 = merge_timestamp
# y1 = merge_PA_PM_correction

# ## Wel Ref
# x2 = merge_timestamp
# y2 = merge_SAAQIS_PM

# ## October 1 2018 - October 31
# #[0:550] - whole month
# # [0:142] - whole week 
# # Wel PA - uncorrected
x0 = merge_timestamp[0:142]
y0 = merge_PA_PM[0:142]

# Wel PA - corrected 
x1 = merge_timestamp[0:142]
y1 = merge_PA_PM_correction[0:142]

## Wel Ref
x2 = merge_timestamp[0:142]
y2 = merge_SAAQIS_PM[0:142]

# # Create the plot

# plt.figure(dpi=300)
# plt.figure(figsize=(10, 6), dpi=300)
# plt.plot(x0, y0, linewidth=3, color='blue', linestyle=':')
# plt.plot(x1, y1, linewidth=3, color='blue')
# plt.plot(x2, y2, linewidth=3, color='red')



# #plt.ylim(0, 20)


# # Get the current axes
# ax = plt.gca()

# # Set the linewidth of the axes
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['top'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2) 

# plt.xticks(rotation=45)

# # Set the font weight of the tick labels
# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontweight('bold')
# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_fontweight('bold') 
    
# ax.tick_params(axis='both', width=2, length=6)   

# ## plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# # Set the font weight of the axis labels
# plt.xlabel('Time (SAST)', fontsize=14, fontweight='bold')
# plt.ylabel('PM$_{2.5}$ ($\mu$g/m$^3$)', fontsize=14, fontweight='bold')

# # Show the plot
# plt.show()

## Centurion PA
## TM Ref
#full time range 

#Cent PA - corrected 
# x1 = merge_timestamp
# y1 = merge_PA_PM_correction

# ## Wel Ref
# x2 = merge_timestamp
# y2 = merge_SAAQIS_PM

# August 1 2020 - August 31 2020
#2020/08/1 – 2020/08/31
#[4787:5029]
#Cent PA - corrected 
# x1 = merge_timestamp[4114:4854]
# y1 = merge_PA_PM_correction[4114:4854]


# # TM Ref
# x2 = merge_timestamp[4114:4854]
# y2 = merge_SAAQIS_PM[4114:4854]

# # # Create the plot

# #wel
# plt.figure(dpi=300)
# plt.figure(figsize=(10, 6), dpi=300)
# plt.plot(x0, y0, linewidth=3, color='blue', linestyle=':', alpha=0.6)
# plt.plot(x1, y1, linewidth=3, color='blue')
# plt.plot(x2, y2, linewidth=3, color='red')

# #cent
# plt.figure(dpi=300)
# plt.figure(figsize=(10, 6), dpi=300)
# #plt.plot(x0, y0, linewidth=3, color='blue', linestyle=':', alpha=0.6)
# plt.plot(x2, y2, linewidth=3, color='red')
# plt.plot(x1, y1, linewidth=3, color='blue')

# #plt.ylim(0, 20)


# # # Get the current axes
# ax = plt.gca()

# # Set the linewidth of the axes
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['top'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2)

# plt.xticks(rotation=45)

# # Set the font weight of the tick labels
# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontweight('bold')
# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_fontweight('bold')

# ax.tick_params(axis='both', which='major', labelsize=14)
# ax.tick_params(axis='both', width=2, length=6)


# #plt.xlabel(r'$x_{\mathbf{subscript}}$')
# # Add a text label with bold subscript
# #ax.text(1.5, 5, r'PM$_\mathbf{2.5}$', fontsize=14, fontweight='bold')
# ## plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# # Set the font weight of the axis labels
# plt.xlabel('Time (SAST)', fontsize=14, fontweight='bold')
# plt.ylabel(r'PM$_\mathbf{2.5}$ ($\mathbf{\mu}$g/m$^\mathbf{3}$)',
#            fontsize=14, fontweight='bold')

# # Show the plot\
# plt.show()

#import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6), dpi=300)
#plt.figure(dpi=300)

plt.scatter(y_test, y_test_pred, color='red', label='Test Data')
plt.scatter(y_train, y_train_pred, color='blue', label='Training Data')


plt.plot([min(y), max(y)], [min(y), max(y)], color='black', linestyle='--')

# plt.scatter(y_train, y_train_pred, color='blue', label='Training Data')
# plt.scatter(y_test, y_test_pred, color='red', label='Test Data')


ax = plt.gca()

# Set the linewidth of the axes
ax.spines['bottom'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)

#plt.xticks(rotation=45)

# Set the font weight of the tick labels
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

ax.tick_params(axis='both', which='major', labelsize=14)
ax.tick_params(axis='both', width=2, length=6)

# plt.xlabel("True Values")
# plt.ylabel("Predicted Values")
# plt.title("True vs Predicted Values")
# plt.legend()


#plt.xlabel(r'$x_{\mathbf{subscript}}$')
# Add a text label with bold subscript
#ax.text(1.5, 5, r'PM$_\mathbf{2.5}$', fontsize=14, fontweight='bold')
## plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# Set the font weight of the axis labels
plt.xlabel('True Values', fontsize=14, fontweight='bold')
plt.ylabel('Predicted Values', fontsize=14, fontweight='bold')



# # Show the plot\
# plt.show()



# plt.xlabel("True Values")
# plt.ylabel("Predicted Values")
# plt.title("True vs Predicted Values")
# plt.legend()

# # Add a line of best fit (optional)


# plt.show()
