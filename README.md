# sparkify

This project is intended to analyze data for a hypothetical start-up called Sparkify. This music streaming start-up wants to analyze their song- and log-related data in a more efficient way.

More specifically, the goal of this project is to build a PostgreSQL database and establish an ETL process to optimize the querying of their (JSON) song- and log-related data. This in turn will facilitate the analysis of their data.

## Database schema

The implemented database schema can be seen in the ER diagram below

![alt text](https://github.com/raul-bermejo/sparkify/blob/main/images/sparkify_erd.png)

The Entity Relationshiip Diagram (ERD) above is a Star Schema where the facts (or metrics) are represented by the songplays relation. The reason for this is to have the analysis of log and song data at the heart of the business. From the songplays relation one can observe the dimension of the sparkify business: users, artists, songs and time. Each of these relations represents a core business aspect of sparkify.

## ETL pipeline

In order to pipe sparkify's JSON data to the PostgreSQL database an ETL process was establish from the data source. The schema shown above was implemented by the use and filtering of pandas.DataFrame objects, combine with the use of a series of INSERT and SELECT SQL statements, once the relations had been created. 

## Dependencies

The following libraries need to be installed for the code to work: numpy, pandas and psycopg2.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install any of these libraries if needed.

```bash
pip install numpy
pip install pandas
pip install psycopg2
```

## Authors

The author of this repo is me, Raul Bermejo, as part of the Data Engineer program at Udacity.

## Usage

So far the usage of this project is minimal, and therefore there are no examples. This section will be updated when enough progress has been made.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
