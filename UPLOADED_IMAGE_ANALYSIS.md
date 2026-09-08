# Uploaded Image Analysis

Four personal test images were evaluated with ResNet, AlexNet, and VGG:

- `Dog_01.jpg`
- `Dog_02.jpg`, a horizontally flipped copy of the first dog image
- `Tiger_01.jpg`
- `coffee_01.jpg`

## Breed predictions

The three architectures did not return the same breed for `Dog_01.jpg`.
ResNet predicted Lhasa Apso, while AlexNet and VGG predicted Shih-Tzu.

ResNet and AlexNet were also sensitive to the horizontal flip:

| Model | Dog 01 | Dog 02 |
|---|---|---|
| ResNet | Lhasa Apso | Shih-Tzu |
| AlexNet | Shih-Tzu | Lhasa Apso |
| VGG | Shih-Tzu | Shih-Tzu |

VGG was the only architecture that produced the same breed prediction for
both orientations.

## Dog/non-dog predictions

All three architectures correctly treated the tiger and coffee images as
non-dogs. They predicted a tiger label for `Tiger_01.jpg` and an espresso
label for `coffee_01.jpg`.

## Conclusion

VGG performed best on this four-image experiment. It remained consistent
after the dog image was flipped and correctly distinguished both non-dog
images. ResNet and AlexNet correctly identified the dog and non-dog groups,
but their breed predictions changed after the horizontal flip.
