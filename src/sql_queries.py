# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
users_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay ( \
                                songplay_id SERIAL PRIMARY KEY NOT NULL, \
                                start_time bigint NOT NULL, \
                                user_id int NOT NULL, \
                                level varchar NOT NULL, \
                                song_id varchar NOT NULL,  \
                                rtist_id varchar NOT NULL,  \
                                ession_id int NOT NULL, \
                                location varchar NOT NULL, \
                                user_agent varchar NOT NULL)""")

users_table_create = ("""CREATE TABLE IF NOT EXISTS users ( \
                                user_id int NOT NULL,  \
                                first_name varchar NOT NULL, \
                                last_name varchar NOT NULL, \
                                gender varchar NOT NULL, \
                                level varchar NOT NULL, \
                                PRIMARY KEY user_id)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song ( \
                            song_id varchar NOT NULL, \
                            title varchar NOT NULL, \
                            artist_id varchar NOT NULL, \
                            year int NOT NULL, \
                            duration int NOT NULL, \
                            PRIMARY KEY song_id)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist ( \
                                artist_id varchar NOT NULL, \
                                name varchar NOT NULL, \
                                location varchar NOT NULL, \
                                latitude float NOT NULL, \
                                longitude float NOT NULL, \
                                PRIMARY KEY artist_id)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time ( \
                                start_time bigint NOT NULL, \
                                hour int NOT NULL, \
                                day int NOT NULL, \
                                week int NOT NULL, \
                                month int NOT NULL, \
                                year int NOT NULL, \
                                weekday int NOT NULL, \
                                PRIMARY KEY start_time)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay (start_time, user_id, level, \
                                            song_id, artist_id, session_id, location, user_agent) \
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")

users_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) \
                                    VALUES (%s, %s, %s, %s, %s) \ 
                                    ON CONFLICT level DO NOTHING""")

song_table_insert = ("""INSERT INTO song (song_id, title, artist_id, year, duration) \
                                    VALUES (%s, %s, %s, %s, %s)""")

artist_table_insert = ("""INSERT INTO artist (artist_id, name, location, latitude, longitude) \
                                    VALUES (%s, %s, %s, %s, %s)""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
                                    VALUES (%s, %s, %s, %s, %s, %s, %s)""")

# FIND SONGS

song_select = ("""SELECT song_id, artist.artist_id \
                FROM song INNER JOIN artist ON song.artist_id = artist.artist_id \
                 WHERE title = %s AND name = %s AND duration = %s""")

# QUERY LISTS
create_table_queries = [songplay_table_create, users_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, users_table_drop, song_table_drop, artist_table_drop, time_table_drop]

# TESTING/SANDPIT

if __name__ == "__main__":
    print(song_select)
