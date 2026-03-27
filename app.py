import asyncio
import websockets
import json

clientes = set()

async def manejar_conexion(websocket):
    clientes.add(websocket)
    print(f"Fiel conectado. Total: {len(clientes)}")
    try:
        async for mensaje in websocket:
            datos = json.loads(mensaje)
            print(f"Pastor envió: {datos}")
            for cliente in clientes.copy():
                if cliente != websocket:
                    await cliente.send(mensaje)
    finally:
        clientes.remove(websocket)
        print(f"Fiel desconectado. Total: {len(clientes)}")

async def main():
    print("Servidor iniciado en puerto 8765")
    async with websockets.serve(manejar_conexion, "0.0.0.0", 8765):
        await asyncio.Future()

asyncio.run(main())