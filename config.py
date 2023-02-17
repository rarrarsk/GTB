import os
class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6071270764:AAGuFvc_gPEaWCZP-e15mqneU8md8gGhSV0")

    API_ID = int(os.environ.get("API_ID", 8233223))

    API_HASH = os.environ.get("API_HASH", "dacf95e444cf26fb3d7e9b997e3ee456")

    DATABASE = os.environ.get("DATABASE", "mongodb+srv://urluploader005bot:urluploader005bot@cluster0.ylujx.mongodb.net/?retryWrites=true&w=majority")

    DEV_NAME = os.environ.get("DEV_NAME", "SK_ROCKIG_WORLD")

    DEV_ID = set(int(x) for x in os.environ.get("DEV_ID", "1285768957").split())
