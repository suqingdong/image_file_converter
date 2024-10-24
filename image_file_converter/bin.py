import click

from image_file_converter import version_info
from image_file_converter.core import ImageFileConverter


CONTEXT_SETTINGS = dict(help_option_names=['-?', '-h', '--help'])

@click.command(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
)
@click.version_option(version=version_info['version'], prog_name=version_info['prog'])
@click.argument('command', type=click.Choice(['to_image', 'to_pdf', 'to_data_url']))
@click.argument('input_file')
@click.option('-o', '--output-file', help='the output file name')
@click.option('--dpi', help='the dpi of pdf to image converter', type=int, default=300, show_default=True)
@click.option('--max-page', help='the max page of pdf to image converter', type=int)
def main(command, input_file, output_file, dpi, max_page):
    converter = ImageFileConverter(input_file, dpi=dpi, max_page=max_page)
    if command != 'to_data_url' and output_file is None:
        suffix = 'pdf' if command == 'to_pdf' else 'png'
        output_file = f'{input_file}.{suffix}'
    
    if command == 'to_image':
        converter.to_image(output_file)
    elif command == 'to_pdf':
        converter.to_pdf(output_file)
    elif command == 'to_data_url':
        converter.to_data_url(output_file)

    if output_file is not None:
        click.secho(f'save file: {output_file}', err=True, fg='green')


if __name__ == '__main__':
    main()
