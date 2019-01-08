from datetime import datetime, timedelta


def get_datetime(time):
    """Sets a GOES formatted date(string) to a datetime object.

    Arguments:
        time {str} -- GOES formatted date.

    Returns:
        {datetime} -- The date formatted in datetime.
    """
    year = int(time[0:4])
    month = int(time[5:7])
    day = int(time[8:10])
    hour = int(time[11:13])
    minute = int(time[14:16])
    second = int(time[17:19])
    return datetime(year, month, day, hour, minute, second)


def get_correct_goes_index(goes_index, begin, end):
    """Get begin and end indexes set from a timerange.

    Arguments:
        goes_index {pandas.Index} -- GOES dataframe's index.
        begin {str} -- GOES formatted date of the begging point.
        end {str} -- GOES formatted date of the ending point.

    Returns:
        begin, end {str} -- begin and and indexes from the dataframe.
    """
    difference = timedelta(seconds=1)
    begin = get_datetime(begin)
    end = get_datetime(end)
    found_begin = False
    found_end = False

    for index in goes_index:
        new_index = get_datetime(str(index)[0:19])

        if ((new_index == begin or new_index == begin-difference or
                new_index == begin-2*difference) and not found_begin):
            found_begin = True
            begin = index
            continue

        if ((new_index == end or new_index == end+difference or
                new_index == end+2*difference) and not found_end):
            found_end = True
            end = index
            continue

    return begin, end
