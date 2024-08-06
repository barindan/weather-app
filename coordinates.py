from dataclasses import dataclass
from subprocess import Popen, PIPE

import config
from exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    """Return current coordinates using MacBook GPS"""
    coordinates = _get_whereami_coordinates()
    return coordinates


def _get_whereami_coordinates() -> Coordinates:
    """Using WhereAmi tool - https://github.com/robmathers/WhereAmI"""
    whereami_output = _get_whereami_output()
    return _parse_coordinates(whereami_output)


def _get_whereami_output() -> bytes:
    process = Popen(['whereami'], stdout=PIPE)
    (output, error) = process.communicate()
    exit_code = process.wait()
    if error is not None or exit_code != 0:
        raise CantGetCoordinates
    return output

def _parse_coordinates(whereami_output: bytes) -> Coordinates:
    try:
        output = whereami_output.decode().strip().lower().split("\n")
    except UnicodeDecodeError:
        raise CantGetCoordinates

    latitude = longitude = None
    for line in output:
        if line.startswith("latitude:"):
            latitude = float(line.split()[1])
        if line.startswith("longitude:"):
            longitude = float(line.split()[1])
    if config.USE_ROUNDED_COORDS:
        latitude, longitude = map(lambda c: round(c, 1), [latitude, longitude])
    return Coordinates(longitude=longitude, latitude=latitude)