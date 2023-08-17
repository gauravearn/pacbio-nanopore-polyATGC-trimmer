import re
import pandas as pd
def longreadpolyATGCtrimmer(infile, polyATGCstretch_type=None):
    """summary_line
    a long read trimmer, given the long read fasta base
    quality check, it will check for the longest stretch of 
    polyATGCstretch_type as selected and will remove that 
    stretch and returns a dataframe which can be easily 
    converted into a fasta file. 
    Keyword arguments:
    argument -- description
    infile = fasta file of the long reads
    Return: return_description
    return a dataframe for direct ingestion
    """
    if polyATGCstretch_type == "A":
        read_long_reads = list(filter(None,[x.strip() for x in open(infile).readlines()]))
        long_read_conversion = {}
        for i in read_long_reads:
            if i.startswith(">"):
                path = i.strip()
                if i not in long_read_conversion:
                    long_read_conversion[i] = ""
                    continue
            long_read_conversion[path] += i.strip()
        ids = list(long_read_conversion.keys())
        sequences = list(long_read_conversion.values())
        long_read_dataframe = pd.DataFrame([(i,j)for i,j in zip(ids, sequences)]). \
                                          rename(columns = {0: "ids", 1: "sequences"})
        long_read_dataframe["stretch_count"] = long_read_dataframe["sequences"]. \
                                               apply(lambda n: re.findall(r'[0-9][0-9]',\
                                                            str(re.search(r"[aA]{10}",n)).\
                                                                        split(";")[1].split("match")[0]))
        counts = [list(map(int,i)) for i in (long_read_dataframe["stretch_count"].to_list())]
        sequences = long_read_dataframe["sequences"].to_list()
        long_read_dataframe["trimmed_sequences_new"] = pd.DataFrame([sequences[i][:counts[i][0]]+ \
                                                sequences[i][counts[i][1]:] for i in range(len(counts))])
        return long_read_dataframe
    if polyATGCstretch_type == "G":
        read_long_reads = list(filter(None,[x.strip() for x in open(infile).readlines()]))
        long_read_conversion = {}
        for i in read_long_reads:
            if i.startswith(">"):
                path = i.strip()
                if i not in long_read_conversion:
                    long_read_conversion[i] = ""
                    continue
            long_read_conversion[path] += i.strip()
        ids = list(long_read_conversion.keys())
        sequences = list(long_read_conversion.values())
        long_read_dataframe = pd.DataFrame([(i,j)for i,j in zip(ids, sequences)]). \
                                          rename(columns = {0: "ids", 1: "sequences"})
        long_read_dataframe["stretch_count"] = long_read_dataframe["sequences"]. \
                                               apply(lambda n: re.findall(r'[0-9][0-9]',\
                                                            str(re.search(r"[gG]{10}",n)).\
                                                                        split(";")[1].split("match")[0]))
        counts = [list(map(int,i)) for i in (long_read_dataframe["stretch_count"].to_list())]
        sequences = long_read_dataframe["sequences"].to_list()
        long_read_dataframe["trimmed_sequences_new"] = pd.DataFrame([sequences[i][:counts[i][0]]+ \
                                                sequences[i][counts[i][1]:] for i in range(len(counts))])
        return long_read_dataframe
    if polyATGCstretch_type == "T":
        read_long_reads = list(filter(None,[x.strip() for x in open(infile).readlines()]))
        long_read_conversion = {}
        for i in read_long_reads:
            if i.startswith(">"):
                path = i.strip()
                if i not in long_read_conversion:
                    long_read_conversion[i] = ""
                    continue
            long_read_conversion[path] += i.strip()
        ids = list(long_read_conversion.keys())
        sequences = list(long_read_conversion.values())
        long_read_dataframe = pd.DataFrame([(i,j)for i,j in zip(ids, sequences)]). \
                                          rename(columns = {0: "ids", 1: "sequences"})
        long_read_dataframe["stretch_count"] = long_read_dataframe["sequences"]. \
                                               apply(lambda n: re.findall(r'[0-9][0-9]',\
                                                            str(re.search(r"[tT]{10}",n)).\
                                                                        split(";")[1].split("match")[0]))
        counts = [list(map(int,i)) for i in (long_read_dataframe["stretch_count"].to_list())]
        sequences = long_read_dataframe["sequences"].to_list()
        long_read_dataframe["trimmed_sequences_new"] = pd.DataFrame([sequences[i][:counts[i][0]]+ \
                                                sequences[i][counts[i][1]:] for i in range(len(counts))])
        return long_read_dataframe
    if polyATGCstretch_type == "G":
        read_long_reads = list(filter(None,[x.strip() for x in open(infile).readlines()]))
        long_read_conversion = {}
        for i in read_long_reads:
            if i.startswith(">"):
                path = i.strip()
                if i not in long_read_conversion:
                    long_read_conversion[i] = ""
                    continue
            long_read_conversion[path] += i.strip()
        ids = list(long_read_conversion.keys())
        sequences = list(long_read_conversion.values())
        long_read_dataframe = pd.DataFrame([(i,j)for i,j in zip(ids, sequences)]). \
                                          rename(columns = {0: "ids", 1: "sequences"})
        long_read_dataframe["stretch_count"] = long_read_dataframe["sequences"]. \
                                               apply(lambda n: re.findall(r'[0-9][0-9]',\
                                                            str(re.search(r"[cC]{10}",n)).\
                                                                        split(";")[1].split("match")[0]))
        counts = [list(map(int,i)) for i in (long_read_dataframe["stretch_count"].to_list())]
        sequences = long_read_dataframe["sequences"].to_list()
        long_read_dataframe["trimmed_sequences_new"] = pd.DataFrame([sequences[i][:counts[i][0]]+ \
                                                sequences[i][counts[i][1]:] for i in range(len(counts))])
        return long_read_dataframe
