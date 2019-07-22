#!/usr/bin/env python3.7
"""
Parse through each PDZ file, one byte at a time, and show when differences occur
"""

from difflib import SequenceMatcher
from pathlib import Path
from pprint import pprint
from typing import Dict, Iterable, List, Union

TEST = ["GLASSMAJORS", "GeoExploration", ""][2]


def _get_file_names(directory: Path) -> Iterable:
    if TEST:
        files = directory.glob(f"files/*{TEST}*.pdz")
    else:
        files = directory.glob("files/*.pdz")
    return files


def _get_max_filesize(files: Union[Iterable, Path]) -> int:
    size: int
    if isinstance(files, Path):
        size = files.stat().st_size
    else:
        sizes = [f.stat().st_size for f in files]
        size = max(sizes)
    return size


def _get_file_contents(
    files: Iterable[Path], lo: int = 0, hi: int = -1
) -> Dict[Path, bytes]:
    file_dict: Dict[Path, bytes] = {}
    file_list: List[Path] = list(files)
    if hi == -1:
        hi = _get_max_filesize(file_list)
    for file in file_list:
        with open(file, "rb") as f:
            file_dict[file] = f.read()[lo:hi]
    return file_dict


def main():
    directory: Path = Path(".")
    files: Iterable = _get_file_names(directory)
    file_dict: Dict[Path, bytes] = _get_file_contents(files, hi=500)
    file_list: List[Path] = [p for p in file_dict]
    print(f"Comparing: {file_list}")
    for ind, file1 in enumerate(file_list):
        for file2 in file_list[ind + 1 :]:
            if file1 != file2:
                print(f"{file1.as_posix()} -- {file2.as_posix()}")
                s = SequenceMatcher(a=file_dict[file1], b=file_dict[file2])
                matching_blocks = s.get_matching_blocks()
                pprint(matching_blocks)
                for a, b, length in matching_blocks:
                    print(f"a[{a}] and b[{b}] for {length}")
                    print(f"{file1.as_posix()}: {file_dict[file1][a:a+length]}")
                    print(f"{file2.as_posix()}: {file_dict[file2][b:b+length]}")


if __name__ == "__main__":
    main()
