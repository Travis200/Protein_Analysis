CSC1034: Practical 2
====================

This package allows analysis and display of proteins from Uniprot.

Pipenv run python uniplot.py list - Returns a list of all proteins in the file.

Pipenv run python uniplot.py dump - Returns everything in the file.

Pipenv run python uniplot.py average - Returns the average length of the protein.

Pipenv run python uniplot.py - pipenv run plot_average_by_taxa - Returns the results in a graph for different taxa's.

"-file" Can be used so that the program processes a different file instead of the default "uniprot_receptor.xml.gz".

For example: pipenv run python uniplot.py -file example_file.xml.gz average





