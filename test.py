import argparse

parser = argparse.ArgumentParser()


parser.add_argument("-o", "--option", type=int, choices=[1,2])
args  = parser.parse_args()

print(args.option)
