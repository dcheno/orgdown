import sys
import os
import headerhandler
import contenthandler
import zipper

TARGET_EXTENSION = ".odt"
TEMPLATE_DIRECTORY = 'Templates'
CONTENT_XML = 'content.xml'

source_filename = sys.argv[1]
source_file = open(source_filename, 'r')

source_filename_no_ext = os.path.splitext(source_filename)[0]
target_filename = source_filename_no_ext + TARGET_EXTENSION

with open(CONTENT_XML, '+w') as content_file:
    headerhandler.add_content_headers(content_file, TEMPLATE_DIRECTORY)
    contenthandler.transform_content(source_file, content_file)

zipper.createODT(target_filename, TEMPLATE_DIRECTORY)
os.remove(CONTENT_XML)
