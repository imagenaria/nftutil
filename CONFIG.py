# The folder where your nfts are, relative to this file.
NFT_DIR = "nfts"

# The wallet ID of the NFT wallet you create (see README)
WALLET_ID = 6

# Ardrive manifest file for your metadata
ARWEAVE_METADATA_MANIFEST_BASE_URL = "https://bubvlxwexxm6hx4n4uverqxqxguf4agmmbzogon5icqnpi3n4m.arweave.net/DQNV3sS92ePfjeUqSMLwuaheAMx_gcuM5vUCg16Nt48/"

# Ardrive manifest file for your NFT images
ARWEAVE_NFT_MANIFEST_BASE_URL = "https://jnmmsqrtieovefqjjigi2dpj2ysfmt26jqdlg4y6bp3cz7db2rdq.arweave.net/S1jJQjNBHVIWCUoMjQ3p1iRWT15MBrNzHgv2LPxh1Ec/"


# Generate this yourself (see README)
COLLECTION_UUID = "75a3c4c5-9c99-45ac-aea0-d62eec04adad"

# Locations on the net where your license can be found
LICENSE_URIS = [
    "https://6ln4pcwai3ynfb52pkmyldfzyrciijudd7tmdafknb4v7gnply.arweave.net/8tvHisBG8NKHunqZ_hYy5xESEJoMf5sGAqmh5X5mvXk"
]

# An address generated by the parent wallet of your NFT wallet
ROYALTY_ADDRESS = "xch1lkdhwd4eqsq86ftk22lynquc5lxs8ry3tc7mwt7l0fwqe4s3y4gsscf5g6"

# An address generated by the parent wallet of your NFT wallet (can be the same as above, or different)
TARGET_ADDRESS = "xch1lkdhwd4eqsq86ftk22lynquc5lxs8ry3tc7mwt7l0fwqe4s3y4gsscf5g6"

# Royalty expressed in % * 100 (i.e. 5% is 500)
ROYALTY_PERCENTAGE = 500

# Fee for minting your NFT RPC spendbundle (1000 mojos for now seems to be enough)
RPC_FEE = 1000
