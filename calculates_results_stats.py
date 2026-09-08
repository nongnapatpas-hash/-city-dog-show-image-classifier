"""Calculate aggregate accuracy statistics."""


def _percentage(numerator: int, denominator: int) -> float:
    """Return a percentage while safely handling an empty group."""
    return 100.0 * numerator / denominator if denominator else 0.0


def calculates_results_stats(results: dict[str, list]) -> dict[str, float | int]:
    """Return image counts and classification percentages."""
    statistics: dict[str, float | int] = {
        "n_images": len(results),
        "n_dogs_img": 0,
        "n_notdogs_img": 0,
        "n_match": 0,
        "n_correct_dogs": 0,
        "n_correct_notdogs": 0,
        "n_correct_breed": 0,
    }

    for values in results.values():
        label_match = values[2]
        truth_is_dog = values[3]
        prediction_is_dog = values[4]

        statistics["n_match"] += label_match
        statistics["n_dogs_img"] += truth_is_dog

        if truth_is_dog:
            statistics["n_correct_dogs"] += prediction_is_dog
            statistics["n_correct_breed"] += label_match
        elif not prediction_is_dog:
            statistics["n_correct_notdogs"] += 1

    statistics["n_notdogs_img"] = (
        statistics["n_images"] - statistics["n_dogs_img"]
    )
    statistics["pct_match"] = _percentage(
        statistics["n_match"], statistics["n_images"]
    )
    statistics["pct_correct_dogs"] = _percentage(
        statistics["n_correct_dogs"], statistics["n_dogs_img"]
    )
    statistics["pct_correct_breed"] = _percentage(
        statistics["n_correct_breed"], statistics["n_dogs_img"]
    )
    statistics["pct_correct_notdogs"] = _percentage(
        statistics["n_correct_notdogs"], statistics["n_notdogs_img"]
    )
    return statistics
