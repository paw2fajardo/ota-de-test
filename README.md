# OTA Data Engineering Test

# OTA Data Engineering Test
  **i.**  Project Overview: 
  
The project aims to develop a data processing system that parses Parquet files containing taxi transaction data. These Parquet files are periodically appended to a SQL table, ensuring that the dataset is continuously updated with new information. The primary objective is to analyze the daily total transaction amounts for taxi rides and visualize them through a bar graph.

Key Features:

 1.  Parquet File Parsing: The system will efficiently parse Parquet files containing taxi transaction data, extracting relevant information such as pickup/drop-off locations, timestamps, and fare amounts.
    
 2.  SQL Table Management: The project will implement functionalities to manage the SQL table where the taxi transaction data is stored.
    
 3.  Daily Total Fare Calculation: The system will compute the total fare amount for taxi rides on each day based on the data stored in the SQL table. It will aggregate the fare amounts and organize them by day.
    
 4.  Bar Graph Generation: Using a data visualization library, the project will generate a bar graph illustrating the daily total fare amounts for taxi rides over a specified time period. Each bar on the graph will represent a day, with the height of the bar corresponding to the total amount for that day.

  **ii.**  Setup Instructions: 
 5.  Environment Setup:
    
Ensure you have Python installed on your system. You can download Python from python.org.
Optionally, set up a virtual environment to isolate project dependencies. You can use `virtualenv` or `venv` for this purpose.

 6.  Clone Repository:
    
    -   Clone the project repository from GitHub using the following command:
        `git clone https://github.com/paw2fajardo/ota-de-test.git` 
        
    -   Navigate to the project directory:
        `cd ota-de-test` 
        
 7.  Install Dependencies:    
Install the required Python dependencies by running:
`pip install -r requirements.txt` 
        
 8.  Database Setup:
    -   Ensure you have a SQL database server installed (e.g., MySQL, PostgreSQL, SQLite).
    -   Create a new database for this project if one doesn't already exist.
    -   Update the database connection settings in the project configuration file (`config.py`) to reflect your database credentials and settings.
 9.  Parquet File Configuration:
    -   Ensure you have Parquet files containing taxi transaction data.
    -   Update the file paths or configurations in the project settings (`config.py`) to point to the directory or location where your Parquet files are stored.
 10.  Run the Application:
    -   Start the application by executing the main script:
        `python main.py` 
        

  **iii.**  Execution Instructions:
Start the application by executing the main script:
`python main.py` 

  **iv.**  Discussion: Insights into your problem-solving process, challenges faced, and how you overcame them. Mention any assumptions made during the development.


1.  Parsing Parquet Files: Employed the `read_parquet` function from the `pandas` library for efficient extraction of data from Parquet files.
    
2.  Filtering Data: Utilized DataFrame operations after parsing to easily filter and manipulate the data as needed.
    
3.  Database Creation: Established a local database using SQLite to persist the extracted data for further analysis and retrieval.
    
4.  Preventing Duplicate Entries: Implemented a safeguard against duplicate records by utilizing the `if_exists='replace'` parameter within the `df.to_sql` function, ensuring that existing records are updated rather than duplicated.
    
5.  Visualization Creation: Employed Matplotlib to generate a visually informative bar graph illustrating the total amount summed per day.
    

Assumptions:

1.  Data Extraction Source: Assumes users will acquire the data from a website or external source.
2.  Analysis Requirement: Assumes users will need insights into the daily total amount, prompting the need for visualization.
