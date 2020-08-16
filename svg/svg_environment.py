import svgwrite


class SvgEnvironment:
    """
    Creates the SVG environment for further drawing
    """

    def __init__(self, svg_path: str) -> None:
        super().__init__()
        self._svg_path = svg_path
        self._svg_dwg = svgwrite.Drawing(self._svg_path, profile='full')
        self._svg_dwg.add(self._svg_dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='#a0a0a0'))

    def text_tag1(self, tag_text: str) -> None:
        """
        Use the text facility for the tag, with a simple drop shadow
        :param tag:
        :return: None
        """
        gg = self._svg_dwg.g(style='font-size: 4.0em; font-weight: bold; font-family: Helvetica, sans-serif;')
        gg.add(self._svg_dwg.text(tag_text, insert=(0, '1.0em'), fill='#7f7f7f'))
        gg.add(self._svg_dwg.text(tag_text, insert=('0.07em', '0.93em'), fill='#c04040'))
        self._svg_dwg.add(gg)

    def save(self) -> None:
        self._svg_dwg.save()