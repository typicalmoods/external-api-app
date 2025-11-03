# API Data Fetcher and MongoDB Storage

This application fetches data from an external API and stores it in a MongoDB database. It can be run either locally or using Docker.

## Prerequisites

### For Local Development
- Python 3.7+
- MongoDB server running locally or accessible via the connection string
- pip (Python package installer)

### For Docker
- Docker
- Docker Compose

## Setup

### Option 1: Local Development

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

### Option 2: Docker

1. Clone this repository
2. The application is ready to run with Docker Compose

## Configuration

Edit the `.env` file to configure the application:

```env
MONGODB_URI=mongodb://mongo:27017/  # Use 'mongo' as host when using Docker
DB_NAME=api_data_db
API_BASE_URL=https://jsonplaceholder.typicode.com
```

## Running the Application

### Local Development

1. Activate the virtual environment if not already activated:
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

### Using Docker

1. Build and start the application with Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. To run in detached mode:
   ```bash
   docker-compose up -d
   ```

3. To view logs:
   ```bash
   docker-compose logs -f
   ```

4. To stop the application:
   ```bash
   docker-compose down
   ```

## How It Works

1. The application connects to the specified MongoDB instance
2. It fetches data from the configured API endpoint (JSONPlaceholder by default)
3. The data is then stored in the specified MongoDB collection
4. Existing records with the same ID are updated, new records are inserted

## Project Structure

- `main.py` - Main application entry point
- `api_client.py` - Handles API requests
- `database.py` - Manages MongoDB connection
- `config.py` - Application configuration
- `Dockerfile` - Docker configuration for the application
- `docker-compose.yml` - Defines multi-container Docker application
- `.env` - Environment variables

## Testing

Run the test suite with:
```bash
pytest
```

## License

This project is open source and available under the MIT License.
