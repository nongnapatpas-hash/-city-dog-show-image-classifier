#!/usr/bin/env python3
"""Run a quick smoke test of the pretrained classifier."""

from classifier import classifier


def main() -> None:
    """Classify a known collie image with VGG."""
    image_path = "pet_images/Collie_03797.jpg"
    model_name = "vgg"
    prediction = classifier(image_path, model_name)
    print(f"{image_path} classified by {model_name}: {prediction}")


if __name__ == "__main__":
    main()
