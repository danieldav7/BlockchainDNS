import time
from web3 import Web3, HTTPProvider
import json

contract_address   = "0x5054f6D117E71a374F4C2b5Cd8508fA578aF439D"
wallet_private_key = "d5e56c6fbb9441cc7c3e996ed1c5d785d96b665482c7f34e08e11249ad2a36ce"
wallet_address     = "0xBAb3632832DAdD4338dbB17227521b13FeD38c76"
url = "http://192.168.56.102:7545"

w3 = Web3(HTTPProvider(url))
w3.eth.defaultAccount = w3.eth.accounts[0]

abi = json.loads('''[{"constant":false,"inputs":[{"name":"newAddress","type":"string"}],"name":"setAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getCreator","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getURL","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getAddress","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newCreator","type":"address"}],"name":"setCreator","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"entry","outputs":[{"name":"ip","type":"string"},{"name":"url","type":"string"},{"name":"dateOfCreation","type":"uint256"},{"name":"expireTimeAmount","type":"uint256"},{"name":"creator","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newURL","type":"string"}],"name":"setURL","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newDateOfCreation","type":"uint256"}],"name":"setDateOfCreation","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newExpireTimeAmount","type":"uint256"}],"name":"setExpireTimeAmount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getDateOfCreation","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getExpireTimeAmount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]''')
contract = w3.eth.contract(address=contract_address, abi=abi)

tx_hash = contract.functions.setURL("BCD2.com").transact()
w3.eth.waitForTransactionReceipt(tx_hash)
tx_hash = contract.functions.setExpireTimeAmount(1).transact()
w3.eth.waitForTransactionReceipt(tx_hash)
tx_hash = contract.functions.setAddress("142.250.74.206").transact()
w3.eth.waitForTransactionReceipt(tx_hash)

contract = w3.eth.contract(address=contract_address, abi=abi)
