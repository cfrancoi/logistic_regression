import csv
import argparse

def describe(path: str):
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

    return

def __start__():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data-set", required=True, type=str, help="csv path used to be describe", action="store")
    args = parser.parse_args()

    describe(args.data_set)

__start__()