import pandas as pd
import numpy as np
import git 

from tabulate import tabulate

repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha
origin_url = repo.remotes["origin"].url


# summary.md generator
class Report(object):
  def __init__(self, fo_md, fo_tex):
    self.fo_md = fo_md
    self.fo_tex = fo_tex
    self.first = True
    # read header file from repo
  
    with open("latex_header.tex", "r") as file_header:
      self.header = file_header.readlines()


  # print document header for latex document 
  def summary_print(self, desc, desc_md, desc_tex):
    print("{}\n".format(desc))
    if (self.first):
      desc_head = self.header
      print("{}\n".format(desc_md), file=open(self.fo_md,"w"))
      # make sure header is written first to latex file
      print("{}\n".format(desc_head), file=open(self.fo_tex,"w"))
      print("{}\n".format(desc_tex), file=open(self.fo_tex,"w"))
      self.first = False
    else:
      print("{}\n".format(desc_md), file=open(self.fo_md,"a"))
      print("{}\n".format(desc_tex), file=open(self.fo_tex,"a"))

  def w_section(self, line):
    desc = line
    desc_md = "# {}".format(line)
    desc_tex = "\section{{ {} }}".format(line)
    self.summary_print(desc, desc_md, desc_tex)

  def w_subsection(self, line):
    desc = line
    desc_md = "## {}".format(line)
    desc_tex = "\subsection{{ {} }}".format(line)
    self.summary_print(desc, desc_md, desc_tex)

  def w_subsubsection(self, line):
    desc = line
    desc_md = "\n ### {}".format(line)
    desc_tex = "\\ \n \subsubsection{{ {} }}".format(line)
    self.summary_print(desc, desc_md, desc_tex)

  def w_lines(self, line):
    desc = line
    desc_md = line
    desc_tex = line
    self.summary_print(desc, desc_md, desc_tex)
  # TODO : put both image and table in a latex figure
  def w_image(self, line, f_img):
    # get url from git remote origin
    url = origin_url[0:-4]+"/blob/main/"

    desc = "{} \n Image URL : {}{}\n Image DIR : {}".format(line, url, f_img, f_img)
    desc_md = desc + "![{}]({}{})".format(f_img, url, f_img)
    desc_tex = "\includegraphics[width=0.9\textwidth]{{{}}}".format(f_img)
    self.summary_print(desc, desc_md, desc_tex)

  def w_table(self, line, df_table):
    desc = line
    desc_md = line + "\n" + tabulate(df_table, tablefmt="pipe", headers="keys") + "\n"    
    desc_tex = line + "\n" + tabulate(df_table, tablefmt="latex", headers="keys") + "\n"
    self.summary_print(desc, desc_md, desc_tex)
  # make sure to do this last
  def w_tail(self):
    tail = "\end{{document}}"
    print(tail, file=open(self.fo_tex,"a"))

