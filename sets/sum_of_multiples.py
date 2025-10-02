def sum_of_multiples(limit, multiples):
    values = []

    for multiple in multiples:
        if multiple == 0:
            continue
        holder = multiple
        while holder < limit:
            values.append(holder)
            holder += multiple

    unique_elements = set(values)

    return sum(unique_elements)