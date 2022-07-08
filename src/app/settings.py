from os import getenv


ENV = getenv("BE_MODE", "DEV")

BE_HOST = getenv("BE_HOST", "0.0.0.0")
BE_PORT = int(getenv("BE_PORT", 5005))

MONGO_HOST = getenv("BE_MONGO_HOST", "localhost")
MONGO_PORT = int(getenv("BE_MONGO_PORT", 0)) or 27017
MONGO_USER = getenv("BE_MONGO_USER", "root")
MONGO_PASSWORD = getenv("BE_MONGO_PASSWORD", "pass12345")
