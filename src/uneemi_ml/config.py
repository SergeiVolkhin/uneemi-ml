"""Конфигурация ML-пайплайна Uneemi: пути и константы."""

from __future__ import annotations

from pathlib import Path

MODEL_ID: str = "google/siglip2-base-patch16-224"
IMAGE_SIZE: int = 224
EMBED_DIM: int = 768
ORT_INTRA_OP_THREADS: int = 4

PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]
MODELS_DIR: Path = PROJECT_ROOT / "models"
DATA_DIR: Path = PROJECT_ROOT / "data"
ONNX_VISION_PATH: Path = MODELS_DIR / "siglip2_vision.onnx"
