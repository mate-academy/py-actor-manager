# Сheck Your Code Against the Following Points

## Don't Push db files

Make sure you don't push db files (files with `.sqlite`, `.db3`, etc. extension).

## Code Style

1. Don't forget that the name of the class should be in the singular form.

Good Example:
```python
class Manager:
  pass
```

Bad Example:
```python
class Managers:
  pass
```

2. If db contains not only one object - name it plural.

Good Example:
```python
self.table_name = "objects"
```

Bad Example:
```python
self.table_name = "object"
```
