From command line
=======================

In order to plot the polysemy of all words do:

.. code-block:: python

    python -m word_polysemy.main <type_of_plot [None, boxplot, scatter, bar]>

Example:

.. code-block:: python

    python -m word_polysemy.main boxplot

In order to calculate the average polysemy of all words do:

.. code-block:: python

    python -m word_polysemy.main <type_of_plot> --average_yes

Example:

.. code-block:: python

    python -m word_polysemy.main boxplot --average_yes
