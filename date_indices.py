def get_index_date(index_name):
    return int(index_name.split('-')[-1])


def filter_indices(indices, date_from=None, date_to=None):
    if date_to and date_from:
        result = [index for index in indices if (date_from <= get_index_date(index) <= date_to)]
    elif date_to:
        result = [index for index in indices if get_index_date(index) <= date_to]
    elif date_from:
        result = [index for index in indices if date_from <= get_index_date(index)]
    else:
        result = indices
    if date_from:
        possible_previous_index = [index for index in indices if get_index_date(index) <= date_from]
        if len(possible_previous_index):
            result.append(max(possible_previous_index, key=get_index_date))

    return result
