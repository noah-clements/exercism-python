def flatten(iterable):
    out = []
    for item in iterable:
        if isinstance(item, list):
            for subitem in flatten(item):
                if subitem is not None:
                    out.append(subitem)
        elif item is not None:
            out.append(item)
    return out
