from .get_json import get_json


def regional_rail_schedules(train_number):
    url = 'https://www3.septa.org/hackathon/RRSchedules/%s' % train_number
    return get_json(url)


def bus_schedules(stop_id):
    url = 'https://www3.septa.org/hackathon/BusSchedules/%s' % stop_id
    return get_json(url)


def list_of_stops_by_route(route):
    url = 'https://www3.septa.org/hackathon/Stops/%s' % route
    return get_json(url)


def system_locations(latitude, longitude, station_type=None, radius=None):
    if station_type not in ['bus_stops', 'perk_locations', 'rail_stations', 'sales_locations', 'trolley_stops', None]:
        raise ValueError('Invalid station type: see documentation here http://www3.septa.org.')

    if station_type is None and radius is None:
        url = 'https://www3.septa.org/hackathon/locations/get_locations.php?lon=%s&lat=%s' % \
              (latitude, longitude)
    elif station_type is None:
        url = 'https://www3.septa.org/hackathon/locations/get_locations.php?lon=%s&lat=%s&radius=%s' % \
              (latitude, longitude, radius)
    elif radius is None:
        url = 'https://www3.septa.org/hackathon/locations/get_locations.php?lon=%s&lat=%s&type=%s' % \
              (latitude, longitude, station_type)
    else:
        url = 'https://www3.septa.org/hackathon/locations/get_locations.php?lon=%s&lat=%s&type=%s&radius=%s' % \
              (latitude, longitude, station_type, radius)
    return get_json(url)
