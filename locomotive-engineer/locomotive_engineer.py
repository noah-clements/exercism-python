"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.
    reposition the first two items of the first list to the end, 
    and insert the values from the second list behind (on the right hand side of) the locomotive ID (1). 
    The function should then return a list with the modifications

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a, b, locomotive, *rest = each_wagons_id
    return [locomotive, *missing_wagons, *rest, a, b]


def add_missing_stops(route: dict, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route['stops'] = list(kwargs.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of 3 rows of wagons, represented as (id, color).
    :return: list[list[tuple]] - list of rows of wagons, reorganized so that each color is a column in the row.
    """
    col1, col2, col3 = zip(*wagons_rows)
    return [list(col1), list(col2), list(col3)]

