import io

import fitz
from PIL import Image

Image.MAX_IMAGE_PIXELS = None


def load_image_from_pdf(file_path, dpi=150, max_page=None, **kwargs):
    """Convert PDF file to image with `PyMuPDF`

    :param file_path: the PDF file path
    :param dpi: the DPI of the image, default is 150
    :param max_page: the maximum number of pages to read, default is None
    :return: the combined image
    """
    # get image list from each pdf page
    images = []
    with fitz.open(file_path) as pdf:
        for n, page in enumerate(pdf, 1):
            pix = page.get_pixmap(dpi=dpi)
            img = Image.open(io.BytesIO(pix.tobytes('png')))
            images.append(img)
            if max_page and n >= max_page:
                break

    # calculate the maximum width and total height
    widths, heights = zip(*(i.size for i in images))
    max_width = max(widths)
    total_height = sum(heights)

    # combine to one image
    combined_image = Image.new('RGB', (max_width, total_height))
    y_offset = 0
    for img in images:
        combined_image.paste(img, (0, y_offset))
        y_offset += img.height

    return combined_image


def load_image(file_path):
    """Load image from file path

    :param file_path: the image file path
    :return: the image
    """
    return Image.open(file_path)

