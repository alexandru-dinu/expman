#!/bin/bash

PYTHONPATH=$PWD:$PYTHONPATH py.test \
    --exitfirst \
    --hypothesis-show-statistics \
    src/ tests/
