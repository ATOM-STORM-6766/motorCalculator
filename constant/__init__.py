import json
# from typing import *

DATA_FOR_MOTORS: dict = json.loads(
    open("./constant/data_for_motors.json").read())

DATA_FOR_MOTORS: dict[str: list[dict[str, str]]]
