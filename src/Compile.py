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


if __name__ == "__main__":
    compiled_sol = compile_solidity ("/Users/Pierre/Desktop/BLOCKCH/Web3_Homework/newContract.sol")
    with open("/Users/Pierre/Desktop/BLOCKCH/Web3_Homework/src/compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)
        print(compiled_sol)

