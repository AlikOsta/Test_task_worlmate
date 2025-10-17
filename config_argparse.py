import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--files", type=str, nargs='+')
parser.add_argument("--report", type=str)

args = parser.parse_args()

# print(args.files) # ["products1.csv", "products2.csv"]
