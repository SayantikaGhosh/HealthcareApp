import pandas as pd
from base.models import Food
from django.core.management import BaseCommand



ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    
    def handle(self, *args, **options):

        if Food.objects.exists():
            print('Food data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        df=pd.read_csv(r'C:\Users\SAYANTIKA GHOSH\OneDrive\Desktop\HealthcareApp\backend\Test.csv')
        row_iter = df.iterrows()

        objs = [

            Food(

                foodname = row['foodname'], # Adjust field names as per your CSV structure
                calories = row['calories'],
                fat = row['fat'],
                carbs = row['carbs'],
                protein = row['protein'],
                fibres = row['fibres'],
            )

            for index, row in row_iter

        ]
        Food.objects.bulk_create(objs)









# import pandas as pd
# from base.models import Food   # If you defined a model

# def import_data_from_csv(csv_file):
#     df = pd.read_csv(csv_file)  # Read the CSV file into a Pandas DataFrame
    
#     for index, row in df.iterrows():
#         foodname = row['foodname']  # Adjust field names as per your CSV structure
#         calories = row['calories']
#         fat = row['fat']
#         carbs = row['carbs']
#         protein = row['protein']
#         fibres = row['fibres']
        
#         Food.objects.create(foodname=foodname, calories=calories, fat=fat, carbs=carbs, protein=protein,fibres=fibres)  # If you defined a model






# from csv import DictReader
# from django.core.management import BaseCommand
# from base.models import Food 


# ALREDY_LOADED_ERROR_MESSAGE = """
# If you need to reload the child data from the CSV file,
# first delete the db.sqlite3 file to destroy the database.
# Then, run `python manage.py migrate` for a new empty
# database with tables"""


# class Command(BaseCommand):
#     # Show this when the user types help
#     help = "Loads data from Test.csv"

#     def handle(self, *args, **options):
    
#         # Show this if the data already exist in the database
#         if Food.objects.exists():
#             print('Food data already loaded...exiting.')
#             print(ALREDY_LOADED_ERROR_MESSAGE)
#             return
            
#         # Show this before loading the data into the database
#         print("Loading food data")


#         #Code to load the data into database
#         for row in DictReader(open('./Test.csv')):
#             food=Food(foodname=row['foodname'], calories=row['calories'], fat=row['fat'],carbs=row['carbs'],protein=['protein'],fibres=row['fibres'])  
#             food.save()