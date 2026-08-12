cat > main.py <<'EOF'
import os
from web3 import Web3
from dotenv import load_dotenv

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

IDENTITY_REGISTRY = Web3.to_checksum_address(
    "0x8004A818BFB912233c491871b3d84c89A494BD9e"
)

CHAIN_ID = 5042002

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
        "outputs": [
            {
                "internalType": "uint256",
                "name": "agentId",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
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

    chain_id = web3.eth.chain_id

    if chain_id != CHAIN_ID:
        raise RuntimeError(
            f"Wrong chain ID: {chain_id}. "
            f"Expected {CHAIN_ID}."
        )

    return web3


def get_account(web3):

    if not PRIVATE_KEY:
        raise RuntimeError(
            "PRIVATE_KEY is not set in .env"
        )

    account = web3.eth.account.from_key(
        PRIVATE_KEY
    )

    return account


def register_agent(web3, account):

    contract = web3.eth.contract(
        address=IDENTITY_REGISTRY,
        abi=IDENTITY_ABI
    )

    nonce = web3.eth.get_transaction_count(
        account.address
    )

    print()
    print("========================================")
    print("Arc Agent ID")
    print("========================================")
    print()
    print(
        f"Network:  Arc Testnet"
    )
    print(
        f"Chain ID: {web3.eth.chain_id}"
    )
    print(
        f"Wallet:   {account.address}"
    )
    print(
        f"Registry: {IDENTITY_REGISTRY}"
    )
    print(
        f"Metadata: {METADATA_URI}"
    )
    print()
    print("Building registration transaction...")

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

    print("Sending transaction...")

    tx_hash = web3.eth.send_raw_transaction(
        signed_transaction.raw_transaction
    )

    print()
    print(
        f"Transaction: {tx_hash.hex()}"
    )

    print("Waiting for confirmation...")

    receipt = web3.eth.wait_for_transaction_receipt(
        tx_hash
    )

    if receipt.status != 1:
        raise RuntimeError(
            "Agent registration transaction failed"
        )

    print()
    print("Transaction confirmed.")
    print(
        f"Block: {receipt.blockNumber}"
    )

    agent_id = None

    transfer_event = contract.events.Transfer()

    events = transfer_event.process_receipt(
        receipt
    )

    for event in events:

        args = event["args"]

        if (
            args["from"]
            == "0x0000000000000000000000000000000000000000"
        ):
            agent_id = args["tokenId"]

            break

    if agent_id is None:
        raise RuntimeError(
            "Could not find agentId in Transfer event"
        )

    print()
    print("========================================")
    print("AGENT REGISTERED")
    print("========================================")
    print()
    print(
        f"Agent ID: {agent_id}"
    )
    print(
        f"Owner:    {account.address}"
    )
    print(
        f"Metadata: {METADATA_URI}"
    )
    print(
        f"Tx Hash:  {tx_hash.hex()}"
    )
    print(
        f"Block:    {receipt.blockNumber}"
    )
    print()
    print("========================================")


def main():

    try:

        web3 = connect_to_arc()

        account = get_account(
            web3
        )

        register_agent(
            web3,
            account
        )

    except Exception as error:

        print()
        print(
            f"Error: {error}"
        )
        print()


if __name__ == "__main__":
    main()
EOF