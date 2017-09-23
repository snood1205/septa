from .get_json import get_json


def regional_rail_station_arrivals_and_departures(station_name, number_of_results=5):
    """
    Returns a list/queue of trains scheduled to arrive at a station in two/both directions. The direction is demarcated
    as either Northbound or Southbound. The directions are obviously not geographical references, but rather a reference
    to the old Reading and Pennsy Railroads. The key to understanding the direction is by using Suburban Station as a
    starting point: Any trains that that move eastbound towards Market East are all considered Northbound; trains going
    from Suburban to 30th St are all Southbound. The 'path' field describes more accurately the path of travel along the
    various branches.
    :param station_name: the station name from which the list will be generated
    :param number_of_results: the number of results desired (defaults to 5)
    :returns: A 'dict' with the following key-value pairs:
      - "direction" (type: string) - As described above a historical directional reference.
      - "path" (type: string) - The route name and the heading on that route formatted as such "R7N" (R7 headed north).
      - "train_id" (type: string) - The train schedule number and ID for that route at that time.
      - "origin" (type: string) - The station at which the train started its route.
      - "destination" (type: string) - The terminus of the route.
      - "status" (type: string) - Whether the train is "On Time" or "n min" where n is the number of minutes late.
      - "service_type" (type: string) - Whether the train is a "LOCAL" or an "EXPRESS"
      - "next_station" (type: string) - The next stop on the train.
      - "sched_time" (type: string, date) - A date string for the scheduled arrival of the train.
      - "depart_time" (type: string, date) - A date string for the scheduled departure of the train.
      - "track" (type: string) - The track on which the train will arrive at the station.
      - "track_change" (type: string | null) - A message related to a track change or null if there is no change.
      - "platform" (type: string) - The platform of the track where the train will arrive.
      - "track_change" (type: string | null) - A message related to a platform change or null if there is no change.
      (date strings are formatted as such "%b %d %Y %I:%M:%S:%f%p").
    :rtype: dict
    """
    url = 'https://www3.septa.org/hackathon/Arrivals/%s/%s' % (station_name, number_of_results)
    return get_json(url)


def train_view():
    """
    Creates a list of all Regional Rail trains on the system. Showing the train's ID number, its starting location, its
    destination, and if it is late or not.
    :returns: An list of 'dict's with the following key-value pairs:
      - "lat" (type: string) - The decimal latitude of the bus or trolley.
      - "lng" (type: string) - The decimal longitude of the bus or trolley.
      - "trainno" (type: string, foreign key) - The train schedule number and ID for that route at that time.
      - "service" (type: string) - Whether the train is a "LOCAL" or an "EXPRESS"
      - "dest" (type: string) - The terminus of the route.
      - "nextstop" (type: string) - The next stop on the train.
      - "late" (type: number) - The number number of minutes the train is late.
      - "SOURCE" (type: string) - The station at which the train started its route.
      - "TRACK" (type: string) - The track on which the train will arrive at the station.
      - "TRACK_CHANGE" (type: string) - A message related to a track change or "" if there is no change.
    :rtype: list<dict>
    """
    return get_json('https://www3.septa.org/hackathon/TrainView/')


def next_to_arrive(start_station, end_station, number_of_results=4):
    """
    Returns departure and arrival times between two different stations.
    :param start_station: the station name from which the train will depart.
    :param end_station: the station name to which the train will arrive.
    :param number_of_results: the number of results desired (defaults to 4).
    :returns: A list of 'dict's with the following key-value pairs:
      - "orig_train":
    """
    url = 'https://www3.septa.org/hackathon/NextToArrive/%s/%s/%s' % (start_station, end_station, number_of_results)
    return get_json(url)


def transit_view(route):
    url = 'https://www3.septa.org/hackathon/TransitView/%s' % route
    return get_json(url)


def transit_view_all():
    return get_json('https://www3.septa.org/hackathon/TransitViewAll/')


def bus_detours(route=None):
    if route is None:
        return get_json('https://www3.septa.org/hackathon/BusDetours/')
    else:
        url = 'https://www3.septa.org/hackathon/BusDetours/%s' % route
        return get_json(url)


def alerts(route=None):
    if route is None:
        return get_json('https://www3.septa.org/hackathon/Alerts/')
    else:
        url = 'https://www3.septa.org/hackathon/Alerts/%s' % route
        return get_json(url)


def elevator_outages():
    return get_json('https://www3.septa.org/hackathon/elevator/')
