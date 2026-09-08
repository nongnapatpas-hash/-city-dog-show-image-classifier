"""Format and print image-classification results."""


PERCENTAGE_LABELS = {
    "pct_match": "Overall label match",
    "pct_correct_dogs": "Dogs classified correctly",
    "pct_correct_breed": "Dog breeds classified correctly",
    "pct_correct_notdogs": "Non-dogs classified correctly",
}


def print_results(
    results: dict[str, list],
    statistics: dict[str, float | int],
    model: str,
    print_incorrect_dogs: bool = False,
    print_incorrect_breed: bool = False,
) -> None:
    """Print summary statistics and optional misclassification details."""
    print(f"\nClassification summary — {model.upper()}")
    print(f"{'Images':34}: {statistics['n_images']:3d}")
    print(f"{'Dog images':34}: {statistics['n_dogs_img']:3d}")
    print(f"{'Non-dog images':34}: {statistics['n_notdogs_img']:3d}")

    for key, label in PERCENTAGE_LABELS.items():
        print(f"{label:34}: {statistics[key]:5.1f}%")

    dog_errors = [
        (filename, values)
        for filename, values in results.items()
        if values[3] != values[4]
    ]
    if print_incorrect_dogs and dog_errors:
        print("\nIncorrect dog/non-dog assignments")
        for filename, values in dog_errors:
            print(
                f"- {filename}: truth='{values[0]}', "
                f"prediction='{values[1]}'"
            )

    breed_errors = [
        (filename, values)
        for filename, values in results.items()
        if values[3] == values[4] == 1 and values[2] == 0
    ]
    if print_incorrect_breed and breed_errors:
        print("\nIncorrect dog-breed assignments")
        for filename, values in breed_errors:
            print(
                f"- {filename}: truth='{values[0]}', "
                f"prediction='{values[1]}'"
            )
