from web3.auto import w3
from hexbytes import HexBytes
from web3.contract import ConciseContract
import os
from utils import *
from common import *

def main():
    rsk = UserRSKContract(USER_CONTRACT_ADDR, USER_ABI_FILE)
    pwd_hash =  HexBytes('0x93f0218b357b9256799540fe638f53f9ab92be1e0457d42c7470c3bd3140d393')
    exit(0)
    txn_id = 1
    tx_hash = rsk.create_transaction(txn_id, USER, CUSTODIAN, pwd_hash, 200,
                                     int(0.001 * 1e18)) 
    wait_to_be_mined(tx_hash)
     
    # TODO: Next watch for CustodianTransactionCreated event.
    # Check the if the transaction contents are ok 
    # User watches CustodianTransferred() event on Eth

    tx_receipt = erc20_approve(WETH_ADDR, USER, USER_CONTRACT_ADDR, 
                               int(10.0 * 1e18))

    tx_receipt = contract.transfer_to_contract(txn_id, USER) 
    
    # TODO: Watch for CustodianExecutionSuccess event and read the password  

    eth = CustodianEthContract(CUSTODIAN_CONTRACT_ADDR, CUSTODIAN_ABI_FILE)
    eth.execute(txn_id, pwd_str)
   

if __name__== '__main__':
    main()
