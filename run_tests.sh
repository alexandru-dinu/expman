#!/bin/bash

PYTHONPATH=$PWD:$PYTHONPATH py.test src/ tests/

rm -rf .pytest_cache
