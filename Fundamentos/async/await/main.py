import asyncio

async def antender_usuario(nombre, tiempo_de_espera):
    print(f"Empiezo a atender a {nombre}")
    await asyncio.sleep(tiempo_de_espera)
    print(f"termine de atender a {nombre}, y tarde {tiempo_de_espera} segundo/s")

async def main():

    antender_usuario("Juan", 1),
    antender_usuario("Ana", 1),


asyncio.run(main())