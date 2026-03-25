import argparse
from .pipeline import fits_to_csv

def main():
  parser = argparse.ArgumentParser(description="Stelix Reduction Pipeline")
  parser.add_argument("input", help="Input fits file")
  parser.add_argument("--to", choices=["csv"], required=True, help="Output format")

  args = parser.parse_args()

  if args.to == "csv":
    fits_to_csv(args.input)

if __name__ == "__main__":
  main()
