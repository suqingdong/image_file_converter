import io
import base64
import mimetypes

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from image_file_converter import utils


class ImageFileConverter(object):
    def __init__(self, input_file, **kwargs):
        self.input_file = input_file
        self.kwargs = kwargs
        self._image = None

    @property
    def image(self):
        if self._image is None:
            mime_type, _ = mimetypes.guess_type(self.input_file)
            if mime_type == 'application/pdf':
                self._image = utils.load_image_from_pdf(self.input_file, **self.kwargs)
            elif mime_type.startswith('image/'):
                self._image = utils.load_image(self.input_file)
            else:
                raise ValueError('Unsupported file type')
        return self._image
    
    def to_bytes(self, fmt='png'):
        buffered = io.BytesIO()
        self.image.save(buffered, format=fmt)
        return buffered.getvalue()
    
    def to_b64_string(self, fmt='png'):
        image_bytes = self.to_bytes(fmt)
        return base64.b64encode(image_bytes).decode()

    def to_image(self, output_file):
        self.image.save(output_file)

    def to_data_url(self, fmt='png', output_file=None):
        b64_string = self.to_b64_string(fmt)
        data_url = f'data:image/{fmt};base64,{b64_string}'
        if output_file:
            with open(output_file, 'w') as out:
                out.write(data_url)
        return data_url

    def to_pdf(self, output_file):
        c = canvas.Canvas(output_file, pagesize=self.image.size)
        c.drawImage(self.image.filename, 0, 0)
        c.save()


if __name__ == '__main__':
    converter = ImageFileConverter('tests/venn.png')
    converter.to_pdf('tests/venn.pdf')
    converter.to_image('tests/venn_converted.jpg', )

    converter = ImageFileConverter('tests/滴滴电子发票.pdf', dpi='300')
    converter.to_image('tests/滴滴电子发票.jpg')
    converter.to_image('tests/滴滴电子发票.png')
    converter.to_data_url('png', output_file='tests/滴滴电子发票.data_url.txt')
