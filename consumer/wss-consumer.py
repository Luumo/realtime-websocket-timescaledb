import asyncio
import json
import psycopg2
import websockets
from dotenv import load_dotenv
import os

BATCH_SIZE = 100

class DataConsumer:
    def __init__(self):
        load_dotenv()
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        self.cursor = self.conn.cursor()
        self.events = []

    async def consume_and_insert_data(self):
        async with websockets.connect('ws://localhost:8765') as websocket:
            while True:
                data = await websocket.recv()
                event = json.loads(data)
                self.events.append(event)

                if len(self.events) >= BATCH_SIZE:
                    self.insert_events()
                    self.conn.commit()
                    self.events = []  # Reset events list

    def insert_events(self):
        sql = "INSERT INTO random_no (time, number, event) VALUES (%s, %s, %s)"
        data = [(event['time'], event['number'], event['event']) for event in self.events]
        self.cursor.executemany(sql, data)

    async def main(self):
        await self.consume_and_insert_data()

if __name__ == "__main__":
    consumer = DataConsumer()
    asyncio.run(consumer.main())