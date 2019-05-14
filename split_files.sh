#! /bin/bash

mkdir mol2_files
cd ./downloads/

for i in ./*.mol2; do
    csplit $i '/@<TRIPOS>MOLECULE/' '{*}'
    for x in xx*; do
        zinc=$(cat $x | head -2 | tail -1)
        mv -- "$x" ../mol2_files/"${zinc}.mol2"
    done
done

#rm -r downloads
