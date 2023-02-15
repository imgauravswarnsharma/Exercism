def transform(legacy_data):
    new_data = {}
    for key in legacy_data:
        for values in legacy_data[key]:
            new_data[values.lower()] = key
    return new_data