from enum import Enum


class ParagraphType(Enum):
    PART = 'Part'
    PROLOGUE = 'Prologue'
    CHAPTER = 'Chapter'
    CHAPTER_PART = 'Chapter Part'
    SCENE = 'Scene'
    PART_ENDER = 'Part Ender'
    EPILOGUE = 'Epilogue'
    NORMAL = 'Normal'
