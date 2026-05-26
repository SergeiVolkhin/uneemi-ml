# Performance Benchmark — Siglip2Encoder

История прогонов performance-бенчмарка. Каждая секция — отдельный запуск `scripts/bench_inference.py`. Новые секции аппендятся в конец.

---

## Прогон 2026-05-26 20:03:07

**Commit:** `ea13908`
**Host:** Windows 10, Intel64 Family 6 Model 151 Stepping 2, GenuineIntel (12C/20T), 31.9 GB RAM
**Python:** 3.11.9 | **onnxruntime:** 1.26.0 | **ORT threads:** 4
**RAM после init Siglip2Encoder:** 416.4 MB

### Латентность

| Операция | p50 (мс) | p95 (мс) | p99 (мс) | per_img (мс) | ram_peak_mb |
|---|---|---|---|---|---|
| preprocess (PIL+normalize) | 2.96 | 3.33 | 3.65 | — | — |
| encode(single) | 82.69 | 89.76 | 92.02 | — | 545.3 |
| encode_batch(1) | 81.88 | 87.63 | 92.16 | 81.88 | 545.5 |
| encode_batch(8) | 657.94 | 815.70 | 826.95 | 82.24 | 704.1 |
| encode_batch(16) | 1312.95 | 1379.79 | 1401.55 | 82.06 | 889.0 |
| encode_batch(32) | 2657.02 | 2698.95 | 2715.01 | 83.03 | 1256.1 |

### Full board pipeline (40 изображений, чанки 32+8)

- t_preprocess: 105.99 мс
- t_encode: 3256.32 мс
- **t_total: 3360.10 мс**

### Таргеты

- [❌] p99 encode(single) ≤ 30 мс (фактическое: 92.02 мс)
- [❌] p99 encode_batch(32) ≤ 500 мс (фактическое: 2715.01 мс)
- [x] ram_peak_bs32 ≤ 2048 MB (фактическое: 1256.1 MB)
