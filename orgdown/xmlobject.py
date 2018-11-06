

class XmlObject:

    def __init__(self, text):
        self._text = text
        self._hasText = True
        self._centered = False
        self._upper = False
        self._pre_page_break = False
        self._post_page_break = False
        self._pre_buffer = 0
        self._post_buffer = 0
        self._indented = False

    def center(self):
        self._centered = True

    def upper(self):
        self._upper = True

    def pre_page_break(self):
        self._pre_page_break = True

    def post_page_break(self):
        self._post_page_break = True

    def set_pre_buffer(self, buffer):
        self._pre_buffer = buffer

    def set_post_buffer(self, buffer):
        self._post_buffer = buffer

    def remove_text(self):
        self._text = ''
        self._hasText = False

    def indent(self):
        self._indented = True

    def getXml(self):
        """
        Returns the XML that that represents the paragraph, .odt style.
        """

        xml = ''

        if self._upper:
            inner_text = self._text.upper()
        else:
            inner_text = self._text

        attributes = []
        if self._centered:
            attributes.append('centered')

        if self._indented:
            attributes.append('indented')

        style_code = '_'.join(attributes)

        if self._pre_page_break:
            xml += self._create_page_break()

        for i in range(self._pre_buffer):
            xml += self._create_blank_line()

        if self._hasText:
            xml += self._create_xml_text_element('p', style_code, inner_text)
        if self._post_page_break:
            xml += self._create_page_break()
        else:
            for i in range(self._post_buffer):
                xml += self._create_blank_line()

        return xml

    # Private Functions:

    def _create_page_break(self):
        """
        Creates and returns a page break xml element.
        """
        PAGE_BREAK_STYLE_CODE = 'page_break'
        page_break_xml = self._create_xml_text_element(
            'p',
            PAGE_BREAK_STYLE_CODE,
            ''
        )

        return page_break_xml

    def _create_blank_line(self):
        """
        Creates and returns a blank line xml element
        """
        BLANK_LINE_STYLE_CODE = 'centered'
        blank_line_xml = self._create_xml_text_element(
            'p',
            BLANK_LINE_STYLE_CODE,
            ''
        )

        return blank_line_xml

    def _create_xml_text_element(self, type_code, style_code, inner_text):
        """
        Creates and returns an xml element of the given type, with
        the given style code and inner text. If inner text is
        empty, returns a self closing tag.
        """
        if len(inner_text) > 0:
            xml_tag = '<text:{0} text:style-name="{1}">{2}</text:{0}>'
            xml_tag = xml_tag.format(type_code, style_code, inner_text)
        else:
            xml_tag = '<text:{0} text:style-name="{1}"/>'
            xml_tag = xml_tag.format(type_code, style_code)

        xml_tag += '\n'

        return xml_tag
