#!/usr/bin/env python3

"""
All of the relevant binary structures and strings for PDZ files
"""

from pprint import pprint
from struct import pack
from typing import List, Union


# Formatting strings (mostly for structs)
def string_fmt(string: Union[str, bytes]) -> str:
    """
    Create struct format string based on text input

    :param string: str
    :return: str
    """
    return "<" + "Bx" * len(string)


def compound_fmt(compound: bytes) -> str:
    """
    Create struct format string based on compound byte-string

    :param compound: bytes
    :return: str
    """
    return "<" + "Bx" * (len(compound) // 2)


FMT_END: str = "< 12x"
FMT_BEGIN: str = "< H I I"
FMT_VALUES: str = "< 3f"
FMT_FOOTER: str = "< B x B 27x I 6x B x B 3x B x B 3x"

# Actual constants - Valid options
_Applications: List[bytes] = [
    b"GLASSMAJOR",
    b"GeoExploration",
    b"GeoMining"
]
_Methods: List[bytes] = [
    b"Oxide3phase",
    b"OxideConcentrates",
    b"GLASSMAJORS"
]

# Actual constants - struct bytes and lists of bytes
PACKET_END: bytes = pack(FMT_END)
PACKET_BEGIN: List[bytes] = [
    pack(FMT_BEGIN, 6, int.from_bytes(A, 'little'), int.from_bytes(B, 'little'))
    for A, B in [
        (b"\x27", b"\x03"),
        (b"\x25", b"\x02"),
        (b"\x2b", b"\x05"),
        (b"\x29", b"\x04"),
        (b"\x23", b"\x01")
    ]
]
INTRA_PACKET_BREAK: bytes = b"\x00\x00\x02"
FILE_HEADER: bytes = b"\x19\x00\x0E\x00\x00\x00p\x00d\x00z\x002\x005"
FILE_FOOTERS: List[bytes] = [
    pack(FMT_FOOTER, 7, 34, 1028443341, 9, x, 5, 8)
    for x in [102, 124, 126]
]
APPLICATIONS: List[bytes] = [
    pack(string_fmt(s), *list(s))
    for s in _Applications
]
METHODS: List[bytes] = [
    pack(string_fmt(s), *list(s))
    for s in _Methods
]


if __name__ == '__main__':
    pprint(f"End: {PACKET_END.hex()}")
    pprint(f"Begins: {[x.hex() for x in PACKET_BEGIN]}")
    pprint(f"Header: {FILE_HEADER.hex()}")
    pprint(f"Footers: {[x.hex() for x in FILE_FOOTERS]}")
    pprint(f"Format for GLASSMAJOR: {string_fmt('GLASSMAJOR')}")
    pprint(f"Applications: {APPLICATIONS}")
    pprint(f"Methods: {METHODS}")
