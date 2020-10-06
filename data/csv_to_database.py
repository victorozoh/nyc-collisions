#! /usr/bin/env python
import psycopg2
import os

# get postgres database URI
DATABASE_URL = os.environ.get('DATABASE_URL')
connection = psycopg2.connect(DATABASE_URL)


def create_database():
    # create Motor Vehicles Collision database
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                DROP TABLE IF EXISTS collisions;
                CREATE TABLE collisions(
                    id integer PRIMARY KEY,
                    crash_date date,
                    crash_time text,
                    borough text,
                    zipcode text,
                    latitude real,
                    longitude real,
                    location point,
                    on_street_name text,
                    cross_street_name text,
                    off_street_name text,
                    num_persons_injured integer,
                    num_persons_killed integer,
                    num_pedestrians_injured integer,
                    num_pedestrians_killed integer,
                    num_cyclist_injured integer,
                    num_cyclist_killed integer,
                    num_motorist_injured integer,
                    num_motorist_killed integer,
                    contributing_factor_vehicle_1 text,
                    contributing_factor_vehicle_2 text,
                    contributing_factor_vehicle_3 text,
                    contributing_factor_vehicle_4 text,
                    contributing_factor_vehicle_5 text,
                    collision_id integer,
                    vehicle_type_code_1 text,
                    vehicle_type_code_2 text,
                    vehicle_type_code_3 text,
                    vehicle_type_code_4 text,
                    vehicle_type_code_5 text
            );
            """)
    print('database successfully created!')

def copy_csv_to_database():
    # copy data from csv file to database
    with connection:
        with connection.cursor() as cursor:
            with open('collisions.csv', 'r') as f:
                next(f) # Skip the header row.
                cursor.copy_from(f, 'collisions', sep=',')

if __name__ == "__main__":
    create_database()
    #copy_csv_to_database()
