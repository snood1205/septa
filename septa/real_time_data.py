from .get_json import get_json


def regional_rail_station_arrivals_and_departures(station_name, number_of_results=5):
    url = 'https://www3.septa.org/hackathon/Arrivals/%s/%s' % (station_name, number_of_results)
    return get_json(url)


def train_view():
    return get_json('https://www3.septa.org/hackathon/TrainView/')


def next_to_arrive(start_station, end_station, number_of_results=4):
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
