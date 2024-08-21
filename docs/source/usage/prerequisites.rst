Prerequisites
-------------
As a first step you need a Python environment with all required dependencies. 
The packages used to run the codes are indicated at the beginning of each notebook. It must be considered that the codes for the data-driven models run better in GPU, therefore a PyTorch version that supports GPU should be installed!


Cloning the repository
------------

If you want to try implementing your own models or datasets, you'll need an editable installation.
For this, start by downloading or cloning the repository to your local machine.
If you use git, you can run:

.. code-block::

    git clone https://github.com/KIT-HYD/Hy2DL.git

Data
----
Training and evaluating models requires a dataset.
If you're unsure where to start, a common dataset is CAMELS US, available at
`CAMELS US (NCAR) <https://ral.ucar.edu/solutions/products/camels>`_.
This dataset is used in all of our tutorials and we have a `dedicated tutorial <../tutorials/data-prerequisites.nblink>`_ with download instructions that you might want to look at.

