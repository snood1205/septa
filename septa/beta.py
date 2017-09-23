from .get_json import get_json


def transit_view_beta(route):
    url = 'https://www3.septa.org/beta/TransitView/%s' % route
    return get_json(url)
