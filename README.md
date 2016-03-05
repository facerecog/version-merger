# version-merger
Version Merger is a Python script which can be used to save snapshots of a CSV as it changes through time. Property of Facerecog Asia Pte. Ltd. and 26 Factorial

Go to the examples/ folder and run  randomizing_csv.py to produce a dump file which changes every second:

`$ cd example`

`$ python randomizing_csv.py` 

Run  version-merger.py in the following manner:
 
`$ python version-merger.py -i <input_file> -o <output_file> -t <seconds> -r <data_resolution_in_seconds>`

Example below:

`$ python version-merger.py -i dump*.csv -o mastercopy.csv -t 60 -r 1` 
