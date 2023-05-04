### How to obtain `KIDS2023_QA.input.txt`

- Download the first TAB in https://docs.google.com/spreadsheets/d/11veOrBcv5WsfdZE3G15HRNJ_TVINfOWwd2ZbafKA3U4/edit#gid=0 as TSV
- Run `sed '2d' KIDS2023_QA_for_training\ -\ general-training_biochemistry.tsv | cut -f 2,3 | tr '\t' ' ' > KIDS2023_QA.input.txt`
