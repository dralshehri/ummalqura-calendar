Umm al-Qura Comparative Calendar
================================

A dataset of Umm al-Qura comparative calendar including Hijri and Gregorian
dates for the years 1300-1500 AH.

|data| |license|

.. |data|
   image:: https://goodtables.io/badge/github/dralshehri/ummalqura-calendar.svg
   :alt: Data Status
   :target: https://goodtables.io/github/dralshehri/ummalqura-calendar
.. |license|
   image:: https://img.shields.io/badge/License-PDDL-brightgreen.svg
   :alt: License
   :target: https://opendatacommons.org/licenses/pddl/

Background
----------

The Umm al-Qura calendar is the lunar Hijri calendar officially adopted by
Saudi Arabia for administrative purposes since 1343 AH (1925 CE). It is widely
used in Saudi Arabia, especially by the governmental sector. However, the
Gregorian calendar is also used, mainly by the private sector.

Data
----

Data was generated using `Hijri Converter`_ Python package to provide accurate
comparative tables for Hijri and Gregorian dates for the years 1343-1500 AH.
In addition, `Reduced Julian Days`_ were computed for corresponding gregorian
dates using a `published`_ method already implemented in `Hijri Converter`_
package.

.. _Hijri Converter: https://pypi.org/project/hijri-converter/
.. _Reduced Julian Days: https://calendars.wikia.org/wiki/Julian_day_number
.. _published: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.13.9215

Columns
~~~~~~~

:``rjd``: Reduced Julian Day.
:``hy``: Hijri year.
:``hm``: Hijri month.
:``hd``: Hijri day.
:``gy``: Gregorian year.
:``gm``: Gregorian month.
:``gd``: Gregorian day.

Sample
~~~~~~

=======  ======  ====  ====  ======  ====  ====
  rjd      hy     hm    hd     gy     gm    gd
=======  ======  ====  ====  ======  ====  ====
 58608    1440    8     29    2019    5     4
 58609    1440    8     30    2019    5     5
 58610    1440    9     1     2019    5     6
 58611    1440    9     2     2019    5     7
 58612    1440    9     3     2019    5     8
 58613    1440    9     4     2019    5     9
=======  ======  ====  ====  ======  ====  ====

Preparation
-----------

You will need Python 3.6 or greater and `Hijri Converter`_ package to generate
the dataset. Follow these steps:

1. Create and activate a virtual environment:
   ::

       python3 -m venv env
       source env/bin/activate

2. Install the dependency package:
   ::

       pip install hijri-converter

3. Run the script to generate the dataset:
   ::

       python scripts/generate.py

Contributing
------------

Contributions are welcome, and they are greatly appreciated!
Please `report an issue`_ if you have any comment, question, or request.

.. _report an issue: https://github.com/dralshehri/ummalqura-calendar/issues

License
-------

This dataset is made available under the Public Domain Dedication and License
v1.0 whose full text can be found at:

http://www.opendatacommons.org/licenses/pddl/1.0/

Change Log
----------

**2.0.0**

- Instead of using tables of the Umm al-Qura calendar website, data was
  generated using `Hijri Converter`_ Python package for more accurate dates.
- Added Python code used to generate data.
- Removed solar Hijri dates as they are rarely used.
- Renamed dataset file.
- Updated README content.

**1.0.0**

- First release.
