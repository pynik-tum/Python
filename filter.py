def deduplicate(entries):
    temp = list(entries)
    for t in temp:
        while(entries.count(t) > 1):
            entries.remove(t)
    return entries
