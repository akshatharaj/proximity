# Careermate

Proxitmity is a python application that maintains a listing of homes for sale, and, accepts a listing/home and returns similar listings nearby.

Currently, the app looks searches for all listings that are in neighboring zip codes and are nearly the same size (~same number of bathrooms/bedrooms)

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

### Install careermate and all its dependencies

    $ cd ~/Code/proximity
    $ pip install requirements.txt

### Then run (Please edit recomment_listings to customize hoome input)

    $ python load_data.py
    $ python recommend_listings.py