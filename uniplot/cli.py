import argparse
from . import parse
from . import analysis
from . import plot
import matplotlib.pyplot as plt

def dump(args):
    for record in parse. uniprot_seqrecords(args.LOC):
        print(record)

def names(args):
    for record in parse. uniprot_seqrecords(args.LOC):
        print(record.name)

def average(args):
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(args.LOC))))

def plot_average_by_taxa(args):
    av = analysis.average_len_taxa2(parse.uniprot_seqrecords(args.LOC), int(args.taxaDepth))
    plot.pieChart(av)
    ##plot.plot_bar_show(av)
    plt.show()

def cli():
    ## Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")
    ## This is the optional arguements
    parser.add_argument("-file",dest="LOC", default="uniprot_receptor.xml.gz")
    parser.add_argument("-taxa", dest="taxaDepth",default=0)
    subparsers = parser.add_subparsers(help="Sub Command Help")

    ## Add subparsers
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("plot_average_by_taxa").set_defaults(func=plot_average_by_taxa)
    ## Parse the command line
    args = parser.parse_args()
    ## Takes the func argument, which points to the function to call it
    args.func(args)




