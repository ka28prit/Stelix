from astropy.io import fits
import pandas as pd

def fits_to_csv(input_file, output_file=None):
  """
  Converts .fits file to .csv file
  """

  with fits.open(input_file) as hdul:
    data = hdul[1].data

  df = pd.DataFrame(data)

  if not output_file:
    output_file = input_file.replace(".fits",".csv")

  df.to_csv(output_file, index=False)
  print(f"Converted {input_file} -> {output_file}")
