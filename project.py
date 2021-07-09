import pandas as pd
import numpy as np
import git 
import matplotlib.pyplot as plt
from tabulate import tabulate

from utils.utils import *

fo_md = "project.md"
fo_tex = "project.tex"
project_report = Report(fo_md, fo_tex)

project_report.w_section("My First Section")
project_report.w_lines ("Always start a section with some explanation about its contents")
project_report.w_subsection("My First Subsection")
project_report.w_lines ("Always start a subsection with some explanation about its contents")
project_report.w_subsubsection("My First Subsubsection")
project_report.w_lines ("Always start a subsubsection with some explanation about its contents")

# generate some data
data_x = np.linspace(0,10,20)
data_y = np.sin(data_x)

# plot your data
fig = plt.figure()
plt.plot(data_x, data_y)
plt.title("My Plot based on {} data points".format(len(data_x)))
fo_plot = "img/My_Plot.png"
plt.xlabel("Always label your x-axis: linspace of x values")
plt.ylabel("Always label your y-axis: sin(x)")
fig.set_size_inches(7, 4)
print("Writing {}".format(fo_plot))
fig.savefig(fo_plot)

# add your plot to your documentation
project_report.w_image("An example plot", fo_plot)

# put your data in a dataframe
df_table = pd.DataFrame({"data_x" : data_x, "data_y" : data_y})
# add your table to your documentation
project_report.w_table("An example table", df_table)

# ALWAYS do this last
project_report.w_tail()
