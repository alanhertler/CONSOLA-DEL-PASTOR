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

import streamlit as st

st.set_page_config(page_title="CONSOLA DEL PASTOR")

st.title("CONSOLA DEL PASTOR")
st.warning("La versión con WebSocket no funciona en Streamlit Cloud.")
st.info("Hay que convertir esta consola a lógica interna de Streamlit.")

asyncio.run(main())
