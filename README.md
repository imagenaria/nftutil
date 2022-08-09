# CHIA NFTUtil

## Intro

This repository contains a collection of utlities that help mint a large NFT collection on Chia that would be cumbersome to do individually.

At the moment, it only generates the metadata, hashes, and RPC files that you need to mint NFTs, and has a utility that mints them one by one. Right now, it takes 40 seconds to mint an NFT using minter.py, but this should be possible to speed up dramatically soon.

You still need to:

-   Upload your NFTs to Ardrive (This will probably work with IPFS or custom domains, but I haven't made sure yet, so not supported at present)
-   Upload your metadata to Ardrive
-   Generate manifests for your images and metadata on ardrive

I recommend you read through these two guides before running this tool, to get familiarity with what is going on here:

- https://devs.chia.net/guides/nft-intro/
- https://github.com/scrutinously/chia-scripts/wiki/Chia-NFTs

NOTE: 
The minter.py script, in my experience, starts to hang up and fail if you don't have enough spendable coins in your wallet. I was able to get around this by doing some manual coin splitting (just sending 2000 mojo transactions back to the wallet). I've also had to go and delete_unconfirmed_transactions a few times in order to continue minting. I also have had issues running other wallet commands during the minting, FYI

## Steps:

Note: Right now, all your images have to be jpg files and end with ".jpg". I will update this tool to respect the actual file extensions of the nft images, but for now please take note of this.

Note: Currently, the only way to specify which "number" an NFT is as part of a collection is just by naming it or giving it an attribute. e.g., NFTname #1, NFTname #2, ...
Note: Collections "exist" only as aggregates of individual NFTS that report the same collection UUID

1. Upload all your NFTs to [ardrive](https://ardrive.io/), generate a manifest url in the drive you uploaded them to, and add that to CONFIG.py
2. Put all your NFT images in the directory nfts/
3. Put the contents of your license in license.txt
4. Generate an NFT wallet and get the wallet # from the CLI, add to CONFIG.py
5. Genrate a UUID for the collection (follow guide at https://github.com/scrutinously/chia-scripts/wiki/Chia-NFTs#generate-a-uuid) and add to CONFIG.py
6. Edit metadata_template.json for your project, adding values for all fields
7. Run generate.py
8. Upload all the metadata json files to ardrive, and generate a manifest, and add that manifest to CONFIG.py
9. Re-run CONFIG.py (now that you have the manifest for the metadata)
10. Review some of the RPC JSON files that were created, and make sure that they look good. Check to see that the URIs work and that the hashes are correct
11. Run the minter.py with a couple RPC's in the rpc folder to make sure it is working properly
12. Run the minter.py with all the RPCs in the RPC folder.

## To add

-   Implement Ardrive API to handle uploading Images, metadata, and generating manifests.
-   Handle file extensions properly (don't just assume ".jpg")
-   Speed up NFT minting via spendbundles
-   Improve minting script to poll blockchain for successfully minted NFTs, rather than waiting 40s between mints.

Please feel free to reach out to me on Keybase [@magnoolia](https://keybase.io/magnoolia), or by email: imagenaria@proton.me or twitter: [@imagenariaNFT](https://twitter.com/imagenariaNFT)
