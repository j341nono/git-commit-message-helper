#!/bin/bash

REPOGITORY_URL="https://github.com/j341nono/git-commit-message-helper.git"

set -e

uv tool install "git+$REPOGITORY_URL"