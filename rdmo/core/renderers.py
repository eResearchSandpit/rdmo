from __future__ import unicode_literals

from django.utils.xmlutils import SimplerXMLGenerator
from django.utils.six.moves import StringIO
from django.utils.encoding import smart_text
from rest_framework.renderers import BaseRenderer


class BaseXMLRenderer(BaseRenderer):

    media_type = 'application/xml'
    format = 'xml'

    def render(self, data):

        if data is None:
            return ''

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, "utf-8")
        xml.startDocument()
        self.render_document(xml, data)
        xml.endDocument()
        return stream.getvalue()

    def render_text_element(self, xml, tag, attrs, text):
        # remove None values from attrs
        attrs = dict((key, value) for key, value in attrs.items() if value)

        xml.startElement(tag, attrs)
        if text is not None:
            xml.characters(smart_text(text))
        xml.endElement(tag)

    def render_document(self, xml, data):
        pass
