import svgwrite


class SvgEnvironment:
    """
    Creates the SVG environment for further drawing
    """

    def __init__(self, svg_path: str) -> None:
        super().__init__()
        self._svg_path = svg_path
        self._svg_dwg = svgwrite.Drawing(self._svg_path, profile='tiny')

    def test1(self) -> None:
        self._svg_dwg.add(self._svg_dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
        self._svg_dwg.add(self._svg_dwg.text('Test', insert=(0, 0.2), fill='red'))
        pass

    def save(self) -> None:
        self._svg_dwg.save()