from typing import Iterable, Hashable, List, Set


def count_common_elements(*lists: Iterable[Hashable]) -> int:
    """
    Принимает N списков (или любых итерируемых коллекций) и возвращает
    количество одинаковых элементов, которые присутствуют во ВСЕХ списках.

    Считаются уникальные элементы (повторы внутри одного списка не увеличивают результат).

    Пример:
        [1, 2, 2, 3], [2, 3, 4], [0, 2, 3] -> общие {2, 3} -> 2
    """
    if not lists:
        return 0

    common: Set[Hashable] = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
        if not common:
            return 0

    return len(common)
