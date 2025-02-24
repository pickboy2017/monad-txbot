import asyncio
import json
from colorama import Fore, Style
from config import web3, AMOUNT_ETH, CONTRACT_ADDRESS, contract_abi
import random

async def send_transactions(private_key, num_transactions):
    """Send multiple transactions for a single account."""
    amount_wei = web3.to_wei(AMOUNT_ETH, 'ether')
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=json.loads(contract_abi))
    from_address = web3.eth.account.from_key(private_key).address

    for i in range(num_transactions):
        print(f"{Fore.CYAN}[{from_address[:8]}...{from_address[-4:]}] Starting transaction {i + 1}...{Style.RESET_ALL}")

        # Get current gas price
        gas_price = web3.eth.gas_price
        gas_price_in_gwei = gas_price / 1e9  # Convert gas price to Gwei

        # Check if gas price is below 0.002 Gwei (adjust this threshold if needed)
        if gas_price_in_gwei < 100:
            print(f"{Fore.YELLOW}[{from_address[:8]}...{from_address[-4:]}] Current Gas Price: {gas_price_in_gwei} Gwei (Below 0.002 Gwei). Proceeding with transaction...{Style.RESET_ALL}")

            retries = 0
            max_retries = 3
            while retries < max_retries:
                try:
                    # Build the transaction
                    transaction = contract.functions.deposit().build_transaction({
                        'from': from_address,
                        'value': amount_wei,
                        'gas': 30902,
                        'gasPrice': gas_price,
                        'nonce': web3.eth.get_transaction_count(from_address),
                        'chainId': 10143  # Monad testnet chain ID
                    })
                    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
                    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

                    print(f"{Fore.GREEN}[{from_address[:8]}...{from_address[-4:]}] Transaction {i + 1} sent: {tx_hash.hex()}{Style.RESET_ALL}")
                    random_delay = random.randint(5, 30)
                    await asyncio.sleep(random_delay)
                    break  # Exit retry loop if transaction is successful

                except Exception as e:
                    retries += 1
                    print(f"{Fore.RED}[{from_address[:8]}...{from_address[-4:]}] Error in transaction {i + 1}: {str(e)}. Retrying... ({retries}/{max_retries}){Style.RESET_ALL}")
                    await asyncio.sleep(5)
                    if retries >= max_retries:
                        print(f"{Fore.RED}[{from_address[:8]}...{from_address[-4:]}] Max retries reached for transaction {i + 1}. Moving to next transaction.{Style.RESET_ALL}")
                        break
        else:
            # Gas price is above 0.002 Gwei, skip the transaction
            print(f"{Fore.RED}[{from_address[:8]}...{from_address[-4:]}] Gas price is {gas_price_in_gwei} Gwei (Above 0.002 Gwei). Skipping transaction.{Style.RESET_ALL}")
            continue  # Skip to the next transaction
