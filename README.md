# long_read_polyATGC_trimmer
A regular expression based polyATGC trimmer from the long reads or the fastq reads extremely fast and returns a fasta and also a dataframe for the sequence classification and this takes the current as 10 continuous bases (you can change the number in the regular expression and i am releasing a new code which checks all of them) and i timeit and instead of pandas, if you use modin pandas as pd for multicore processing, it parses the GBs of long read file in less than few minutes. 😀 It also returns where the stretch was and how many iterations are needed. A sample on how to run the code is given below. if you are using the long reads for machine learning then it directly returns a dataframe for ingestion to machine leaning.

```
longreadpolyATGCtrimmer("/Users/gauravsablok/Desktop/CodeCheck/fasta_sample_datasets/test_sample_short.fasta",
                              polyATGCstretch_type="G")
	ids	sequences	stretch_count	trimmed_sequences_new
0	>1	GCAGCGTACGTGGTTGGATCAATTAGTGGGGCACATTTGAATCCAG...	[27, 30]	GCAGCGTACGTGGTTGGATCAATTAGTGCACATTTGAATCCAGCTT...
1	>2	GCAGCGTACGTGGTTGGATCAATTAGTGGGGCACATTTGAATCCAG...	[27, 30]	GCAGCGTACGTGGTTGGATCAATTAGTGCACATTTGAATCCAGCTT...
2	>3	GCAGCGTACGTGGTTGGATCAATTAGTGGGGCACATTTGAATCCAG...	[27, 30]	GCAGCGTACGTGGTTGGATCAATTAGTGCACATTTGAATCCAGCTT...
3	>4	CGAAAATTACTTCGGTACAATGCTTGTATACATGGGCAAAGCACAC...	[33, 36]	CGAAAATTACTTCGGTACAATGCTTGTATACATCAAAGCACACGGT...
```
Gaurav Sablok \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany
