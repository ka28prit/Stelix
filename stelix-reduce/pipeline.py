from astropy.io import fits
import numpy as np
import os

def normalize_image(image_data):
  """
  Normalizes any numeric image data to range 0-1.
  Works for int or float astypes.
  """

  image_data = image_data.astype(float)
  minval = np.min(image_data)
  maxval = np.max(image_data)

  if maxval == minval:
    return np.zeros_like(image_data)

  return ((image_data - minval) / (maxval - minval))

def reduce_fits (input_file, output_file=None, to_csv=False):
  """
  Reduces a fits file: normalizes image or converts to a table

  Parameters:
  - input_file: str, path to .fits file
  - output_file: str, optional output path
  - to_csv: bool, whether to also save as .csv file
  """

  if output_file is None:
    folder = os.path.dirname(input_file)
    base = os.path.basename(input_file).replace(".fits","_reduced.fits")
    output_file = os.path.join(folder, base)

  with fits.open(input_file) as hdul:
    processed = False

    for i, hdu in enumerate(hdul):
      if hdu.data is not None:
        data = hdu.data
        if np.issubdtype(data.dtype, np.number):
          data = normalize_image(data)
          header = hdu.header
          fits.writeto(output_file, data.astype(np.float32), header, overwrite=True)
          print(f"Saved normalized .fits: {output_file}")

          if to_csv:
            csv_file = output_file.replace(".fits",".csv")
            np.savetxt(csv_file, data, delimeter=",")
            print(f"Saved .csv:{csv_file}")

          processed = True
          break
          
        elif hasattr(data, "columns"):
          df = pd.DataFrame(data)
          csv_file = output_file.replace(".fits",".csv")
          df.to_csv(csv_file, index=False)
          print(f"Saved .csv from Table HDU: {csv_file}")
          
          processed = True
          break
          
    if not processed:
      print(f"No usable data found in {input_file")
  
