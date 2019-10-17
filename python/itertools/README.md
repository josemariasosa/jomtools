# Itertools

## 1. Generate combinations out of a list.

https://docs.python.org/3/library/itertools.html#itertools.combinations

```python
l = [1, 2, 3, 4]
size = 2
results = list(itertools.combinations(l, size))
print(results)
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

size = 3
results = list(itertools.combinations(l, size))
print(results)
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

size = 4
results = list(itertools.combinations(l, size))
print(results)
# [(1, 2, 3, 4)]
```

