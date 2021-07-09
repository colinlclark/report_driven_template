# report_driven_template
Report Driven Template for experiments

# Setup Instructions
## fork THIS repo
1. navigate to
   [https://github.com/bwbellmath/report_driven_template.git](https://github.com/bwbellmath/report_driven_template.git)
2. in the top right corner, click "Fork" and create a fork under your
own github account. 
![Fork
Button](https://github.com/bwbellmath/report_driven_template/blob/main/img/fork_button.jpg)
3. In your fork of *report_driven_template* click the "Code" button
   and copy the URL to *clone* the repo into a directory on your
   computer. 
4. clone the repo onto your computer -- note that `git clone` *creates*
   a folder with the name of the git repo in the directory where it is
   run, so if are in `/usr/you/code` and you run `clone clone
   .../report_driven_template.git` it will create a new directory
   `/usr/you/code/report_driven_template` which will now contain your
   local copy of the code. 
   ~~~~
   cd
   cd code
   git clone https://github.com/[your git username]/report_driven_template.git
   ~~~~
5. navigate to the directory you just pulled your fork of the repo
   into: `cd report_driven_template`

## software dependencies
1. install texlive from
   [here.](https://www.tug.org/texlive/acquire-netinstall.html)
2. install anaconda from
   [here](https://docs.anaconda.com/anaconda/install/index.html)
3. install git from
   [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## pip and conda
1. `conda install numpy pandas gitpython tabulate matplotlib`

## running the code, committing and pushing to github
0. Edit `latex_header.tex` to add yourself as `\author` and change the title
1. `python report.py`
2. `latex report.tex`
3. `git add img/*.png` if you have added any plot images
4. `git commit -am "[describe what you have done]"`
5. `git push`

## Code Development Suggestions:
1. Print all of your results to the output files -- never manually
   generate an important result -- never consider an experiment
   *finished* until it is securely documented in the `project.pdf` or
   `project.md` file on github. 
2. Add commentary as you go, don't generate a *naked* result and move
   on to the next experiment without wrapping it up by writing some
   notes about how you arrived at that result and your interpretation
   of it. 
3. Commit `git commit -am "brief note"` and push `git push` your code
   *often* -- this is your "save" procedure for your project. 

# files: 
##  `.gitignore`
File where extensions and files that should *not* be included in the
git repo are listed -- preconfigured for python, LaTeX, emacs, and vim

##  `project.py`
Script where your experiment is performed

##  `project.tex`
LaTeX document that is *produced* by project.py and stored in git for
reuse later. 
##  `latex_header.tex`
Header for your latex document -- preconfigured with everything you
need (and way more...)

##  `project.pdf`
PDF file created for `project.tex` stored in git for convenience

##  `project.md`
Markdown formatted output for your 

##  `utils/utils.py`
File where functions that are shared among multiple experiment scripts
can be stored. All of the .markdown and .pdf print things live here. 

##  `img/`
Directory where output images will be stored

##  `data/`
Directory where ourput data will be stored -- you can change this to a
location outside of the repo if you'll be producing *very* large files.

##  `img/plot.png`
The Image file produced by our particular block of code. 


