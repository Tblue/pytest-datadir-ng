datadir-ng plugin for pytest |pypi-badge|
=========================================

The ``datadir-ng`` plugin for pytest_ provides the ``datadir``
and ``datadir_copy`` fixtures which allow test functions to easily access resources
in data directories. It was inspired by the `pytest-datadir plugin`_ and is intended
to be a more flexible version of that plugin (hence the "ng" part in its name -- as
in "next generation").

This plugin provides two fixtures:

- The datadir_ fixture allows test functions and methods to access resources in
  so-called "data directories".
- The `datadir_copy`_ fixture is similar to the datadir_ fixture, but it copies the
  requested resources to a temporary directory first so that test functions or
  methods can modify their resources on-disk without affecting other test functions
  and methods.

Installation
------------

Just do::

    pip install pytest-datadir-ng

.. _datadir:

The datadir fixture
-------------------

The "datadir" fixture allows test functions and methods to access resources in
so-called "data directories".

The fixture behaves like a dictionary. Currently, only retrieving items using the
``d[key]`` syntax is supported. Things like iterators, ``len(d)`` etc. are not.

How the fixture looks for resources is best described by an example.
Let us assume the following directory structure for your tests::

    tests/
    +-- test_one.py
    +-- test_two.py
    +-- data/
    |   +-- global.dat
    +-- test_one/
    |   +-- test_func/
    |       +-- data.txt
    +-- test_two/
        +-- TestClass/
            +-- test_method/
                +-- strings.prop

The file ``test_one.py`` contains the following function:

.. code:: python

    def test_func(datadir):
        data_path = datadir["data.txt"]

        # ...

The file ``test_two.py`` contains the following class:

.. code:: python

    class TestClass(object):
        def test_method(self, datadir):
            strings_path = datadir["strings.prop"]

            # ...

When the ``test_func()`` function asks for the ``data.txt`` resource, the
following directories are searched for a file or directory named ``data.txt``,
in this order:

- ``tests/test_one/test_func/``
- ``tests/test_one/``
- ``tests/data/test_one/test_func/``
- ``tests/data/test_one/``
- ``tests/data/``

The path to the first existing file (or directory) is returned as a
py.path.local_ object. In this case, the returned path would be
``tests/test_one/test_func/data.txt``.

When the ``test_method()`` method asks for the ``strings.prop`` resource,
the following directories are searched for a file or directory with the name
``strings.prop``, in this order:

- ``tests/test_two/TestClass/test_method/``
- ``tests/test_two/TestClass/``
- ``tests/test_two/``
- ``tests/data/test_two/TestClass/test_method/``
- ``tests/data/test_two/TestClass/``
- ``tests/data/test_two/``
- ``tests/data/``

Here, this would return the path
``tests/test_two/TestClass/test_method/strings.prop``.

As you can see, the searched directory hierarchy is slighly different if a
*method* instead of a *function* asks for a resource. This allows you to
load different resources based on the name of the test class, if you wish.

Finally, if a test function or test method would ask for a resource named
``global.dat``, then the resulting path would be ``tests/data/global.dat``
since no other directory in the searched directory hierarchy contains
a file named ``global.dat``. In other words, the ``tests/data/`` directory
is the place for global (or fallback) resources.

If a resource cannot be found in *any* of the searched directories, a
`KeyError` is raised.

.. _datadir_copy:

The datadir_copy fixture
------------------------

The "datadir_copy" fixture is similar to the datadir_ fixture, but copies the requested resources to a
temporary directory first so that test functions or methods can modify their resources on-disk without affecting
other test functions and methods.

Each test function or method gets its own temporary directory and thus its own fresh copies of the resources it
requests.

**Caveat:** Each time a resource is requested using the dictionary notation, a fresh copy of the resource is made.
This also applies if a test function or method requests the same resource multiple times. Thus, if you modify a
resource and need to access the *modified* version of the resource later, save its path in a variable and use that
variable to access the resource later instead of using the dictionary notation multiple times:

.. code:: python

    def test_foo(datadir_copy):
        # This creates the initial fresh copy of data.txt and saves
        # its path in the variable "resource1".
        resource1 = datadir_copy["data.txt"]

        # ...modify resource1 on-disk...

        # You now want to access the modified version of data.txt.

        # WRONG way: This will overwrite your modified version of the
        #            resource with a fresh copy!
        fh = datadir_copy["data.txt"].open("rb")

        # CORRECT way: This will let you access the modified version
        #              of the resource.
        fh = resource1.open("rb")

Version history
---------------

Version 1.1.1
+++++++++++++

- Add a `LICENSE` file (fixes #3).

Version 1.1.0
+++++++++++++

- Allow per-test directories under ``data/`` (thanks, Alexander Lukanin).

Version 1.0.1
+++++++++++++

- Added this `Version history`_ section. :-)
- Fixed bad usage of py.path.local_ objects in code examples.

Version 1.0.0
+++++++++++++

- Initial release


..
    NB: Without a trailing question mark in the following image URL, the
        generated HTML will contain an <object> element instead of an <img>
        element, which apparently cannot be made into a link (i. e. a
        "clickable" image).
.. |pypi-badge| image:: https://img.shields.io/pypi/v/pytest-datadir-ng.svg?
    :align: middle
    :target: https://pypi.python.org/pypi/pytest-datadir-ng

.. _pytest: http://pytest.org/
.. _pytest-datadir plugin: https://github.com/gabrielcnr/pytest-datadir
.. _py.path.local: http://pylib.readthedocs.org/en/latest/path.html
