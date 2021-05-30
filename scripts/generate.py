import csv
from datetime import date, timedelta
from hijri_converter.convert import Gregorian
from hijri_converter.ummalqura import GREGORIAN_RANGE


def generate_calendar(filename):
    start, end = GREGORIAN_RANGE
    start_date = date(*start)
    end_date = date(*end)

    with open(filename, mode='w') as file:
        calendar_writer = csv.writer(file)
        calendar_writer.writerow(["rjd", "hy", "hm", "hd", "gy", "gm", "gd"])
        row_date = start_date
        while row_date <= end_date:
            gy, gm, gd = row_date.timetuple()[:3]
            hy, hm, hd = Gregorian(gy, gm, gd).to_hijri().datetuple()
            rjd = row_date.toordinal() + 1721425 - 2400000
            calendar_writer.writerow([rjd, hy, hm, hd, gy, gm, gd])
            row_date += timedelta(days=1)


if __name__ == '__main__':
    generate_calendar("../data/ummalqura-calendar.csv")
