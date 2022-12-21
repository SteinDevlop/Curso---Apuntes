import logging as log
def mensajes():
    log.debug("Mensaje debug")
    log.info("Mensaje info")
    log.warning("Mensaje warning")
    log.critical("Mensaje critical")
print("---------------------")
log.basicConfig(level=log.DEBUG,
format="%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
datefmt="%I:%M:%S %p",
handlers=[
    log.FileHandler("Capa_datos.log"),
    log.StreamHandler()
    ])


