# -*- coding: utf-8 -*-

__author__ "Rahul Bhalley"

# Some configuration for networks
IMG_DIM = 32 # [32, 256]
if IMG_DIM == 32:   
    Z_DIM = 64
elif IMG_DIM == 256:
    Z_DIM = 100
BATCH_SIZE = 64
MODE = 'wgan' # [wgan, sgan]

# Some other configurations
DATASET = 'mnist' # [mnist, fashion-mnist, cifar-10, cifar-100, ...]
if DATASET in ['fashion-mnist', 'mnist']:
    N_CHANNELS = 1
else:
    N_CHANNELS = 3
BEGIN_ITER = 0
TOTAL_ITERS = 1000000
ITERS_PER_LOG = 100
VERBOSE = True