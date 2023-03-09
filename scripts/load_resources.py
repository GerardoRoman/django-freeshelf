from resources.models import Resource
import csv


def run():
    with open('sample_books.csv') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            # print(row)

            resource = Resource(
                title=row[0], author=row[1], link=row[2], description=row[3])
            resource.save()
