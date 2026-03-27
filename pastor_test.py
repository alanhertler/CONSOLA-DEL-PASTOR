import asyncio
import websockets
import json

async def pastor():
    async with websockets.connect("ws://localhost:8765") as ws:
        mensaje = {"texto": "Juan 3:16 - Porque de tal manera amó Dios al mundo..."}
        await ws.send(json.dumps(mensaje))
        print("Mensaje enviado")
        await asyncio.sleep(2)

asyncio.run(pastor())