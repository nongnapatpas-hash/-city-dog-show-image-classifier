# Image Classification for a City Dog Show

[ภาษาไทย](README_TH.md)

A Python project comparing **AlexNet**, **ResNet**, and **VGG** for identifying
dogs, distinguishing non-dogs, and classifying dog breeds.

## Overview

This project simulates image validation for a city dog-show registration
system. It uses an existing ImageNet-pretrained convolutional neural network
(CNN) classifier and focuses on the Python workflow around that classifier:

1. Read command-line arguments.
2. Extract ground-truth labels from image filenames.
3. Classify each image with a selected CNN architecture.
4. Determine whether the true and predicted labels represent dogs.
5. Calculate accuracy statistics and runtime.
6. Compare AlexNet, ResNet, and VGG.

The project uses a supplied pretrained classifier; it does not train a new
neural network.

## Results

The supplied dataset contains 40 images: 30 dogs and 10 non-dogs.

| Model | Dogs correct | Non-dogs correct | Breeds correct | Label match | Runtime* |
|---|---:|---:|---:|---:|---:|
| ResNet | 100.0% | 90.0% | 90.0% | 82.5% | 5 s |
| AlexNet | 100.0% | 100.0% | 80.0% | 75.0% | 2 s |
| VGG | 100.0% | 100.0% | 93.3% | 87.5% | 19 s |

\*Runtime depends on the hardware and execution environment.

**VGG was the best overall model.** It perfectly separated dogs from non-dogs
and achieved the highest breed accuracy. AlexNet was the fastest and is a good
alternative when dog/non-dog identification and speed matter more than breed
accuracy.

## Uploaded-image experiment

Four additional images tested robustness to a horizontal flip and to unrelated
objects:

| Model | `Dog_01.jpg` | `Dog_02.jpg` (flipped) | `Tiger_01.jpg` | `coffee_01.jpg` |
|---|---|---|---|---|
| ResNet | Lhasa Apso | Shih-Tzu | Tiger / not dog | Espresso / not dog |
| AlexNet | Shih-Tzu | Lhasa Apso | Tiger / not dog | Espresso / not dog |
| VGG | Shih-Tzu | Shih-Tzu | Tiger / not dog | Espresso / not dog |

VGG was the most consistent model because it returned the same breed for the
original and horizontally flipped dog images. All three models correctly
treated the tiger and coffee images as non-dogs.

## Installation

Python 3.10 or newer is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

The pretrained weights are downloaded automatically on the first run and may
require approximately 1 GB of disk space.

## Usage

Run one architecture:

```bash
python3 check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

Valid values for `--arch` are `resnet`, `alexnet`, and `vgg`. Without arguments,
the program uses `pet_images/`, `vgg`, and `dognames.txt`.

Run all architectures on the supplied images:

```bash
sh run_models_batch.sh
```

Run all architectures on the uploaded images:

```bash
sh run_models_batch_uploaded.sh
```

Generated reports are written to `results/`.

## Project structure

```text
.
├── check_images.py
├── get_input_args.py
├── get_pet_labels.py
├── classify_images.py
├── adjust_results4_isadog.py
├── calculates_results_stats.py
├── print_results.py
├── classifier.py
├── dognames.txt
├── imagenet1000_clsid_to_human.txt
├── pet_images/
├── uploaded_images/
├── results/
├── UPLOADED_IMAGE_ANALYSIS.md
├── run_models_batch.sh
└── run_models_batch_uploaded.sh
```

## Learning outcomes

- Command-line interfaces with `argparse`
- Dictionaries, lists, functions, and mutable data
- File and string processing
- Accuracy and percentage calculations
- Runtime measurement
- Comparing model accuracy with computational cost

## Attribution

Completed as part of Udacity's **AI Programming with Python** coursework.
The starter code, pretrained-classifier wrapper, mapping data, and supplied pet
images originate from the
[Udacity AIPND Revision repository](https://github.com/udacity/AIPND-revision).
The application workflow and portfolio-oriented refactoring in this repository
were completed by Nongnapat Pasittungkul.

Before publishing, ensure that you have permission to redistribute any personal
images in `uploaded_images/`.
