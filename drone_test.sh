#!/bin/sh
coverage run --include=bipolar/* tests/__init__.py
coverage report -m --fail-under=85 bipolar/*.py
OUT=$?

STATUS="failed"
if [ "$OUT" = "0" ]; then
    STATUS="passed"
fi

exit $OUT
