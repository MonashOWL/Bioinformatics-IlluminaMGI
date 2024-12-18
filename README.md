# Bioinformatics-IlluminaMGI
_SOPs or documents related to Illumina/MGI sequencing bioinformatics pipeline._

The bioinformatics SOPs written over here assumes that you already have access to Monash MASSIVE account and project (https://www.massive.org.au/index.html). If you use other cluster computing systems (or do not have access to one), please feel free to modify the script to suit yours. 

For the guidelines, I wrote the script based on my MASSIVE account, project, and directory, so please modify the codes as per yours.

In terms of directory within the scripts, I will be replacing the project folder directory (e.g., _/fs04/hj18/_) with _~/_ to avoid confusion. You can name your directory based on your preference, it will not cause any issue with running of scripts.

<ins>**16S sequencing**</ins>

You can start off by looking at the following documentations:
1) Setting up WINSCP and PUTTY (_WINSCP and PUTTY setup_22032024.docx_)
2) FIGARO and FASTP setup (_FIGARO and FASTP setup_15032024.docx_) - located in **16S** folder
3) Illumina sequencing pipeline (_Illumina sequence pipeline_03062024.docx_) - located in **16S** folder
4) Leave one out at a time, LOO (_Leave one out at a time (LOO) pipeline_17032024.docx_) - located in **16S** folder
5) Source variability, i.e., assessing source library based on number of included source samples (_Source variability pipeline_30102024.docx_) - located in **16S** folder

For these pipeline, at minimum you would need to have Python (for LOO (4) and source variability (5)) (https://www.python.org/), QIIME2 (https://qiime2.org/) and SourceTracker (https://github.com/caporaso-lab/sourcetracker2). These software are freely available to be used.
