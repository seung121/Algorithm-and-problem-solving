def set_cover(universe, subsets):
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None
    covered = set()
    cover = []

    while covered != elements:
        subset = max(subsets, key=lambda s:len(s-covered))
        cover.append(subset)
        covered |= subset
    return cover

universe = set(range(1, 11))
subsets = [set([1, 2, 3, 8]),
            set([1, 2, 3, 4, 8]),
            set([1, 2, 3, 4]),
            set([2, 3, 4, 5, 7, 8]),
            set([4, 5, 6, 7]),
            set([5, 6, 7, 9, 10]),
            set([4, 5, 6, 7]),
            set([1, 2, 4, 8]),
            set([6, 9]),
            set([6, 9])]
cover = set_cover(universe, subsets)
print(cover)