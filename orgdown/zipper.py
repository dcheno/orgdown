import zipfile
import os

ODT_PARTS_DIRECTORY = 'odt_parts'


def createODT(odtname, template_directory):
    parts_path = os.path.join(template_directory, ODT_PARTS_DIRECTORY)
    with zipfile.ZipFile(odtname, 'w') as archive:
        archive.write(os.path.join(parts_path, 'META-INF'), 'META-INF')
        archive.write(os.path.join(
            parts_path + '/META-INF',
            'manifest.xml'
        ),
            '/META-INF/manifest.xml')
        archive.write(os.path.join(parts_path, 'meta.xml'), 'meta.xml')
        archive.write('content.xml')
        archive.write(os.path.join(parts_path, 'mimetype'), 'mimetype')
        archive.write(os.path.join(parts_path,
                                   'styles.xml'), 'styles.xml')
