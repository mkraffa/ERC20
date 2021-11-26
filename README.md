# ERC20
Pull ERC20 Wallet content

Simple pull of ERC20 compatible wallet content.
ERC20 contracts to be looked for have to be specified (except for ETH, see examples)

## before getting started:
1. update the CSV file:
  i.  update the public addresses (pub) you are looking to track
  ii. change the headers if looking for different tokens

2. update the python script
  i. get a valid Etherscan API Key from https://etherscan.io/apis and paste it in the API variable
  ii. update the ERC20 contract address where needed
  iii. make sure the csv. headers match the iloc in the script.

NB. I'm well aware this isn't the best way of doing this, but it works... comments and edits are welcome :)
