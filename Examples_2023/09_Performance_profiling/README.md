# Performance profiling

Measure the performance of your code with different methods.

Nice visualization with `snakeviz` module.

```bash
python -m cProfile -o program.prof my_program.py
snakeviz program.prof
```