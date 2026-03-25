import argparse
from .pipeline import reduce_fits

def main():
  parser = argparse.ArgumentParser(description="Stelix Reduction Pipeline")
  parser.add_argument("input", help="Input fits file")
  parser.add_argument("--to-csv", action="store_true", help="Also export csv")
  parser.add_argument("--output", help="Optional output filename or path")

  args = parser.parse_args()

  reduce_fits(args.input, output_file=args.output, to_csv=args.to_csv)

if __name__ == "__main__":
  main()
