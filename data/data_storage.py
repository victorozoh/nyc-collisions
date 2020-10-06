#! /usr/bin/env python
import psycopg2
import os

# get postgres database URI
DATABASE_URL = os.environ.get('DATABASE_URL')
connection = psycopg2.connect(DATABASE_URL)


def create_database():
    """
    This function is responsible for creating a database Table
    in a Heroku PostGRESQL database
    """
    # create Motor Vehicles Collision database
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                DROP TABLE IF EXISTS collisions;
                CREATE TABLE collisions(
                    crash_date date,
                    crash_time text,
                    borough text,
                    zip_code text,
                    latitude real,
                    longitude real,
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
                    collision_id integer
            );
            """)
    print('database successfully created!')

def load_database():
    """
    This function takes the cleaned csv file and copies it
    to the database table
    """
    # copy data from csv file to database
    with connection:
        with connection.cursor() as cursor:
            with open('cleaned_collisions.csv', 'r') as f:
                next(f) # Skip the header row.
                cursor.copy_from(f, 'collisions', sep=',')
    print("data upload complete!")

if __name__ == "__main__":
    create_database()
    load_database()
