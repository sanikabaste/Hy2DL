Initial Steps
==============

Prerequisites
-------------
As a first step you need a Python environment with all required dependencies. The packages used to run the codes are indicated at the beginning of each notebook.
It must be considered that the codes for the data-driven models run better in GPU, therefore a PyTorch version that supports GPU should be installed!


Cloning the repository
------------

If you want to try implementing your own models or datasets, it is advisable to clone the repository.
If you are well versed with git, you can run the following:

.. code-block::

    git clone https://github.com/KIT-HYD/Hy2DL.git

Data
----
Training and evaluating models requires a dataset.
If you're unsure where to start, a common dataset is CAMELS US, available at
`CAMELS US (NCAR) <https://ral.ucar.edu/solutions/products/camels>`_.

Additionally, the repository also includes experiments which make use of the 'CAMELS GB <https://doi.org/10.5285/8344e4f3-d2ea-44f5-8afa-86d2987543a9>',
'CAMELS CH <https://zenodo.org/records/10354485>', CAMELS DE and the CARAVAN datasets. 

The datasets are freely available for public use. The downloaded datasets should be
uploaded to the 'data' folder ensuring that the folder structure remains intact. Ensuring that the folder structure or their names remain intact is essential
while using the classes meant to create the datasets.

