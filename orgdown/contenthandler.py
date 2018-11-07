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
    "PART_ENDER": ParagraphType.PART_ENDER,
    "EPILOGUE": ParagraphType.EPILOGUE
}


def transform_content(source_file, content_file):
    """
    Takes unprocessed text from a source file, parses it for special
    markdown and then writes it to the content file.
    """
    previous_paragraph_type = ParagraphType.NONE
    for line in source_file:
        paragraph = _get_paragraph(line, previous_paragraph_type)
        new_line = paragraph.getXml()
        content_file.write(new_line)
        previous_paragraph_type = paragraph.get_type()


def _get_paragraph(line, previous_paragraph_type):
    """
    Takes a line of text and returns the processed line. Requires
    the prevoius paragraph type,  which might be an interface break.
    """
    paragraph_type = _check_paragraph_type(line)
    line = line.strip()
    line = line.rstrip('\n')
    if paragraph_type != ParagraphType.NORMAL:
        line = line.split(' ', 1)[1]
    paragraph = Paragraph(paragraph_type, line, previous_paragraph_type)

    print(line)
    print(paragraph_type)
    print(previous_paragraph_type)
    return paragraph


def _check_paragraph_type(line):
    indicator = line.split(' ', 1)[0]

    paragraph_type = PARAGRAPH_TYPE_INDICATORS.get(
        indicator,
        ParagraphType.NORMAL
    )

    # Special Cases
    if paragraph_type == ParagraphType.CHAPTER:
        secondary_indicator = line.split(' ', 2)[1]
        paragraph_type = SECONDARY_TYPE_INDICATORS.get(
            secondary_indicator,
            ParagraphType.CHAPTER)

    return paragraph_type
