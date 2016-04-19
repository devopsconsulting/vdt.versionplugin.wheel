import argparse


def parse_version_extra_args(version_args):
    p = argparse.ArgumentParser(
        description="Package python packages with vdt.versionplugin.wheel")
    p.add_argument(
        '--build-dependencies', action='store_true', default=False,
        help="Using this flag makes also builds wheels of dependencies.")
    args, extra_args = p.parse_known_args(version_args)

    return args, extra_args
