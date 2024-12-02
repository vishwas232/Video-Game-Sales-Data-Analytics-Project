# One single loop for eda univariate analysis

# Viz Libraries

import matplotlib.pyplot as plt
import seaborn as sns

from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
import plotly.express as px

from simple_colors import *

import warnings
warnings.filterwarnings("ignore")


def univariate(data):
    for col in data.columns:

        if data[col].dtype == 'object':
            print(green("Column:", ['bold']), black(col, ['bold']))
            print(blue("=============================================================", ['bold']))
            print()
            print(blue("*****************************************", ['bold']))
            print(black("          Descriptive Stats              ", ['bold']))
            print(blue("*****************************************", ['bold']))
            print()

            # pandas inbuilt functions for unique, nunique, fdt
            print(magenta("Number of Unique Classes:", ['bold']), data[col].nunique())
            print()
            print(magenta("Unique Classes:", ['bold']))
            print(data[col].unique())
            print()
            print(magenta("Value Counts of each class (FDT):", ['bold']))
            print(data[col].value_counts())  # FDT
            print()
            print(magenta("Each Class percentage:", ['bold']))
            print(round((data[col].value_counts() / len(data)) * 100,2))  # FDT Percentage
            print()
            print(magenta("Mode value:", ['bold']), data[col].mode()[0])
            print()
            print(cyan("*****************************************", ['bold']))
            print(black("      Visual Analysis - Pie Chart      ", ['bold']))
            print(cyan("*****************************************", ['bold']))
            print()
            print(black("Top Catgeories:", ['bold']))
            
            # Considering only top 10 categories for pie chart
            index = data[col].value_counts().sort_values(ascending=False)[0:10].index
            vals = data[col].value_counts().sort_values(ascending=False)[0:10].values
            fig = px.pie(names=index, values=vals, width=700, height=400)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(showlegend=False)
            fig.show()
            print()
            

                
        elif data[col].dtype == 'datetime64[ns]':

            print(yellow("Column Name:", ['bold']), col)
            print("============================================================")
            print()
            print(blue("*****************************************", ['bold']))
            print(black("          Descriptive Stats              ", ['bold']))
            print(blue("*****************************************", ['bold']))
            print()

            # pandas inbuilt functions stats

            # Measure of Spread
            print(magenta("Min & Max:", ['bold']),(data[col].min(), data[col].max()))
            print(magenta("Data belongs to Time Period :", ['bold']),data[col].min().year, "to", data[col].max().year)
            print(magenta("Value Counts of each Year/Month/Date:", ['bold']))
            print(data[col].dt.year.value_counts())  # FDT
            print()
            print(cyan("********************************************************",['bold']))
            print(black(" Visual Analysis - Line Chart",['bold']))
            print(cyan("********************************************************",['bold']))
            print()
            
            print("Select Values column to Display With Time:")
            print([col for col in data.columns if data[col].dtype!=object])
            refcol = input()
            px.line(data, x=col, y=refcol, width=650, height=350).show()

        elif data[col].dtype == 'int32' or data[col].dtype == 'int64':
            print(yellow("Column Name:", ['bold']), col)
            print("============================================================")
            print()
            print(blue("*****************************************", ['bold']))
            print(black("          Descriptive Stats              ", ['bold']))
            print(blue("*****************************************", ['bold']))
            print()

            # pandas inbuilt functions for the mct, ms stats

            # Measure of Central Tendancy
            print(magenta("Mean:", ['bold']), round(data[col].mean()))
            print(magenta("Median:", ['bold']), round(data[col].median()))
#             print("Mode of the {} Col:".format(col),data[col].mode()[0])  # optional
            print()
            # Measure of Spread
            print(magenta("Min & Max:", ['bold']),(data[col].min(), data[col].max()))
            print(magenta("Standard Deviation:", ['bold']),round(data[col].std()))
            print()
            # Short Summary
            print(magenta("Summary & Quantiles:", ['bold']))
            print(round(data[col].describe()))
            print()
            # Measure of Symmetry
            print(magenta("Skewness:", ['bold']), round(data[col].skew()))
            print(magenta("Kurtosis:", ['bold']), round(data[col].kurt()))
            print()
            print(cyan("********************************************************",['bold']))
            print(black(" Visual Analysis - Distplot (Histogram + Desnsity plot) ",['bold']))
            print(cyan("********************************************************",['bold']))
            print()
            plt.figure(figsize=(4, 3))
            sns.distplot(data[col])
            plt.show()
            
        elif data[col].dtype == 'float32' or data[col].dtype == 'float64':
            
            print(yellow("Column Name:", ['bold']), col)
            print("============================================================")
            print()
            print(blue("*****************************************", ['bold']))
            print(black("          Descriptive Stats              ", ['bold']))
            print(blue("*****************************************", ['bold']))
            print()

            # pandas inbuilt functions for the mct, ms stats

            # Measure of Central Tendancy
            print(magenta("Mean:", ['bold']), round(data[col].mean(), 2))
            print(magenta("Median:", ['bold']), data[col].median())
            print("Mode of the {} Col:".format(col),data[col].mode()[0])  # optional
            print()
            # Measure of Spread
            print(magenta("Min & Max:", ['bold']),(data[col].min(), data[col].max()))
            print(magenta("Standard Deviation:", ['bold']),round(data[col].std(), 2))
            print()
            # Short Summary
            print(magenta("Summary & Quantiles:", ['bold']))
            print(round(data[col].describe(), 2))
            print()
            # Measure of Symmetry
            print(magenta("Skewness:", ['bold']), round(data[col].skew(), 2))
            print(magenta("Kurtosis:", ['bold']), round(data[col].kurt(), 2))
            print()
            print(cyan("********************************************************",['bold']))
            print(black(" Visual Analysis - Distplot (Histogram + Desnsity plot) ",['bold']))
            print(cyan("********************************************************",['bold']))
            print()
            plt.figure(figsize=(4, 3))
            sns.distplot(data[col])
            plt.show()