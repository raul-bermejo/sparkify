# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
users_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay (songplay_id varchar, start_time time, user_id int, level varchar, \
                                            song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)""")

users_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int, first_name varchar, last_name varchar, gender varchar, level varchar)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song (song_id varchar, title varchar, artist_id varchar, year int, duration int)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist (artist_id varchar, name varchar, location varchar, latitude float, longitude float)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time time, hour time, day int, week int, month varchar)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay (songplay_id, start_time, user_id, level, \
                                            song_id, artist_id, session_id, location, user_agent) \
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")

users_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) \
                                    VALUES (%s, %s, %s, %s, %s)""")

song_table_insert = ("""INSERT INTO song (song_id, title, artist_id, year, duration) \
                                    VALUES (%s, %s, %s, %s, %s)""")

artist_table_insert = ("""INSERT INTO artist (artist_id, name, location, latitude, longitude) \
                                    VALUES (%s, %s, %s, %s, %s)""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month) \
                                    VALUES (%s, %s, %s, %s, %s)""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, users_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, users_table_drop, song_table_drop, artist_table_drop, time_table_drop]

# TESTING/SANDPIT

if __name__ == "__main__":
    print(song_table_insert)