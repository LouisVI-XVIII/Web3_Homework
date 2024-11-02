from solcx import compile_standard
import json
import os


SOLIDITY_PRAGMA = "0.8.13"


def compile_solidity(contract: str) -> dict:
    
    with open(contract, 'r') as file:
        contract_file = file.read()

    
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {contract: {"content": contract_file}},
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["abi", "evm.bytecode"]
                    }
                }
            },
        },
        solc_version=SOLIDITY_PRAGMA
    )

    return compiled_sol


contract_path = os.path.join(os.path.dirname(__file__), '/Users/Pierre/Desktop/BLOCKCH/Web3_Homework/newContract.sol')


compiled_contract = compile_solidity(contract_path)


output_path = os.path.join(os.path.dirname(__file__), 'compiled_code.json')
with open(output_path, "w") as file:
    json.dump(compiled_contract, file)

print("Contract compiled successfully and saved as 'compiled_code.json'")
