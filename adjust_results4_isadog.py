"""Mark true and predicted labels as dog or non-dog labels."""

from pathlib import Path


def adjust_results4_isadog(
    results: dict[str, list],
    dogfile: str,
) -> None:
    """Append truth-is-dog and prediction-is-dog flags to every result."""
    dog_names_path = Path(dogfile)
    if not dog_names_path.is_file():
        raise FileNotFoundError(f"Dog-name file not found: {dog_names_path}")

    dog_names = {
        line.strip()
        for line in dog_names_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }

    for values in results.values():
        truth_is_dog = int(values[0] in dog_names)
        prediction_is_dog = int(values[1] in dog_names)
        values.extend([truth_is_dog, prediction_is_dog])
