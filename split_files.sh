#! /bin/bash

mkdir mol2_files
csplit ./downloads/ZINC_results.mol2 '/@<TRIPOS>MOLECULE/' '{*}'

for f in xx*; do
    zinc=$(cat $f | head -2 | tail -1)
    mv -- "$f" mol2_files/"${zinc}.mol2"
done

#rm -r downloads