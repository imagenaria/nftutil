from os.path import isfile, join
from os import listdir, walk
import json
import hashlib
import os
from CONFIG import *


def sha256sum(filename):
    h = hashlib.sha256()
    b = bytearray(128 * 1024)
    mv = memoryview(b)
    with open(filename, "rb", buffering=0) as f:
        for n in iter(lambda: f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()


LICENSE_HASH = sha256sum("license.txt")


def generate_json_from_masterdict():

    masterdict = open_master_dict()

    with open("metadata_template.json", "r") as f:
        data = json.load(f)

    for nft_num in masterdict:

        data["name"] = "Imagenaria #" + nft_num
        data["attributes"][0]["value"] = nft_num

        with open(f"metadata_jsons/{nft_num}.json", "w") as dumpfile:
            json.dump(data, dumpfile)


def open_master_dict():
    with open("master_dict.json", "r") as f:
        data = json.load(f)
    return data


def write_master_dict(masterdict):
    with open("master_dict.json", "w") as f:
        json.dump(masterdict, f)


def init_master_dict_from_dir():

    try:
        os.remove("master_dict.json")
    except:
        pass

    masterdict = {}

    NFT_Files = [f for f in listdir(NFT_DIR) if isfile(join(NFT_DIR, f))]

    for file in NFT_Files:

        masterdict[file.split(".")[0]] = {}

    write_master_dict(masterdict)


def add_metadata_hash_to_master_dict():

    masterdict = open_master_dict()

    for nft_num in masterdict:

        thehash = sha256sum(f"metadata_jsons/{nft_num}.json")
        masterdict[nft_num]["metadata_hash"] = thehash

    write_master_dict(masterdict)


def add_license_hash_to_master_dict():

    masterdict = open_master_dict()

    for nft_num in masterdict:

        masterdict[nft_num]["license_hash"] = LICENSE_HASH

    write_master_dict(masterdict)


def add_image_hash_to_master_dict():

    masterdict = open_master_dict()

    def absoluteFilePaths(directory):
        for dirpath, _, filenames in os.walk(directory):
            for f in filenames:
                yield os.path.abspath(os.path.join(dirpath, f))

    paths = absoluteFilePaths(NFT_DIR)

    for filepath in paths:

        nftnum = filepath.split("/").pop().split(".")[0]
        masterdict[nftnum]["image_hash"] = sha256sum(filepath)

    write_master_dict(masterdict)


def generate_RPC_Jsons():
    masterdict = open_master_dict()

    with open("RPC_JSON_template.json", "r") as f:
        rpc_json = json.load(f)

    for nftnum in masterdict:
        rpc_json["wallet_id"] = WALLET_ID
        rpc_json["uris"] = [ARWEAVE_NFT_MANIFEST_BASE_URL + nftnum + ".jpg"]
        rpc_json["hash"] = masterdict[nftnum]["image_hash"]
        rpc_json["meta_uris"] = [ARWEAVE_METADATA_MANIFEST_BASE_URL + nftnum + ".json"]
        rpc_json["meta_hash"] = masterdict[nftnum]["metadata_hash"]
        rpc_json["license_uris"] = LICENSE_URIS
        rpc_json["license_hash"] = LICENSE_HASH
        rpc_json["royalty_address"] = ROYALTY_ADDRESS
        rpc_json["target_address"] = TARGET_ADDRESS
        rpc_json["royalty_percentage"] = ROYALTY_PERCENTAGE
        rpc_json["fee"] = RPC_FEE

        with open(f"rpc_jsons/{nftnum}.json", "w") as f:
            json.dump(rpc_json, f)


# File names can only have one "." in them. i.e. cat.jpg is good but "cat.old.jpg"
# would end up just being referred to as "cat". This is lazy and I should fix this.

# Need to come up with better way of handling file extension parsing and saving
# -- probably add it to the masterdict i.e. 4 vs 4.jpg in its various uses

init_master_dict_from_dir()
generate_json_from_masterdict()
add_metadata_hash_to_master_dict()
add_license_hash_to_master_dict()
add_image_hash_to_master_dict()
generate_RPC_Jsons()
