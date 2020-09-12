Movies Project
==============

# Code Quality

Flake8

```bash
  # apply changes
  docker-compose exec movies flake8 .
```

Black docker commands

```bash
  # run with `check-only` and `diff` options
  docker-compose exec movies black --check --exclude=migrations .
  docker-compose exec movies black --diff --exclude=migrations .

  # apply changes
  docker-compose exec movies black --exclude=migrations .
```

isort

```bash
  # run with `check-only` and `diff` options
  docker-compose exec movies /bin/sh -c "isort ./*/*.py --check-only"
  docker-compose exec movies /bin/sh -c "isort ./*/*.py --diff"

  # apply changes
  docker-compose exec movies /bin/sh -c "isort ./*/*.py"
```
