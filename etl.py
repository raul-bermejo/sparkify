import os
import glob
import psycopg2
import pandas as pd
import numpy as np
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Executes INSERT SQL to populate song and artist tables in PostgreSQL.
    from data song_data files which are converted into pd.Dataframes
    
    Parameters:
    ----------
    cur: psycopg2.connect.cursor() object
         Cursor that enables PostreSQL command execution
    filepath: str
              Contains absolute path to datafile so it can be read as pandas.DataFrame           

    Returns: 
    ----------
    None: Only SQL commands are exectuted
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[["artist_id", "artist_name", "artist_location", 'artist_latitude', 'artist_longitude']].values[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Executes INSERT SQL to populate time and user tables in PostgreSQL 
    from data log_data files which are converted into pd.Dataframes.
    
    Parameters:
    ----------
    cur: psycopg2.connect.cursor() object
         Cursor that enables PostreSQL command execution
    filepath: str
              Contains absolute path to datafile so it can be read as pandas.DataFrame           

    Returns: 
    ----------
    None: Only SQL commands are exectuted
    """
    
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    is_NextSong = df["page"] == "NextSong"           # define mask as variable
    df = df[is_NextSong]

    # convert timestamp column to datetime
    t = pd.to_datetime(df["ts"], unit="ms")
    
    # insert time data records
    # turn the time_data collection of pd.Series to transform and transpose
    # to get row by row data (saves having to build a dictionary) 
    time_data = np.array([df["ts"].values, t.dt.hour, t.dt.day, t.dt.isocalendar().week, t.dt.month, t.dt.year, t.dt.weekday]).T
    column_labels = ("UNIX Timestamp", "Hour", "Day", "Week of Year", "Month", "Year", "Weekday") 
    time_df = pd.DataFrame(time_data, columns=column_labels)


    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(users_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, 
                            row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    ETLs all data by iterating through all song_- 
    and log_data files and then calling 
    appropiate processing function. 
    
    Executes INSERT SQL to populate time and user tables in PostgreSQL 
    from data log_data files which are converted into pd.Dataframes.
    
    Parameters:
    ----------
    cur: psycopg2.connect.cursor() object
         Cursor that enables PostreSQL command execution into database
    conn: psycopg2.connect() object
          Enables PostreSQL connection with database  
    filepath: str
              Contains absolute path to datafile so it can be read as pandas.DataFrame         
    func: function 
          Processing function to populate either log or song data. Must be either 
          process_song_file() process_log_file() functions.

    Returns: 
    ----------
    None: Data is ETLed without nothing being returned. Databases are populated
    
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
