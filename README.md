# Toolkit for converting image files

## Installation

```bash
python -m pip install image_file_converter
```

## Usage in Python

```python
from image_file_converter.core import ImageFileConverter

# convert pdf to image or data_url
input_file = 'tests/test.pdf
converter = ImageFileConverter(input_file, dpi=300, max_page=5)
converter.to_image('output.png')
converter.to_image('output.jpg')
data_url = converter.to_data_url()
print(data_url)

# convert image to pdf or data_url
input_file = 'tests/test.png'
converter = ImageFileConverter(input_file)
converter.to_pdf('output.pdf')
data_url = converter.to_data_url()
print(data_url)
```

## Usage in CMD

```bash
image_file_converter --help
image_file_converter --version

# convert pdf to image
image_file_converter to_image tests/test.pdf -o output.png
image_file_converter to_image tests/test.pdf -o output.jpg
image_file_converter to_image tests/test.pdf -o output.png --dpi 300 --max-page 5

# convert image to pdf
image_file_converter to_pdf tests/test.png -o output.pdf
image_file_converter to_pdf tests/test.jpg -o output.pdf

# convert image or pdf to data_url
image_file_converter to_data_url tests/test.png
image_file_converter to_data_url tests/test.pdf
image_file_converter to_data_url tests/test.pdf --dpi 300 --max-page 5
```
