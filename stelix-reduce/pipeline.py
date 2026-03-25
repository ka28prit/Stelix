from astropy.io import fits
import numpy as np
import os

def normalize_image(image_data):
  """
  Normalizes image data to range 0-1
  """

  return (image_data - np.min(image_data))

def reduce_fits (input_file, output_file=None, to_csv=False):
  """
  Reduces a fits file: normalizes image or converts to a table
  """

  with fits.open(input_file) as hdul:
    if len(hdul) == 1 or hdul[0].data is not None:

      data = hdul[0].data.astype(float)
      data = normalize_image(data)
      header = hdul[0].header
      if not output_file:
        output_file = input_file.replace(".fits",".reduced_fits")
      fits.writeto(output_file, data, header, overwrite=True)
      print(f"Saved normalized fits: {output_file}")
      
      if to_csv:
        csv_file = output_file.replace(".fits",".csv")
        np.savetxt(csv_file, data, delimeter=",")
        print(f"Saved csv: {csv_file}")

    elif len(hdul) > 1 and hdul[1].data is not None:
      data = hdul[1].data
      if not output_file:
        output_file = input_file.replace(".fits",".csv")
      df = pd.DataFrame(data)
      df.to_csv(output_file, index=False)
      print(f"Saved csv: {output_file}")
