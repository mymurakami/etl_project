# Simple ETL Pipeline Project

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python. The pipeline fetches data from a public API, processes it, and stores it in a local SQLite database.

## Project Structure

- `scripts/extract.py`: Extracts data from a public API.
- `scripts/transform.py`: Transforms the extracted data.
- `scripts/load.py`: Loads the transformed data into a SQLite database.
- `data/`: Contains the raw data, transformed data, and the SQLite database.
- `requirements.txt`: Lists the Python dependencies.

## Setup and Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/data_pipeline_project.git
   cd data_pipeline_project
