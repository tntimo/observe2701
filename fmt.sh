#!/bin/sh
set -e

poetry run ruff check --fix src tests
