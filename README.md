CSC1034: Practical 2
====================

This package allows analysis and display of proteins from Uniprot. The programme parses the data from the uniprot file  
and then presents the data in variety of ways depending on the users needs. The command line interface is explained  
below. 

```Pipenv run python uniplot.py list``` - Returns a list of all protein names.

```Pipenv run python uniplot.py dump``` - Returns everything in the file.

```Pipenv run python uniplot.py average``` - Returns the average length of the protein.

```Pipenv run python uniplot.py``` - pipenv run plot-average-by-taxa - Returns the results in a bar chart for  
different taxas. 

`````-file````` Can be used so that the program processes a different file instead of the "uniprot_receptor.xml.gz".  
For example: ```pipenv run python uniplot.py -file example_file.xml.gz average```

```pipenv run python uniplot.py plot-average-by-taxa-pie``` - Returns the results in a pie chart for different taxas.

````-depth```` can be used to specify the level of taxa (the top level is zero). If no level is specified the default is zero.  
For example: ```pipenv run python uniplot.py -depth 1 plot-average-by-taxa-pie```








