"""
This module calculates the speed
"""
from prettytable import PrettyTable


def calc_speed(path: int, time: int) -> str:
    """
    Calculates the speed
    :param path: the path traveled
    :param time: for what period of time
    :return: text table with values: 'speed', 'distance traveled', 'time'
    '''
        +------------+------+-------------------+
        | PathTravel | Time |       Speed       |
        +------------+------+-------------------+
        |    1100    |  15  | 73.33333333333333 |
        +------------+------+-------------------+
    '''
    """
    # speed formula
    speed = path / time
    # create table result
    table = PrettyTable(['PathTravel', 'Time', 'Speed'])
    table.add_row([path, time, speed])
    # output result
    return table.get_string()
