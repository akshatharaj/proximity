# Proximity

Proxitmity is a python application that maintains a listing of homes for sale, and, accepts a listing/home and returns similar listings nearby.

Currently, the app searches for all listings that are in neighboring zip codes and are nearly the same size (~same number of bathrooms/bedrooms)

This could perhaps be improved to look for same/similar dwelling type etc.


## Installation

### Clone the repository

    $ cd ~/Code
    $ git clone git@github.com:username/proximity.git

### Make a new virtual environment

    $ virtualenv --no-site-packages --distribute ~/Code/env
    $ cd ~/Code/env
    $ . bin/activate
    $ pip install -U distribute

### Install all its dependencies

    $ cd ~/Code/proximity
    $ pip install requirements.txt

### Configure database connection settings

    edit db_connection.py 

### Then run (Please edit recomment_listings to customize home input)

    $ python load_data.py
    $ python recommend_listings.py