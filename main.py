import argparse
from config import get_config


def parse_option():
    parser = argparse.ArgumentParser('Swin Transformer script', add_help=False)
    #
    #
    #
    args, unparsed = parser.parse_known_args()
    config = get_config(args)
    return args, config


def main(cfg):
    loader = build_loader(cfg)


if __name__ == "__main__":
    _, cfg= parse_option()
    main(cfg)
