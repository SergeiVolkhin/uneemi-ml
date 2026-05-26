"""Sanity benchmark: ImageNet zero-shot top-1 для SigLIP 2.

Логика zero-shot classification:
1. Загрузить stratified subset из HF `mrm8488/ImageNet1K-val` (5/класс = 5000).
2. Построить class embeddings: 1000 классов × ~80 промптов → усреднить через
   PyTorch text encoder SigLIP 2 (однократно, кеш в data/).
3. Прогнать картинки через наш ONNX `Siglip2Encoder`.
4. cosine similarity → argmax → top-1 / top-5 accuracy.

Реализация — см. план Шага 2, Этап 3.

Запуск (после реализации):
    uv run python scripts/sanity_imagenet.py [--subset-size 5000]
"""

from __future__ import annotations

import sys

# Windows console падает на Unicode (м/с, символы перцентилей).
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")


def main() -> int:
    raise NotImplementedError("Sanity ImageNet benchmark не реализован. См. план Шага 2 / Этап 3.")


if __name__ == "__main__":
    raise SystemExit(main())
