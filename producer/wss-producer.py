import asyncio
import random
import datetime
import websockets
import os
import json
from dotenv import load_dotenv

class RandomNumberGenerator:
    def __init__(self):
        load_dotenv()
        self.event = "random number"
        self.server_host = os.getenv("SERVER_HOST")
        self.server_port = int(os.getenv("SERVER_PORT"))
        self.sleep_duration = float(os.getenv("SLEEP_DURATION"))

    def create_event_json(self, number, time):
        event_data = {
            'event': self.event,
            'number': number,
            'time': time
        }
        json_data = json.dumps(event_data)
        return json_data

    async def generate_random_numbers(self, websocket, path):
        while True:
            # Generate a random number
            random_number = random.randint(1, 100)
            
            time = datetime.datetime.now()

            data = self.create_event_json(random_number, str(time))

            # Send the random number to the client
            await websocket.send(data)

            # Wait for a short period of time before sending the next random number
            await asyncio.sleep(self.sleep_duration)

    def start_server(self):
        # Start the WebSocket server
        start_server = websockets.serve(self.generate_random_numbers, self.server_host, self.server_port)

        # Run the event loop
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    generator = RandomNumberGenerator()
    generator.start_server()