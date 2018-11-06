from paragraph_type import ParagraphType
from xmlobject import XmlObject

SCENE_BREAK_CHARACTER = "*"
ONE_THIRD_PAGE = 12
STANDARD_BUFFER = 2

# I imagine these might someday be better
# placed in their own configuration file.

CENTERED = [
    ParagraphType.PART,
    ParagraphType.CHAPTER,
    ParagraphType.CHAPTER_PART,
    ParagraphType.SCENE,
    ParagraphType.PROLOGUE,
    ParagraphType.EPILOGUE,
    ParagraphType.PART_ENDER
]

UPPER = [
    ParagraphType.PART,
    ParagraphType.CHAPTER
]

PAGE_BREAK_BEFORE = [
    ParagraphType.PART,
    ParagraphType.CHAPTER,
    ParagraphType.PROLOGUE,
    ParagraphType.EPILOGUE,
    ParagraphType.PART_ENDER
]

PAGE_BREAK_AFTER = [
    ParagraphType.PART
]

BUFFER_SPACES = {
    ParagraphType.CHAPTER_PART: 2,
    ParagraphType.SCENE: 1
}

HIDE_TITLE = [
    ParagraphType.PART_ENDER
]

INDENT = [
    ParagraphType.NORMAL
]


class Paragraph:
    def __init__(self, paragraph_type, line):
        self.text = line
        self.paragraph_type = paragraph_type

        if paragraph_type == ParagraphType.PROLOGUE:
            self.text = 'Prologue'
        elif paragraph_type == ParagraphType.EPILOGUE:
            self.text = 'Epilogue'

    def getXml(self):
        xmlObject = XmlObject(self.text)
        if self.paragraph_type in CENTERED:
            xmlObject.center()

        if self.paragraph_type in UPPER:
            xmlObject.upper()

        if self.paragraph_type in PAGE_BREAK_BEFORE:
            xmlObject.pre_page_break()
            xmlObject.set_pre_buffer(ONE_THIRD_PAGE)
            xmlObject.set_post_buffer(STANDARD_BUFFER)

        if self.paragraph_type in PAGE_BREAK_AFTER:
            xmlObject.post_page_break()

        if self.paragraph_type in BUFFER_SPACES:
            xmlObject.set_pre_buffer(BUFFER_SPACES[self.paragraph_type])
            xmlObject.set_post_buffer(BUFFER_SPACES[self.paragraph_type])

        if self.paragraph_type in HIDE_TITLE:
            xmlObject.removeText()

        if self.paragraph_type in INDENT:
            xmlObject.indent()

        output = xmlObject.getXml()
        return output
