from svg.svg_environment import SvgEnvironment


def startup():
    """
    The main function
    :return: None
    """
    print("Hello world!")
    svgenv = SvgEnvironment('test.svg')
    svgenv.test1()
    svgenv.save()


if __name__ == '__main__':
    startup()
