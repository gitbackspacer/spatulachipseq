# spatulachipseq
Helper scripts to find the common gene in the ChIP-seq study

Comparing ChIP-seq data with the published RNA-seq data
----------------------------------------------------------


- To identify the overlap, we compared our ChIP-seq–enriched SPT target genes with the RNA-Seq–derived SPT target gene list from Bernal-Gallardo et al. (2023), titled “Novel Roles of SPATULA in the Control of Stomata and Trichome Number, and Anthocyanin Biosynthesis”, published in Plants (Basel), 12(3):596, doi: 10.3390/plants12030596; PMID: 36771679; PMCID: PMC9919660.
- We downloaded the supplementary `plants-2165966-supplementary.xlsx` containing the gene list from the study.
- The gene list from the study (n = 3,692 genes) was saved as plants-2165966-target-gene-spt-listing.txt.
- We find the common gene between our study or the list of gene by TAIR10 gene ids.


```python

- The input files:

md5sum
--------
c177c2cff46aed92123ee73101b3e579  chipseq_gene_hit_rank.txt
7892e8f5f8e07ca72d6214dc65a7bb47  thalemine_summary.csv
38ec3cc59a4b392e1dfef526d3019841  plants-2165966-target-gene-spt-listing.txt

- code:
c4bd4f676a30257d2528871ff81887ae  common_genes_rnaseq_chipseq_spt_targets.py

> output:
2e88310405ec339b6742d8122f653805  chipseq_rnaseq_intersection-spt-targets-ath.tab

The file is converted to excel:
  338db3e1623e96eb045ad748667e013c  chipseq_rnaseq_intersection-spt-targets.tab.xls


Citing: Bernal-Gallardo JJ, Zuñiga-Mayo VM, Marsch-Martinez N, de Folter S. Novel Roles of SPATULA in the Control of Stomata and Trichome Number, and Anthocyanin Biosynthesis. Plants (Basel). 2023 Jan 29;12(3):596. doi: 10.3390/plants12030596. PMID: 36771679; PMCID: PMC9919660.

```
