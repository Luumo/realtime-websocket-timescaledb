# WebSocket Data Streaming

This is a simple example of data streaming using WebSocket communication. It consists of a producer (`wss-producer.py`) that generates random numbers and sends them to a consumer (`wss-consumer.py`), which inserts the received data into a PostgreSQL database.

## Prerequisites

- Python 3.7 or higher
- PostgreSQL database server (incl. Timescale extension). Read more here: https://docs.timescale.com/self-hosted/latest/

## Setup

1. Clone or download the repository.
2. Install the required Python packages by running the following command:
   ```
   pip install -r requirements.txt
   ```
3. Create a PostgreSQL database and note down the connection details (host, port, database name, username, password).
4. Create a new file named `.env` in the project's root directory and add the following contents, replacing the placeholder values with your PostgreSQL connection details:
   ```
   DB_HOST=<PostgreSQL host>
   DB_PORT=<PostgreSQL port>
   DB_NAME=<PostgreSQL database name>
   DB_USER=<PostgreSQL username>
   DB_PASSWORD=<PostgreSQL password>
   
   SERVER_HOST=localhost
   SERVER_PORT=8765
   SLEEP_DURATION=0.01
   ```
5. Execute the `create.sql` script in your PostgreSQL database to create the required table and indices.

## Usage

1. Start the data producer by running the following command:
   ```
   python wss-producer.py
   ```
   The producer will start generating random numbers and sending them to the WebSocket server.

2. Start the data consumer by running the following command:
   ```
   python wss-consumer.py
   ```
   The consumer will establish a WebSocket connection with the server, receive the random numbers, and insert them into the PostgreSQL database.

3. The consumer will continue running and inserting data into the database until it is manually stopped.

## Customization

- You can modify the `SLEEP_DURATION` value in the `.env` file to control the time interval between each random number generated by the producer.
- The `BATCH_SIZE` constant in `wss-consumer.py` determines the number of events to be inserted into the database in each batch. You can adjust this value based on your requirements.
- If you want to change the database table structure or use a different database system, you will need to modify the `create.sql` script and adapt the code in `wss-consumer.py` accordingly.

**Note**: Make sure to review and update the security measures, such as access controls and encryption, before deploying this system in a production environment.