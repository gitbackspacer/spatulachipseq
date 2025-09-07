"""
Find common genes between:

Column 'C' of:
   Copy of common-gene_hit_ranking_by_IDR_415_by_replicates-GOterms.tab (1)
   --> chipseq_gene_hit_rank.txt
   chip_targets: 6639
And
column 'A' of
   'plants-2165966-supplementary.xlsx' --> plants-2165966-target-gene-spt.txt
   plants_spt_targets: 3692

$ md5sum *
7caf5c764455f454260e16ca3d0cb79b  README-spt.md

c177c2cff46aed92123ee73101b3e579  chipseq_gene_hit_rank.txt
c3b426f15979bb8677d82954ffc17efd  plants-2165966-supplementary.xlsx
38ec3cc59a4b392e1dfef526d3019841  plants-2165966-target-gene-spt-listing.txt
7892e8f5f8e07ca72d6214dc65a7bb47  thalemine_summary.csv

2e88310405ec339b6742d8122f653805  chipseq_rnaseq_intersection-spt-targets-ath.tab
af64da1e057aa92f6f2a8180e385f151  common_genes_rnaseq_chipseq_spt_targets.py

$
"""


import csv
import sys

def load_gene_set(filename, comment_char="#"):
    """Load gene IDs from a file into a set, ignoring short lines and comments."""
    gene_order = []
    with open(filename) as infile:
        for line in infile:
            if line.startswith(comment_char):
                continue
            this_gene = line.strip()
            if len(this_gene) > 1:
                assert this_gene.startswith("AT")
                gene_order.append(this_gene)
    return gene_order


def thalemine_description_data():
    details = {}
    with open("thalemine_summary.csv", newline="\n", encoding="utf-8") as thale:
        # Use csv.DictReader with space delimiter and quotechar
        reader = csv.DictReader(thale, delimiter=" ", quotechar='"')
        for row in reader:
            details[row["input"]] = {
                "Gene_symbol": row["symbol"],
                "TairAliases": row["tairAliases"],
                "ShortDescription": row["tairShortDescription"],
                "ComputationalDescription": row["tairComputationalDescription"],
            }
    return details


if __name__ == "__main__":

    chip_gene_order = load_gene_set("chipseq_gene_hit_rank.txt")
    print(f"chip_genes: {len(chip_gene_order)}")  # 6639

    plants_spt_targets_order = load_gene_set(
        "plants-2165966-target-gene-spt-listing.txt"
    )
    print(f"plants_spt_targets: {len(plants_spt_targets_order)}")  # 3692

    common_genes = set(chip_gene_order) & set(plants_spt_targets_order)

    print(f"common L: {len(common_genes)}")
    print(f"common genes: {common_genes}")
    assert len(common_genes) == 657

    details = thalemine_description_data()

    output_file = "chipseq_rnaseq_intersection-spt-targets-ath.tab"

    header = [
        "Gene_symbol",
        "TairAliases",
        "ShortDescription",
        "ComputationalDescription",
    ]

    n = 0
    with open(output_file, "w") as outf:
        outf.write("\t".join(["Gene_name"] + header) + "\n")
        for gene in chip_gene_order:  # we want to keep the order of chipseq order
            if gene not in common_genes:
                continue

            if gene not in details:
                print(f"Error: {gene} not found in Thalemine description file")
                sys.exit(1)
            outf.write("\t".join([gene] + [details[gene][h] for h in header]) + "\n")
            n+=1

    assert n == len(common_genes)

    print("Done")
