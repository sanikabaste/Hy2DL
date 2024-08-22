.. Hy2DL documentation master file, created by
   sphinx-quickstart on Wed Aug 21 12:55:11 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Hy2DL's documentation!
=================================

Hy2DL is a python library to create hydrological models for rainfall-runoff prediction, which make use of deep learning methods. The main idea of this repository is to provide models that are 'easy' to understand, interpret and implement. This 'ease', naturally, comes at the cost of code modularity and, to some extent flexibility. The logic of the codes presented here are heavily based on 'NeuralHydrology --- A Python library for Deep Learning research in hydrology' (https://github.com/neuralhydrology/neuralhydrology.git). For a more flexible, robust and modular implementation of deep learning method in hydrological modeling we advice the use of Neural Hydrology.

In addition to Long Short Term Memory (LSTM) network architectures, the repository also features hybrid hydrological models which use an LSTM network combined with a process based rainfall-runoff model and transformer based hydrological model. Regional hydrological models for several datasets namely the CAMELS_GB, CAMELS_US, CAMELS_CH, CAMELS_DE and the CARAVAN are at the user's easy disposal.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage/initialsteps
   usage/datasetzoo
   api
