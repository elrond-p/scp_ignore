#!/usr/local/bin/python3

import os
from argparse import ArgumentParser
from pathlib import Path


def _scpignore_parser(filepath):
    # print(filepath)
    root_dir = Path(filepath).parent.resolve()
    scpignore = root_dir / '.scpignore'
    ignored = []

    if not os.path.isfile(str(scpignore)):
        return ignored


    with open(scpignore, 'r') as file:
        for line in file.read().splitlines():
            if line.startswith('#'):
                continue

            ignored.append(Path(line))

    return ignored


def _move_file(filepath, tmp):

    tmp_filepath = Path(f'/tmp/scpi/{filepath.stem}')
    tmp_filepath.parent.mkdir(exist_ok=True)
    
    if tmp:
        filepath.rename(tmp_filepath)
    else:
        tmp_filepath.rename(filepath)


def _handle_recursive(ignored):
    pass


def main():
    parser = ArgumentParser()
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        default=False,
    )
    parser.add_argument(
        'filepath',
        # required=True,
    )
    parser.add_argument(
        'destination',
        # required=True,
    )
    args = parser.parse_args()

    ignored = _scpignore_parser(args.filepath)

    if args.recursive:
        _handle_recursive(ignored)
    else:
        _move_file(ignored[0], tmp=True)

if __name__ == '__main__':
    main()
