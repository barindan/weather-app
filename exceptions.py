class CantGetCoordinates(Exception):
    """Program can't get current GPS coordinates"""

class ApiServiceError(Exception):
    """Can't get data from this API point"""