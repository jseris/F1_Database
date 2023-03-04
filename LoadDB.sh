#!/bin/bash

python3 Create_F1_DB.py
python3 Create_Tables.py
python3 MySQL_FillTables.py
python3 MySQL_Queries.py
