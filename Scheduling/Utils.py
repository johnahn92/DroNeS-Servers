import configparser
import os


class Args:
    def __init__(self):
        self.items = []
        self.origin = None
        self.radius = None
        self.generator_params = None


def getArgs():
    args = Args()
    config = configparser.ConfigParser()
    file = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(file)

    for (item, params) in config['Jobs'].items():
        entry = {'item': item,
                 'reward': eval(params)[0],
                 'penalty': eval(params)[1],
                 'valid_for': eval(params)[2]}
        args.items.append(entry)

    args.origin = eval(config['Settings']['dispatch_origin'])
    args.radius = eval(config['Settings']['dispatch_radius'])
    args.generator_params = eval(config['Job Generator']['params'])

    return args
