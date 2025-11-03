# API Data Fetcher and MongoDB Storage

This application fetches data from an external API and stores it in a MongoDB database.

## Prerequisites

- Python 3.7+
- MongoDB server running locally or accessible via the connection string
- pip (Python package installer)

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Make sure MongoDB is running locally or update the `MONGODB_URI` in the `.env` file

## Configuration

Edit the `.env` file to configure the application:
- `MONGODB_URI`: MongoDB connection string (default: `mongodb://localhost:27017/`)
- `DB_NAME`: Name of the database to use (default: `api_data_db`)
- `API_BASE_URL`: Base URL of the API to fetch data from (default: `https://jsonplaceholder.typicode.com`)

## Running the Application

1. Activate the virtual environment if not already activated:
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

## How It Works

1. The application connects to the specified MongoDB instance
2. It fetches data from the configured API endpoint
3. The data is then stored in the specified MongoDB collection
4. Existing records with the same ID are updated, new records are inserted


## Testing

Run the test suite with:
```bash
pytest
```

## License

This project is open source and available under the MIT License.
