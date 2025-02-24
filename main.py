import asyncio
from banner import display_banner
from config import web3
from transactions import send_transactions
from colorama import Fore, Style

# Load private keys
with open("pvkeys.txt", "r") as file:
    private_keys = [line.strip() for line in file if line.strip()]
display_banner()

async def main():
    num_transactions = None  # Initialize the number of transactions as None

    while True:
        # Ask for the number of transactions only if it hasn't been set yet
        if num_transactions is None:
            while True:
                try:
                    num_transactions = int(input(f"{Fore.CYAN}Enter the number of transactions to perform per account: {Style.RESET_ALL}"))
                    if num_transactions > 0:
                        break
                    else:
                        print(f"{Fore.RED}Number of transactions must be greater than 0.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Invalid input. Please enter a valid number.{Style.RESET_ALL}")

        # Process transactions for each private key
        for private_key in private_keys:
            from_address = web3.eth.account.from_key(private_key).address
            short_address = f"{from_address[:8]}...{from_address[-4:]}"
            print(f"{Fore.CYAN}[{short_address}] Processing Daily Transactions: {short_address}{Style.RESET_ALL}")
            
            # Send transactions
            await send_transactions(private_key, num_transactions)

        print(f"{Fore.YELLOW}All accounts processed. Sleeping for 24 hours...{Style.RESET_ALL}")
        await asyncio.sleep(24 * 60 * 60)

asyncio.run(main())
