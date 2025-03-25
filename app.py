import asyncio
import websockets

clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    print(f"New client connected. Total connections: {len(clients)}")

    try:
        async for message in websocket:
            for client in clients:
                if client != websocket:
                    await client.send(message)
    except websockets.ConnectionClosed:
        print("Client disconnected")
    finally:
        clients.remove(websocket)
        print(f"Client removed. Active connections: {len(clients)}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 3000):
        print("WebSocket server running on ws://0.0.0.0:3000")
        await asyncio.Future()  # Keeps the server running

asyncio.run(main())