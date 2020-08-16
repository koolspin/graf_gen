import svgwrite


class SvgEnvironment:
    """
    Creates the SVG environment for further drawing
    """

    def __init__(self, svg_path: str) -> None:
        super().__init__()
        self._svg_path = svg_path
        self._svg_dwg = svgwrite.Drawing(self._svg_path, size=("512px", "512px"), profile='full')
        self._svg_dwg.add(self._svg_dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='rgb(200, 200, 200)'))

    def text_tag1(self, tag_text: str) -> None:
        """
        Use the text facility for the tag, with a simple drop shadow
        :param tag:
        :return: None
        """
        self._svg_dwg.add(self._svg_dwg.text(tag_text, insert=(0, '1.0em'), fill='#7f7f7f', style='font-size: 4.0em; font-weight: bold; font-family: Helvetica, sans-serif;'))
        self._svg_dwg.add(self._svg_dwg.text(tag_text, insert=('0.1em', '0.9em'), fill='red', style='font-size: 4.0em; font-weight: bold; font-family: Helvetica, sans-serif;'))

    def save(self) -> None:
        self._svg_dwg.save()