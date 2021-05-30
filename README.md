# Umm al-Qura Comparative Calendar

A dataset of Umm al-Qura comparative calendar including the Hijri years 1343-1500 AH.

## Background

The Umm al-Qura calendar is the lunar Hijri calendar officially adopted by
Saudi Arabia for administrative purposes. It was originated from Umm al-Qura
newspaper, the official newspaper of government of Saudi Arabia. The newspaper
is published weekly and its first issue was on Friday, 15 Jumada al-Ula 1343 AH
(12 December 1924 CE). However, the calendar has been printed and distributed
separately by the Saudi government since 1346 AH (1927 CE).

The calendar is widely used in Saudi Arabia, especially by the public
sector. Official documents, political letters, health care records, and
education certificates, are just examples of many other documents that are
dated by the Hijri calendar.

However, the Gregorian calendar is the calendar used in most of the world,
and it has been implemented as the default calendar in nearly every computer
and database.

## Data

Data was generated using the [Hijri Converter] Python package to provide an
accurate comparative table for Hijri and Gregorian dates for the period from the
beginning of 1343 AH (1 August 1924 CE) to the end of 1500 AH (16 November 2077 CE).
Additionally, [Reduced Julian Day] numbers were computed assuming noon time for
corresponding Gregorian dates using a [published] formula that is already implemented
in the [Hijri Converter] package.

### Columns

`rjd`: Reduced Julian Day number.  
`hy`: Hijri year.  
`hm`: Hijri month.  
`hd`: Hijri day.  
`gy`: Gregorian year.  
`gm`: Gregorian month.  
`gd`: Gregorian day.  

### Sample

|  rjd  |  hy  |  hm  |  hd  |  gy  |  gm  |  gd  |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- |
| 58608 | 1440 |   8  |  29  | 2019 |   5  |   4  |
| 58609 | 1440 |   8  |  30  | 2019 |   5  |   5  |
| 58610 | 1440 |   9  |   1  | 2019 |   5  |   6  |
| 58611 | 1440 |   9  |   2  | 2019 |   5  |   7  |
| 58612 | 1440 |   9  |   3  | 2019 |   5  |   8  |
| 58613 | 1440 |   9  |   4  | 2019 |   5  |   9  |

### Preparation

You will need Python 3.6 or greater and [Hijri Converter] package to generate
the dataset.

1. Install the package:

```shell
pip install -U hijri-converter
```

2. Run the script to generate the dataset:

```shell
python scripts/generate.py
```

## Contributing

Contributions are welcome, and they are greatly appreciated!

Please [report an issue] if you have any comment, question, or request.

## License

This dataset is licensed under the Creative Commons Zero v1.0 Universal. See [LICENSE].

[Hijri Converter]: https://pypi.org/project/hijri-converter/
[Reduced Julian Day]: https://calendars.wikia.org/wiki/Julian_day_number
[published]: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.13.9215
[report an issue]: https://github.com/dralshehri/ummalqura-calendar/issues/new
[LICENSE]: https://github.com/dralshehri/ummalqura-calendar/blob/main/LICENSE
