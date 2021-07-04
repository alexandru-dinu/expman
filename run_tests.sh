#!/bin/bash

PYTHONPATH=$PWD:$PYTHONPATH py.test expman/ tests/

rm -rf .pytest_cache
