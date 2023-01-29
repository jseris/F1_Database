<h1>Introduction<h1>
<body>Hello, welcome to my relational database architecture project. For this project, I focused on taking CSV files consisting of Formula One data and creating a MySQL database using Python. There was plenty to consider while working on this project, which I will highlight below<body>

<h1>Considerations<h1>
<body>First and foremost, I accessed this data via Kaggle.com (citation at the bottom). An immediate concern is the missing data in several tables. There are several blank columns and missing data here and there. I very well could have filled out the missing data, but this was not the goal of my project. Furthermore, it would have been a tedious process detracting from my main goal. Another point of discussion is the format of the race times (pitstop length, lap times, etc.). The format for these columns was not friendly with Python data types. Though I would have preferred a simple way to be able to perform mathematical functions on these numbers, it is not easily possible. Therefore, I opted to treat them as strings. That way, I could perform other tasks easier such as joining lap times and lap time milliseconds together.<body>

<h1>What You Need To Know<h1>
<body>This project uses MySQL to construct the database. In order to use the code, you will need to create a text file named "MySQLMellon.txt" in the same directory as the Python files with the following information listed accordingly: MySQL username, MySQL password, host name. The program will pull the directory in which these files reside via os.path.abspath().

The file names should be self-explanatory to run in order. Be sure to create the database, create tables, fill the tables, and lastly run some simple queries that I composed.<body>
