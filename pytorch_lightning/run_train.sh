#!/bin/bash

python train.py \
    --batch_size 512 \
    --hidden_size 128 \
    --learning_rate 0.001 \
    --max_epochs 10 \
    --dataset_path ${HOME}/workspace/ml-data/ \
    --num_workers 8 \
    --cuda \
    || exit 1
