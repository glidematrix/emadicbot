import os
import argparse
from emadicbot import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()

parser = argparse.ArgumentParser()

parser.add_argument(
    "-p", 
    "--port", 
    default=os.getenv('PORT', 8080), 
    help="Default Port"
)

args = parser.parse_args()

PORT = args.port

def run():

    app.run(
        host="0.0.0.0",
        port=PORT,
        debug=True
    )