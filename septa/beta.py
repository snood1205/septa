from .get_json import get_json


def transit_view_beta(route):
    """
    [BETA] Get the GTFS Trip IDs for a specified route.
    :param route: a valid bus or trolley route.
    :returns: A 'dict' with the following key-value pairs:
      - "trip" (type: string) - The GTFS trip ID.
      - "lat" (type: string) - The decimal latitude of the bus or trolley.
      - "lng" (type: string) - The decimal longitude of the bus or trolley.
      - "label" (type: string) - The vehicle's label.
      - "VehicleID" (type: string) - The vehicle's numeric ID.
      - "BlockID" (type: string) - The block's ID (i.e. an ID might correspond to the 1900 Block of Arch St.)
      - "Direction" (type: string) - The cardinal direction in which the vehicle is headed.
      - "destination" (type: string) - The terminus of the route.
      - "Offset" (type: string) - The age of the observation in minutes (floored).
      - "Offset_sec" (type: string) - The age of the observation in seconds.
    :rtype: dict
    """
    url = 'https://www3.septa.org/beta/TransitView/%s' % route
    return get_json(url)
