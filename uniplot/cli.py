import argparse
from . import parse
from . import analysis
from . import plot
import matplotlib.pyplot as plt

def dump(args):
    """This parses all of the data from the file"""
    for record in parse. uniprot_seqrecords(args.LOC):
        print(record)

def names(args):
    """This parses all of the names from the file"""
    for record in parse. uniprot_seqrecords(args.LOC):
        print(record.name)

def average(args):
"""This retrieves the data for the average"""
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(args.LOC))))

def plot_average_by_taxa(args):
    """This will shows the bar chart of the data by taxa"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(args.LOC), int(args.taxaDepth))
    plot.plot_bar_show(av)
    plt.show()

def plot_average_by_taxa_pie(args):
    """This will show the pie chart of the data by taxa"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(args.LOC), int(args.taxaDepth))
    plot.pieChart(av)
    plt.show()

def cli():
    """This contains all of the parsers and subparsers for the command line interface"""
    ## Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")
    ## This is the optional arguements
    parser.add_argument("-file",dest="LOC", default="uniprot_receptor.xml.gz")
    parser.add_argument("-depth", dest="taxaDepth",default=0)
    subparsers = parser.add_subparsers(help="Sub Command Help")

    ## Add subparsers
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("plot-average-by-taxa").set_defaults(func=plot_average_by_taxa)
    subparsers.add_parser("plot-average-by-taxa-pie").set_defaults(func=plot_average_by_taxa_pie)
    ## Parse the command line
    args = parser.parse_args()
    ## Takes the func argument, which points to the function to call it
    args.func(args)




