"""Command-line interface for the image-classification program."""

import argparse


def get_input_args() -> argparse.Namespace:
    """Parse and return the image directory, architecture, and dog-name file."""
    parser = argparse.ArgumentParser(
        description="Classify pet images with a pretrained CNN.",
    )
    parser.add_argument(
        "--dir",
        default="pet_images/",
        help="directory containing the images (default: pet_images/)",
    )
    parser.add_argument(
        "--arch",
        choices=("resnet", "alexnet", "vgg"),
        default="vgg",
        help="CNN architecture (default: vgg)",
    )
    parser.add_argument(
        "--dogfile",
        default="dognames.txt",
        help="file containing valid dog labels (default: dognames.txt)",
    )
    return parser.parse_args()
