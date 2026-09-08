"""Build ground-truth labels from image filenames."""

from pathlib import Path


SUPPORTED_IMAGE_TYPES = {".jpg", ".jpeg", ".png"}


def get_pet_labels(image_dir: str) -> dict[str, list[str]]:
    """Return a filename-to-label mapping for supported images in a directory."""
    directory = Path(image_dir)
    if not directory.is_dir():
        raise FileNotFoundError(f"Image directory not found: {directory}")

    results: dict[str, list[str]] = {}
    for image_path in sorted(directory.iterdir()):
        if (
            image_path.name.startswith(".")
            or not image_path.is_file()
            or image_path.suffix.lower() not in SUPPORTED_IMAGE_TYPES
        ):
            continue

        words = [
            word
            for word in image_path.stem.lower().split("_")
            if word.isalpha()
        ]
        results[image_path.name] = [" ".join(words)]

    return results
