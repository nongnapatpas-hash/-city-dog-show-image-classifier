"""Small ImageNet inference wrapper used by the project.

The project starter supplied this classifier interface. This version keeps the
same public function while loading only the requested model and using the
current TorchVision weights API.
"""

import ast
from functools import lru_cache
from pathlib import Path

import torch
from PIL import Image
from torchvision import models, transforms


MODEL_CONFIG = {
    "resnet": (models.resnet18, models.ResNet18_Weights.IMAGENET1K_V1),
    "alexnet": (models.alexnet, models.AlexNet_Weights.IMAGENET1K_V1),
    "vgg": (models.vgg16, models.VGG16_Weights.IMAGENET1K_V1),
}

PREPROCESS = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ]
)

LABELS_PATH = Path(__file__).with_name("imagenet1000_clsid_to_human.txt")
with LABELS_PATH.open(encoding="utf-8") as labels_file:
    IMAGENET_LABELS = ast.literal_eval(labels_file.read())


@lru_cache(maxsize=len(MODEL_CONFIG))
def _load_model(model_name: str) -> torch.nn.Module:
    """Load and cache one pretrained model in evaluation mode."""
    try:
        factory, weights = MODEL_CONFIG[model_name]
    except KeyError as error:
        valid = ", ".join(MODEL_CONFIG)
        raise ValueError(
            f"Unknown model '{model_name}'. Choose one of: {valid}."
        ) from error
    return factory(weights=weights).eval()


def classifier(img_path: str, model_name: str) -> str:
    """Return the ImageNet label predicted for an image."""
    with Image.open(img_path) as image:
        image_tensor = PREPROCESS(image.convert("RGB")).unsqueeze(0)

    model = _load_model(model_name)
    with torch.inference_mode():
        predicted_index = model(image_tensor).argmax(dim=1).item()

    return IMAGENET_LABELS[predicted_index]
