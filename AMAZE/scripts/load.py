import csv
import os
from products.models import Products


def run():
    dataset_path = "/home/mitul/_03_ Dev&git/AMAZE-CART/AMAZE/amezon_seller_data"
    Products.objects.all().delete()
    for csv_file in os.listdir(dataset_path):
        file = open(os.path.join(dataset_path, csv_file))
        read_file = csv.reader(file)
        count = 1
        for record in read_file:
            if count == 1:
                pass
            else:
                # print(read_file, record)
                print(count)
                Products.objects.create(
                    name=record[0],
                    main_category=record[1],
                    sub_category=record[2],
                    image=record[3],
                    link=record[4],
                    ratings=record[5],
                    no_of_ratings=record[6],
                    discount_price=record[7],
                    actual_price=record[8],
                )
            count += 1
