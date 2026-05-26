"""Sanity benchmark: XM3600 image-text retrieval (только русский язык).

Логика zero-shot retrieval:
1. Скачать XM3600 (captions + images) с google.github.io/crossmodal-3600/.
2. Отфильтровать RU captions (3600 изображений × 2 RU-captions = 7200 пар).
3. Image embeddings через наш ONNX `Siglip2Encoder`.
4. Text embeddings через PyTorch text encoder SigLIP 2.
5. Метрики: image→text R@1/R@5, text→image R@1/R@5.

Реализация — см. план Шага 2, Этап 4.

Запуск (после реализации):
    uv run python scripts/sanity_xm3600_ru.py
"""

from __future__ import annotations

import sys

# Windows console падает на Unicode.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")


def main() -> int:
    raise NotImplementedError("Sanity XM3600 RU benchmark не реализован. См. план Шага 2 / Этап 4.")


if __name__ == "__main__":
    raise SystemExit(main())
