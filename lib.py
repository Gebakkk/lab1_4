from typing import Iterable, Hashable, List, Set


def count_common_elements(*lists: Iterable[Hashable]) -> int:

    if not lists:
        return 0

    common: Set[Hashable] = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
        if not common:
            return 0

    return len(common)
