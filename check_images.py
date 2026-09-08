#!/usr/bin/env python3
"""Run the complete pet-image classification workflow."""

from time import perf_counter

from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from classify_images import classify_images
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from print_results import print_results


def main() -> None:
    """Classify the selected image directory and print summary statistics."""
    start_time = perf_counter()
    args = get_input_args()

    results = get_pet_labels(args.dir)
    classify_images(args.dir, results, args.arch)
    adjust_results4_isadog(results, args.dogfile)
    statistics = calculates_results_stats(results)

    print_results(
        results,
        statistics,
        args.arch,
        print_incorrect_dogs=True,
        print_incorrect_breed=True,
    )

    elapsed_seconds = int(perf_counter() - start_time)
    hours, remainder = divmod(elapsed_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\nTotal elapsed runtime: {hours:02d}:{minutes:02d}:{seconds:02d}")


if __name__ == "__main__":
    main()
