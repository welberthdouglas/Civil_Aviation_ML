#!bin/bash
zipfiles=ANAC_DATA_ZIP/basica*.zip
set -- $zipfiles
mkdir ANAC_DATA
unzip $zipfiles -d ANAC_DATA
datasets=ANAC_DATA/basica*.txt
set -- $datasets
head -n 1 $1 > tmp1.txt
tail -n +2 $datasets  | grep -a -v "==>"  > tmp2.txt
cat tmp1.txt  tmp2.txt > temp3.txt
columns=$(<keep_columns.txt)
csvcut -d ';' -c $columns -e 'ISO-8859-1' temp3.txt >  temp.csv
csvgrep -c ds_servico_tipo_linha  -m PASSAGEIRO temp.csv | csvgrep -c ds_grupo_di -i -m IMPRODUTIVO | csvgrep -c ds_tipo_empresa -m 'TRANSPORTE AÉREO REGULAR' > data.csv
rm temp3.txt temp.csv tmp1.txt tmp2.txt keep_columns.txt

