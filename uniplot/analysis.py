def average_len(records):
    count = 0
    total_Length = 0
    for i in records:
        count = count + 1
        total_Length = total_Length + len(i.seq)
        average = total_Length/count
    return average

def average_len_taxa(records):
    """Returns the average length for the top level taxa"""
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][0]
        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
