from paragraph_type import ParagraphType
from xmlobject import XmlObject

SCENE_BREAK_CHARACTER = "#"
ONE_THIRD_PAGE = 12
STANDARD_BUFFER = 2

# I imagine these might someday be better
# placed in their own configuration file.

LEVELS = {
    ParagraphType.PART: 0,
    ParagraphType.PROLOGUE: 1,
    ParagraphType.CHAPTER: 1,
    ParagraphType.PART_ENDER: 1,
    ParagraphType.EPILOGUE: 1,
    ParagraphType.CHAPTER_PART: 2,
    ParagraphType.SCENE: 3,
    ParagraphType.NORMAL: 4
}


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
    def __init__(self, paragraph_type, line, previous_paragraph_type):
        self._display_xml = True
        if paragraph_type != ParagraphType.SCENE:
            self._text = line
        else:
            self._text = SCENE_BREAK_CHARACTER
            if previous_paragraph_type != ParagraphType.NORMAL:
                self._display_xml = False

        self._paragraph_type = paragraph_type
        self._previous_paragraph_type = previous_paragraph_type

        if paragraph_type == ParagraphType.PROLOGUE:
            self._text = 'Prologue'
        elif paragraph_type == ParagraphType.EPILOGUE:
            self._text = 'Epilogue'

    def get_type(self):
        return self._paragraph_type

    def getXml(self):

        # Special Case where the line does not represent any
        # displayable text.
        if self._display_xml == False:
            return ''

        xmlObject = XmlObject(self._text)
        if self._paragraph_type in CENTERED:
            xmlObject.center()

        if self._paragraph_type in UPPER:
            xmlObject.upper()

        if self._paragraph_type in PAGE_BREAK_BEFORE:
            if self._previous_paragraph_type not in PAGE_BREAK_AFTER:
                xmlObject.pre_page_break()

            xmlObject.set_pre_buffer(ONE_THIRD_PAGE)
            xmlObject.set_post_buffer(STANDARD_BUFFER)

        if self._paragraph_type in PAGE_BREAK_AFTER:
            xmlObject.post_page_break()

        if self._paragraph_type in BUFFER_SPACES:
            previous_buffer = BUFFER_SPACES.get(
                self._previous_paragraph_type, 0)
            def_pre_buffer = BUFFER_SPACES[self._paragraph_type]
            print(previous_buffer)
            print(def_pre_buffer)
            pre_buffer = max(def_pre_buffer - previous_buffer, 0)
            print(pre_buffer)
            xmlObject.set_pre_buffer(pre_buffer)

            xmlObject.set_post_buffer(def_pre_buffer)

        if self._paragraph_type in HIDE_TITLE:
            xmlObject.remove_text()

        if self._paragraph_type in INDENT:
            xmlObject.indent()

        output = xmlObject.getXml()
        return output
