def build_tree(xs):
    if not xs:
        return {}

    head, *tail = xs
    mid = len(xs) // 2

    return {"val": head, "lhs": build_tree(tail[:mid]), "rhs": build_tree(tail[mid:])}
