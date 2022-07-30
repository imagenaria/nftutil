import os
import time
from subprocess import run

from datetime import datetime


# abspaths
CHIA_DIR = "/ABS/PATH/TO/chia-blockchain"
RPC_JSONS_DIR = "/ABS/PATH/TO/JSONS/DIR"

for filename in os.listdir(RPC_JSONS_DIR):
    filepath = os.path.join(f"{RPC_JSONS_DIR}/{filename}")

    print(filepath)

    mint_command = f"chia rpc wallet nft_mint_nft -j {filepath}"

    print(mint_command)

    run(
        f"cd {CHIA_DIR} && . ./activate && {mint_command}", shell=True,
    )

    now = datetime.now()

    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    print("\n\n\n")
    print(f"sleeping for 40 seconds at {current_time}")
    time.sleep(40)
