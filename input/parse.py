#!/usr/bin/env python3.7
"""
Parse PDZ files, extracting necessary information
"""

import re
from pprint import pprint
from struct import unpack
from typing import Dict, List, NamedTuple

from input.structures import PACKET_BEGIN, PACKET_END, INTRA_PACKET_BREAK, FMT_VALUES
from input.structures import compound_fmt


# TODO: implement valid PDZ file checking


def _process_compound(compound: bytes) -> str:
    """
    Transform the packet compound into a string

    :param compound: bytes
    :return: str
    """
    comp_ints = unpack(compound_fmt(compound), compound)  # tuple of integers
    comp_str = "".join(chr(x) for x in comp_ints)
    # There are occasionally still some extraneous characters present (likely
    # due to the regex used), so we're just interested in the "regular" chars.
    # TODO: fix regex to only return valid chemical values. Right now it is
    #       also returning, e.g., "TaI" and "Te4" instead of "Ta" and "Te".
    comp = re.findall(r"[A-IK-PR-Z2-9]+", comp_str, flags=re.I)[0]
    return comp


def _process_values(values: bytes) -> NamedTuple:
    """
    Transform the packet values into actual numbers

    :param values: bytes
    :return: Tuple[float, float]
    """
    # Will always be three values, with the concentration duplicated
    # TODO: some sort of check if the error is greater than the concentration?
    concentration, verify_conc, error = unpack(FMT_VALUES, values)
    if concentration != verify_conc:
        raise ValueError(
            f"Two different concentrations detected: "
            f"{concentration} vs {verify_conc}"
        )
    reading = NamedTuple("reading", [("conc", float), ("err", float)])
    return reading(conc=concentration, err=error)


def packets_to_readings(packets: List[bytes]) -> Dict[str, Dict[str, float]]:
    """
    Convert list of packet data into 'Element: {concentration, error}'

    :param packets: List[bytes]
    :return: Dict[str, float]
    """
    readings: Dict[str, Dict[str, float]] = {}
    for packet in packets:
        compound_s, values_s = re.split(INTRA_PACKET_BREAK.hex(), packet.hex())
        compound = _process_compound(bytes.fromhex(compound_s))
        values = _process_values(bytes.fromhex(values_s))
        readings[compound] = values._asdict()
    return readings


def extract_readings(file: bytes) -> Dict[str, Dict[str, float]]:
    """
    Extract the compound concentrations from a PDZ file

    :param file: bytes
    :return: Dict[str, float]
    """
    packet_data_strs: List[str] = []
    for packet_header in PACKET_BEGIN:
        re_packet = packet_header.hex() + "((.{2}){15,30})" + PACKET_END.hex()
        packet_data_strs += re.findall(re_packet, file.hex(), flags=re.DOTALL)
    # The regex returns two matches for every packet: [0] is the packet data,
    # while [1] is the last byte of the data. We don't care about the last byte.
    packet_data_bytes: List[bytes] = [bytes.fromhex(p[0]) for p in packet_data_strs]
    return packets_to_readings(packet_data_bytes)


if __name__ == "__main__":
    from pathlib import Path

    file = Path("./files/").glob("00174*.pdz").__next__()
    with file.open("rb") as f:
        test_packets = f.read()
    pprint(extract_readings(test_packets))
