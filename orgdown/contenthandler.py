from paragraph_type import ParagraphType
from paragraph import Paragraph

PARAGRAPH_TYPE_INDICATORS = {
    "*": ParagraphType.PART,
    "**": ParagraphType.CHAPTER,
    "***": ParagraphType.CHAPTER_PART,
    "****": ParagraphType.SCENE
}

SECONDARY_TYPE_INDICATORS = {
    "PROLOGUE": ParagraphType.PROLOGUE,
    "PART ENDER": ParagraphType.PART_ENDER,
    "EPILOGUE": ParagraphType.EPILOGUE
}

SCENE_BREAK_CHARACTER = "*"


def transform_content(source_file, content_file):
    """
    Takes unprocessed text from a source file, parses it for special
    markdown and then writes it to the content file.
    """

    for line in source_file:
        new_line = _transform_line(line)
        print(new_line)
        content_file.write(new_line)


def _transform_line(line):
    """
    Takes a line of text and returns the processed line.
    """
    paragraph_type = _check_paragraph_type(line)

    line = line.rstrip('\n')
    if paragraph_type != ParagraphType.NORMAL:
        line = line.split(' ', 1)[1]
    print(paragraph_type)
    print(line)
    paragraph = Paragraph(paragraph_type, line)
    new_line = paragraph.getXml()
    return new_line


def _check_paragraph_type(line):
    indicator = line.split(' ')[0]

    paragraph_type = PARAGRAPH_TYPE_INDICATORS.get(
        indicator,
        ParagraphType.NORMAL
    )

    # Special Cases
    if paragraph_type == ParagraphType.CHAPTER:
        secondary_indicator = line.split(' ')[1]
        paragraph_type = SECONDARY_TYPE_INDICATORS.get(
            secondary_indicator,
            ParagraphType.CHAPTER)

    return paragraph_type
