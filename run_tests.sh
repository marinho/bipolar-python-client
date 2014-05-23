#!/bin/bash
./env/bin/python -c "from bipolar.version import version_number; print 'Version', version_number"

echo "Running tests"
./env/bin/coverage run --include=bipolar/* tests/__init__.py
OUT=$?
if [ "$OUT" == "0" ]; then
    ./env/bin/coverage report -m --fail-under=85 bipolar/*.py
    OUT=$?
fi

exit $OUT
