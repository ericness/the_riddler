import copy
from typing import List


class Score:
    def __init__(self) -> None:
        self.saf_count: int = 0
        self.fg_count: int = 0
        self.td_count: int = 0
        self.td_1_count: int = 0
        self.td_2_count: int = 0

    def total(self) -> int:
        return (
            self.saf_count * 2
            + self.fg_count * 3
            + self.td_count * 6
            + self.td_1_count * 7
            + self.td_2_count * 8
        )

    def __eq__(self, __o: object) -> bool:
        return (
            self.saf_count == __o.saf_count
            and self.fg_count == __o.fg_count
            and self.td_count == __o.td_count
            and self.td_1_count == __o.td_1_count
            and self.td_2_count == __o.td_2_count
        )

    def __hash__(self) -> int:
        return hash(
            f"{self.saf_count}|{self.fg_count}|{self.td_count}|{self.td_1_count}|{self.td_2_count}"
        )


def count_score_paths(target: int, score: Score) -> List[Score]:
    """Calculate number of ways to target score.

    Args:
        target (int): Score to target.

    Returns:
        int: Count of ways.
    """
    if target == 2:
        result = copy.deepcopy(score)
        result.saf_count += 1
        return [result]
    elif target == 3:
        result = copy.deepcopy(score)
        result.fg_count += 1
        return [result]
    elif target == 4:
        result = copy.deepcopy(score)
        result.saf_count += 2
        return [result]
    elif target == 5:
        result = copy.deepcopy(score)
        result.saf_count += 1
        result.fg_count += 1
        return [result]
    elif target == 6:
        result1 = copy.deepcopy(score)
        result1.saf_count += 3
        result2 = copy.deepcopy(score)
        result2.fg_count += 2
        result3 = copy.deepcopy(score)
        result3.td_count += 1
        return [result1, result2, result3]
    elif target == 7:
        result1 = copy.deepcopy(score)
        result1.saf_count += 2
        result1.fg_count += 1
        result2 = copy.deepcopy(score)
        result2.td_1_count += 1
        return [result1, result2]
    elif target == 8:
        result1 = copy.deepcopy(score)
        result1.saf_count += 4
        result2 = copy.deepcopy(score)
        result2.fg_count += 2
        result2.saf_count += 1
        result3 = copy.deepcopy(score)
        result3.td_count += 1
        result3.saf_count += 1
        result4 = copy.deepcopy(score)
        result4.td_2_count += 1
        return [result1, result2, result3, result4]

    result = []
    if target - 2 > 1:
        tmp_score = copy.deepcopy(score)
        tmp_score.saf_count += 1
        result.extend(count_score_paths(target - 2, tmp_score))
    if target - 3 > 1:
        tmp_score = copy.deepcopy(score)
        tmp_score.fg_count += 1
        result.extend(count_score_paths(target - 3, tmp_score))
    if target - 6 > 1:
        tmp_score = copy.deepcopy(score)
        tmp_score.td_count += 1
        result.extend(count_score_paths(target - 6, tmp_score))
    if target - 7 > 1:
        tmp_score = copy.deepcopy(score)
        tmp_score.td_1_count += 1
        result.extend(count_score_paths(target - 7, tmp_score))
    if target - 8 > 1:
        tmp_score = copy.deepcopy(score)
        tmp_score.td_2_count += 1
        result.extend(count_score_paths(target - 8, tmp_score))
    return result


if __name__ == "__main__":
    score = 14
    result = []
    paths = count_score_paths(score, Score())
    count = len(set(paths))
    print(f"Score Paths for {score}: {count}")
