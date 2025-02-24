from web3 import Web3

# Monad Network details
RPC_URL = "https://testnet-rpc.monad.xyz"  # Monad RPC URL
CHAIN_ID = 10143  # Monad Chain ID
CURRENCY_SYMBOL = "MON"  # Currency symbol for Monad
BLOCK_EXPLORER_URL = "https://testnet.monadexplorer.com/"  # Block explorer URL

# Transaction settings
max_gwei = 50  # Maximum gas price you're willing to pay (adjust as needed)
AMOUNT_ETH = 0.00000005  # ETH amount per transaction (adjust as needed)

# Contract details
CONTRACT_ADDRESS = "0x760AfE86e5de5fa0Ee542fc7B7B713e1c5425701"  # wmonad contract address
contract_abi = '''
[
    {
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]
'''

# Connect to Monad Network
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Ensure connection is successful
if not web3.is_connected():
    raise Exception("Failed to connect to Monad Network")

# Optional: Connect to Ethereum RPC for gas price checks (if needed)
RPC_ETH = "https://eth.llamarpc.com"  # Ethereum RPC for gas price comparison
check_gass = Web3(Web3.HTTPProvider(RPC_ETH))
