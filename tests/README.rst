=============
pyngdom tests
=============

Here are the simple test that will be run by travis. Some test needs credential, and i will not put them on travis.
So if you want to run test you should run them like:

.. code:: bash

    [Path/to/pyngdom.git] PYTHONPATH=`pwd` PINGDOM_USERNAME=user@epi10.cl PINGDOM_PASSWORD=password PINGDOM_RUMID=8989cbbb  py.test tests

