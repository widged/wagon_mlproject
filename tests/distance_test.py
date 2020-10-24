# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.distance import haversine
import pytest


def test_clean_data():
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 49.865070, 2.480009
    distance = haversine(lon1, lat1, lon2, lat2)
    assert distance == 111.43044100970154
