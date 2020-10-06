import psycopg2

# get postgres database URI
POSTGRESQL_URI = 'postgres://nzhueovukglghy:7bee70d2b91537932a3277fc1d524c90d2e88c5cff790f441b74d217e54dfe01@ec2-100-25-100-81.compute-1.amazonaws.com:5432/da04g219jcspip'
connection = psycopg2.connect(POSTGRESQL_URI)


def main():
    # create Motor Vehicles Collision database
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE collisions(
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

    # copy data from csv file to database
    with connection:
        with connection.cursor() as cursor:
            with open('collisions.csv', 'r') as f:
                next(f) # Skip the header row.
                cur.copy_from(f, 'collisions', sep=',')

if __name__ == "__main__":
    main()
