import os

HEADER_FILENAME = 'content_heading.xml'


def add_content_headers(file, template_directory):
    header_file = open(os.path.join(
        template_directory,
        HEADER_FILENAME
    ), 'r')

    for line in header_file:
        file.write(line)
