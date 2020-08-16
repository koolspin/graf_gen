from svg.svg_environment import SvgEnvironment


def startup():
    """
    The main function
    :return: None
    """
    print("Hello world!")
    svgenv = SvgEnvironment('test.svg')
    svgenv.text_tag1('Nile 2020!')
    svgenv.save()


if __name__ == '__main__':
    startup()
