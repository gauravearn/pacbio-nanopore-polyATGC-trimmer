# long_read_polyATGC_trimmer
A regular expression based polyATGC trimmer from the long reads or the fastq reads with O(n)1 complexity making it extremely fast and returns a fasta and also a dataframe for the sequence classification and this takes the current as 10 continuous bases (you can change the number in the regular expression and i am releasing a new code which checks all of them) and i timeit and instead of pandas, if you use modin pandas as pd for multicore processing, it parses the GBs of long read file in less than few minutes. 😀 It also returns where the stretch was and how many iterations are needed. A sample on how to run the code is given below. if you are using the long reads for machine learning then it directly returns a dataframe for ingestion to machine leaning.

Best regards,
Gaurav \
Gaurav Sablok \
Frontiers: https://loop.frontiersin.org/people/33293/overview \
ORCID: https://orcid.org/0000-0002-4157-9405 \
WOS: https://www.webofscience.com/wos/author/record/C-5940-2014 \
Github:https://github.com/sablokgaurav \
Linkedin: https://www.linkedin.com/in/sablokgaurav/ 

```
longreadpolyATGCtrimmer("/Users/gauravsablok/Desktop/CodeCheck/fasta_sample_datasets/test_sample_short.fasta",
                              polyATGCstretch_type="G")
	ids	sequences	stretch_count	trimmed_sequences_new
0	>1	GCAGCGTACGTGGTTGGATCAATTAGTGGGGCACATTTGAATCCAG...	[27, 30]	GCAGCGTACGTGGTTGGATCAATTAGTGCACATTTGAATCCAGCTT...
1	>2	GCAGCGTACGTGGTTGGATCAATTAGTGGGGCACATTTGAATCCAG...	[27, 30]	GCAGCGTACGTGGTTGGATCAATTAGTGCACATTTGAATCCAGCTT...
2	>3	GCAGCGTACGTGGTTGGATCAATTAGTGGGGCACATTTGAATCCAG...	[27, 30]	GCAGCGTACGTGGTTGGATCAATTAGTGCACATTTGAATCCAGCTT...
3	>4	CGAAAATTACTTCGGTACAATGCTTGTATACATGGGCAAAGCACAC...	[33, 36]	CGAAAATTACTTCGGTACAATGCTTGTATACATCAAAGCACACGGT...
```
