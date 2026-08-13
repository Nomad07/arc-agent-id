import os

from dotenv import load_dotenv
from web3 import Web3


load_dotenv()


RPC_URL = os.getenv(
    "RPC_URL",
    "https://rpc.testnet.arc.network"
)

PRIVATE_KEY = os.getenv("PRIVATE_KEY")

METADATA_URI = os.getenv(
    "METADATA_URI",
    "ipfs://bafkreibdi6623n3xpf7ymk62ckb4bo75o3qemwkpfvp5i25j66itxvsoei"
)

AGENT_ID = os.getenv("AGENT_ID")

CHAIN_ID = 5042002

IDENTITY_REGISTRY = Web3.to_checksum_address(
    "0x8004A818BFB912233c491871b3d84c89A494BD9e"
)


IDENTITY_ABI = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "agentURI",
                "type": "string"
            }
        ],
        "name": "register",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "ownerOf",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "tokenURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]


def connect_to_arc():

    web3 = Web3(
        Web3.HTTPProvider(RPC_URL)
    )

    if not web3.is_connected():

        raise RuntimeError(
            "Could not connect to Arc RPC"
        )

    if web3.eth.chain_id != CHAIN_ID:

        raise RuntimeError(
            f"Wrong chain ID: "
            f"{web3.eth.chain_id}"
        )

    return web3


def get_account(web3):

    if not PRIVATE_KEY:

        raise RuntimeError(
            "PRIVATE_KEY is not set in .env"
        )

    return web3.eth.account.from_key(
        PRIVATE_KEY
    )


def get_contract(web3):

    return web3.eth.contract(
        address=IDENTITY_REGISTRY,
        abi=IDENTITY_ABI
    )


def check_agent(
    web3,
    agent_id
):

    contract = get_contract(web3)

    try:

        owner = contract.functions.ownerOf(
            agent_id
        ).call()

        metadata_uri = contract.functions.tokenURI(
            agent_id
        ).call()

    except Exception as error:

        print()
        print(
            f"Could not read agent {agent_id}:"
        )
        print(
            error
        )
        return

    print()
    print(
        "========================================"
    )
    print(
        "ERC-8004 AGENT"
    )
    print(
        "========================================"
    )
    print()
    print(
        "Network:      Arc Testnet"
    )
    print(
        f"Chain ID:     {web3.eth.chain_id}"
    )
    print(
        f"Agent ID:     {agent_id}"
    )
    print(
        f"Owner:        {owner}"
    )
    print(
        f"Metadata URI: {metadata_uri}"
    )
    print(
        f"Registry:     {IDENTITY_REGISTRY}"
    )
    print()
    print(
        "Status:       Registered"
    )
    print()
    print(
        "========================================"
    )


def register_agent(
    web3,
    account
):

    contract = get_contract(web3)

    print()
    print(
        "========================================"
    )
    print(
        "ERC-8004 AGENT REGISTRATION"
    )
    print(
        "========================================"
    )
    print()
    print(
        "Network:  Arc Testnet"
    )
    print(
        f"Chain ID: {web3.eth.chain_id}"
    )
    print(
        f"Wallet:   {account.address}"
    )
    print(
        f"Metadata: {METADATA_URI}"
    )
    print()

    nonce = web3.eth.get_transaction_count(
        account.address
    )

    transaction = contract.functions.register(
        METADATA_URI
    ).build_transaction(
        {
            "from": account.address,
            "nonce": nonce,
            "chainId": CHAIN_ID,
            "gas": 500000,
            "gasPrice": web3.eth.gas_price,
        }
    )

    signed_transaction = account.sign_transaction(
        transaction
    )

    print(
        "Sending registration transaction..."
    )

    tx_hash = web3.eth.send_raw_transaction(
        signed_transaction.raw_transaction
    )

    print()
    print(
        f"Transaction: {tx_hash.hex()}"
    )
    print()
    print(
        "Waiting for confirmation..."
    )

    receipt = web3.eth.wait_for_transaction_receipt(
        tx_hash
    )

    if receipt.status != 1:

        raise RuntimeError(
            "Registration transaction failed"
        )

    print(
        f"Confirmed in block: "
        f"{receipt.blockNumber}"
    )

    transfer_event = contract.events.Transfer()

    events = transfer_event.process_receipt(
        receipt
    )

    agent_id = None

    for event in events:

        event_args = event["args"]

        if (
            event_args["from"].lower()
            == "0x0000000000000000000000000000000000000000"
        ):

            if (
                event_args["to"].lower()
                == account.address.lower()
            ):

                agent_id = event_args["tokenId"]

                break

    if agent_id is None:

        raise RuntimeError(
            "Agent ID was not found"
        )

    print()
    print(
        "========================================"
    )
    print(
        "AGENT REGISTERED"
    )
    print(
        "========================================"
    )
    print()
    print(
        f"Agent ID: {agent_id}"
    )
    print(
        f"Owner:    {account.address}"
    )
    print(
        f"Tx Hash:  {tx_hash.hex()}"
    )
    print(
        f"Block:    {receipt.blockNumber}"
    )
    print()
    print(
        f"https://testnet.arcscan.app/tx/"
        f"{tx_hash.hex()}"
    )
    print()
    print(
        "========================================"
    )


def show_menu():

    print()
    print(
        "========================================"
    )
    print(
        "Arc Agent ID"
    )
    print(
        "ERC-8004 Toolkit"
    )
    print(
        "========================================"
    )
    print()
    print(
        "1. Check existing agent"
    )
    print(
        "2. Register new agent"
    )
    print(
        "3. Exit"
    )
    print()


def main():

    try:

        web3 = connect_to_arc()

        print()
        print(
            f"Connected to Arc Testnet"
        )
        print(
            f"Chain ID: {web3.eth.chain_id}"
        )

        while True:

            show_menu()

            choice = input(
                "Select an option: "
            ).strip()

            if choice == "1":

                agent_id = input(
                    "Enter Agent ID: "
                ).strip()

                if not agent_id.isdigit():

                    print(
                        "Invalid Agent ID."
                    )
                    continue

                check_agent(
                    web3,
                    int(agent_id)
                )

            elif choice == "2":

                account = get_account(
                    web3
                )

                register_agent(
                    web3,
                    account
                )

            elif choice == "3":

                print(
                    "Goodbye."
                )
                break

            else:

                print(
                    "Invalid option."
                )

    except KeyboardInterrupt:

        print()
        print(
            "Stopped."
        )

    except Exception as error:

        print()
        print(
            "ERROR:"
        )
        print(
            error
        )


if __name__ == "__main__":

    main()