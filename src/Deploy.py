from web3 import Web3
import json
import os
from dotenv import load_dotenv
from Compile import compile_solidity


load_dotenv()

ACCOUNT = os.getenv("ANVIL_ACCOUNT")
PRIVATE_KEY = os.getenv("ANVIL_PRIVATE_KEY")
LOCAL_PROVIDER = os.getenv("LOCAL_PROVIDER")

def deploy_contract(contract_file: str = "/Users/Pierre/Desktop/BLOCKCH/Web3_Homework/newContract.sol", contract_name: str = "newContract"):
    
    compiled_sol = compile_solidity(contract_file)

   
    bytecode = compiled_sol["contracts"][contract_file][contract_name]["evm"]["bytecode"]["object"]
    abi = compiled_sol["contracts"][contract_file][contract_name]["abi"]

    
    w3 = Web3(Web3.HTTPProvider(LOCAL_PROVIDER))
    chain_id = 31337
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.get_transaction_count(ACCOUNT)

    
    transaction = contract.constructor().build_transaction({
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": ACCOUNT,
        "nonce": nonce
    })

   
    signed_txn = w3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

    
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

   
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

  
    return tx_receipt.contractAddress, abi

if __name__ == "__main__":
   
    contract_address, abi = deploy_contract()
    print(f"Contract deployed at address: {contract_address}")
