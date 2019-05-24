Umm al-Qura Calendar
====================

A dataset of Umm al-Qura comparative calendar for Hijri (lunar and solar) and
Gregorian dates.

|data| |license|

.. |data|
   image:: https://goodtables.io/badge/github/datasets/ummalqura-calendar.svg
   :alt: Data Status
   :target: https://goodtables.io/github/datasets/ummalqura-calendar
.. |license|
   image:: https://img.shields.io/github/license/dralshehri/ummalqura-calendar.svg
   :alt: License
   :target: https://github.com/dralshehri/ummalqura-calendar/blob/master/LICENSE

Background
----------

Umm al-Qura calendar is the Hijri lunar calendar officially used in Saudi
Arabia. Although it also has a Hijri solar (zodiacal) calendar that is closely
tied with the Gregorian calendar, it is rarely used.

The lunar calendar is based on astronomical calculations and used mainly by
the governmental sector of the country for civil purposes. Sighting of the
lunar crescent is done at the beginning of each lunar month by an official
supervisory committee set up by the government, however, their adjustments are
meant for religious purposes and are not reflected on the calculated calendar.

Data
----

Data was collected from the following sources which provide comparative tables
between Hijri lunar dates and corresponding Gregorian and Hijri solar dates:

- Umm al-Qura calendar official `website`_.
  (1318-1500 AH).
- Umm al-Qura Comparative Calendar (Arabic: تقويم ام القرى المقارن;
  Taqwīm Umm al-Qurá al-muqāran), 1st edition.
  A printed book published in Arabic language by Saudi government in 1993.
  (1300-1420 AH).
- Umm al-Qura Comparative Calendar (Arabic: تقويم أم القرى المقارن;
  Taqwīm Umm al-Qurá al-muqāran), 2nd edition.
  A printed book published in Arabic language by Saudi government in 2003.
  (1420-1450 AH).

Data from website was verified through the printed books and needed only some
minor fixes for artifacts.

In addition to Hijri and Gregorian comparative dates, `Reduced Julian Days`_
were computed for corresponding gregorian dates using a `published`_ method
implemented in Python language as follows:

.. code-block:: Python

    from datetime import date
    jd = date(2019, 5, 24).toordinal() + 1721425
    rjd = jd - 2400000
    print(rjd)
    # 58628

.. _website: http://www.ummulqura.org.sa/Index.aspx
.. _Reduced Julian Days: https://calendars.wikia.org/wiki/Julian_day_number
.. _published: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.13.9215

Columns
~~~~~~~

``rjd``: Reduced Julian Day, computed as (Julian Day - 2,400,000).

``hy``: Hijri lunar year.

``hm``: Hijri lunar month.

``hd``: Hijri lunar day.

``gy``: Gregorian year.

``gm``: Gregorian month.

``gd``: Gregorian day.

``sy``: Hijri solar year.

``sm``: Hijri solar month.

``sd``: Hijri solar day.

Sample
~~~~~~

=======  ======  ====  ====  ======  ====  ====  ======  ====  ====
  rjd      hy     hm    hd     gy     gm    gd     sy     sm    sd
=======  ======  ====  ====  ======  ====  ====  ======  ====  ====
 58624    1440    9     15    2019    5     20    1397    8     30
 58625    1440    9     16    2019    5     21    1397    8     31
 58626    1440    9     17    2019    5     22    1397    9     1
 58627    1440    9     18    2019    5     23    1397    9     2
 58628    1440    9     19    2019    5     24    1397    9     3
 58629    1440    9     20    2019    5     25    1397    9     4
=======  ======  ====  ====  ======  ====  ====  ======  ====  ====

Contributing
------------

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

Please `report an issue`_ if you have faced one.

.. _report an issue: https://github.com/dralshehri/ummalqura-calendar/issues

License
-------

This data is released into the public domain. See `LICENSE`_ file.

.. _LICENSE: https://github.com/dralshehri/ummalqura-calendar/blob/master/LICENSE
