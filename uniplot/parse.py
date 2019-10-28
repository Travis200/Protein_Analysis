import gzip
from Bio import SeqIO

def uniprot_seqrecords(file_location):
    """This unzips and parses through the file"""
    records = []

    handle = gzip.open(file_location)
    for record in SeqIO.parse(handle, "uniprot-xml"):
        records.append(record)

    return records
