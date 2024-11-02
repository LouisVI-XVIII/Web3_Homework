import json
import os
from web3 import Web3
from dotenv import load_dotenv


load_dotenv()
ANVIL_ACCOUNT = os.getenv("ANVIL_ACCOUNT")
ANVIL_PRIVATE_KEY = os.getenv("ANVIL_PRIVATE_KEY")
LOCAL_PROVIDER = os.getenv("LOCAL_PROVIDER")


w3 = Web3(Web3.HTTPProvider(LOCAL_PROVIDER))
chain_id = 31337  


with open("src/compiled_code.json", "r") as file:
    compiled_contract = json.load(file)
    
    abi = compiled_contract['contracts']['/Users/Pierre/Desktop/BLOCKCH/Web3_Homework/newContract.sol']['newContract']['abi']


contract_address = "0x5FbDB2315678afecb367f032d93F642f64180aa3"  

contract = w3.eth.contract(address=contract_address, abi=abi)


update_tx = contract.functions.updateID(5341).build_transaction({
    'chainId': chain_id,
    'from': ANVIL_ACCOUNT,
    'nonce': w3.eth.get_transaction_count(ANVIL_ACCOUNT),
    'gas': 6721975,
    'gasPrice': w3.to_wei('1', 'gwei')  
})

signed_update_tx = w3.eth.account.sign_transaction(update_tx, private_key=ANVIL_PRIVATE_KEY)
w3.eth.send_raw_transaction(signed_update_tx.raw_transaction)


updated_value = contract.functions.viewMyId().call()
print(f"Updated StudentId: {updated_value}")



