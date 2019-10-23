def average_len(records):
    count = 0
    total_Length = 0
    for i in records:
        count = count + 1
        total_Length = total_Length + len(i.seq)
        average = total_Length/count
    return average


