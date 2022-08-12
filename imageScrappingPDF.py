PDF_PATH = '/Users/akifislam/Desktop/QuestionReader/AS  Biology (9700)/2011'

import os
import io
from PIL import Image

import fitz  # pip install --upgrade pip; pip install --upgrade pymupdf
from tqdm import tqdm  # pip install tqdm

workdir = PDF_PATH

for each_path in os.listdir(workdir):
    print(each_path)
    if ".pdf" in each_path:
        doc = fitz.Document((os.path.join(workdir, each_path)))

        for i in tqdm(range(len(doc)), desc="pages"):
            for img in tqdm(doc.get_page_images(i), desc="page_images"):
                xref = img[0]
                base_image = doc.extract_image(xref) #base image
                pix = fitz.Pixmap(doc, xref)
                try:
                    # pix.save(os.path.join(workdir, "%s_p%s.%s" % (each_path[:-4], i,base_image["ext"])))
                    image_bytes = base_image["image"]
                    # get the image extension
                    image_ext = base_image["ext"]
                    # load it to PIL
                    image = Image.open(io.BytesIO(image_bytes))
                    # save it to local disk
                    image.save(open(f"image{page_index + 1}_{image_index}.{image_ext}", "wb"))

                except:
                    print('Cannot save')

print("Done!")