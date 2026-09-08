"""Classify images and compare predictions with filename-derived labels."""

from pathlib import Path

from classifier import classifier


def classify_images(
    images_dir: str,
    results: dict[str, list],
    model: str,
) -> None:
    """Append the classifier label and exact alias-match flag to each result."""
    directory = Path(images_dir)

    for filename, values in results.items():
        predicted_label = classifier(
            str(directory / filename),
            model,
        ).lower().strip()

        accepted_aliases = {
            alias.strip() for alias in predicted_label.split(",")
        }
        is_match = int(values[0] in accepted_aliases)
        values.extend([predicted_label, is_match])
