import os

from dotenv import load_dotenv
from web3 import Web3


load_dotenv()


NETWORK = os.getenv(
    "NETWORK",
    "testnet"
).lower()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")

METADATA_URI = os.getenv(
    "METADATA_URI",
    "ipfs://bafkreibdi6623n3xpf7ymk62ckb4bo75o3qemwkpfvp5i25j66itxvsoei"
)

AGENT_ID = os.getenv("AGENT_ID")


NETWORKS = {
    "testnet": {
        "rpc_url": "https://rpc.testnet.arc.network",
        "chain_id": 5042002,
        "identity_registry": "0x8004A818BFB912233c491871b3d84c89A494BD9e",
        "reputation_registry": "0x8004B663056A597Dffe9eCcC1965A193B7388713",
        "validation_registry": "0x8004Cb1BF31DAf7788923b405b754f57acEB4272",
    },
    "mainnet": {
        "rpc_url": "https://rpc.mainnet.arc.io",
        "chain_id": 5042,
        "identity_registry": "0x8004A169FB4a3325136EB29fA0ceB6D2e539a432",
        "reputation_registry": "0x8004BAa17C55a88189AE136b182e5fdA19dE9b63",
        "validation_registry": None,
    },
}

if NETWORK not in NETWORKS:
    raise RuntimeError(
        f"Unsupported network: {NETWORK}. "
        f"Use testnet or mainnet."
    )

NETWORK_CONFIG = NETWORKS[NETWORK]

RPC_URL = NETWORK_CONFIG["rpc_url"]
CHAIN_ID = NETWORK_CONFIG["chain_id"]

IDENTITY_REGISTRY = Web3.to_checksum_address(
    NETWORK_CONFIG["identity_registry"]
)

REPUTATION_REGISTRY = Web3.to_checksum_address(
    NETWORK_CONFIG["reputation_registry"]
)

VALIDATION_REGISTRY = (
    Web3.to_checksum_address(
        NETWORK_CONFIG["validation_registry"]
    )
    if NETWORK_CONFIG["validation_registry"]
    else None
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
                "name": "agentId",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "newURI",
                "type": "string"
            }
        ],
        "name": "setAgentURI",
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
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "agentId",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "newURI",
                "type": "string"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "updatedBy",
                "type": "address"
            }
        ],
        "name": "URIUpdated",
        "type": "event"
    }
]


REPUTATION_ABI = [
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "agentId",
                "type": "uint256"
            }
        ],
        "name": "getClients",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "agentId",
                "type": "uint256"
            },
            {
                "internalType": "address[]",
                "name": "clientAddresses",
                "type": "address[]"
            },
            {
                "internalType": "string",
                "name": "tag1",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "tag2",
                "type": "string"
            }
        ],
        "name": "getSummary",
        "outputs": [
            {
                "internalType": "uint64",
                "name": "count",
                "type": "uint64"
            },
            {
                "internalType": "int128",
                "name": "summaryValue",
                "type": "int128"
            },
            {
                "internalType": "uint8",
                "name": "summaryValueDecimals",
                "type": "uint8"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "agentId",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "clientAddress",
                "type": "address"
            },
            {
                "internalType": "uint64",
                "name": "feedbackIndex",
                "type": "uint64"
            }
        ],
        "name": "readFeedback",
        "outputs": [
            {
                "internalType": "int128",
                "name": "value",
                "type": "int128"
            },
            {
                "internalType": "uint8",
                "name": "valueDecimals",
                "type": "uint8"
            },
            {
                "internalType": "string",
                "name": "tag1",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "tag2",
                "type": "string"
            },
            {
                "internalType": "bool",
                "name": "isRevoked",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]


VALIDATION_ABI = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validatorAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "agentId",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "requestURI",
                "type": "string"
            },
            {
                "internalType": "bytes32",
                "name": "requestHash",
                "type": "bytes32"
            }
        ],
        "name": "validationRequest",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "requestHash",
                "type": "bytes32"
            },
            {
                "internalType": "uint8",
                "name": "response",
                "type": "uint8"
            },
            {
                "internalType": "string",
                "name": "responseURI",
                "type": "string"
            },
            {
                "internalType": "bytes32",
                "name": "responseHash",
                "type": "bytes32"
            },
            {
                "internalType": "string",
                "name": "tag",
                "type": "string"
            }
        ],
        "name": "validationResponse",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "agentId",
                "type": "uint256"
            }
        ],
        "name": "getAgentValidations",
        "outputs": [
            {
                "internalType": "bytes32[]",
                "name": "",
                "type": "bytes32[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "requestHash",
                "type": "bytes32"
            }
        ],
        "name": "getValidationStatus",
        "outputs": [
            {
                "internalType": "address",
                "name": "validatorAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "agentId",
                "type": "uint256"
            },
            {
                "internalType": "uint8",
                "name": "response",
                "type": "uint8"
            },
            {
                "internalType": "bytes32",
                "name": "responseHash",
                "type": "bytes32"
            },
            {
                "internalType": "string",
                "name": "tag",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "lastUpdate",
                "type": "uint256"
            }
        ],
        "name": "getValidationStatus",
        "outputs": [
            {
                "internalType": "address",
                "name": "validatorAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "agentId",
                "type": "uint256"
            },
            {
                "internalType": "uint8",
                "name": "response",
                "type": "uint8"
            },
            {
                "internalType": "bytes32",
                "name": "responseHash",
                "type": "bytes32"
            },
            {
                "internalType": "string",
                "name": "tag",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "lastUpdate",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "agentId",
                "type": "uint256"
            },
            {
                "internalType": "address[]",
                "name": "validatorAddresses",
                "type": "address[]"
            },
            {
                "internalType": "string",
                "name": "tag",
                "type": "string"
            }
        ],
        "name": "getSummary",
        "outputs": [
            {
                "internalType": "uint64",
                "name": "count",
                "type": "uint64"
            },
            {
                "internalType": "uint8",
                "name": "averageResponse",
                "type": "uint8"
            }
        ],
        "stateMutability": "view",
        "type": "function"
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


def get_reputation_contract(web3):

    return web3.eth.contract(
        address=REPUTATION_REGISTRY,
        abi=REPUTATION_ABI
    )


def get_validation_contract(web3):

    return web3.eth.contract(
        address=VALIDATION_REGISTRY,
        abi=VALIDATION_ABI
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


def check_reputation(
    web3,
    agent_id
):

    contract = get_reputation_contract(web3)

    print()
    print(
        "========================================"
    )
    print(
        "ERC-8004 REPUTATION"
    )
    print(
        "========================================"
    )
    print()
    print(
        f"Agent ID:     {agent_id}"
    )
    print(
        f"Registry:     {REPUTATION_REGISTRY}"
    )
    print()

    try:

        clients = contract.functions.getClients(
            agent_id
        ).call()

    except Exception as error:

        print(
            "Could not read reputation:"
        )
        print(
            error
        )
        return

    if not clients:

        print(
            "Feedback clients: 0"
        )
        print()
        print(
            "No reputation feedback found."
        )
        print()
        print(
            "========================================"
        )
        return

    print(
        f"Feedback clients: {len(clients)}"
    )
    print()

    for index, client in enumerate(
        clients,
        start=1
    ):

        print(
            f"Client {index}:     {client}"
        )

    print()

    try:

        (
            count,
            summary_value,
            summary_decimals
        ) = contract.functions.getSummary(
            agent_id,
            clients,
            "",
            ""
        ).call()

        if summary_decimals > 0:

            display_value = (
                summary_value
                / (10 ** summary_decimals)
            )

        else:

            display_value = summary_value

        print(
            f"Feedback count:   {count}"
        )
        print(
            f"Summary value:    {display_value}"
        )
        print(
            f"Value decimals:   {summary_decimals}"
        )

    except Exception as error:

        print()
        print(
            "Could not calculate reputation summary:"
        )
        print(
            error
        )

    print()
    print(
        "========================================"
    )


def check_validation(
    web3,
    agent_id
):

    contract = get_validation_contract(web3)

    print()
    print(
        "========================================"
    )
    print(
        "ERC-8004 VALIDATION"
    )
    print(
        "========================================"
    )
    print()
    print(
        f"Agent ID:     {agent_id}"
    )
    print(
        f"Registry:     {VALIDATION_REGISTRY}"
    )
    print()

    try:

        request_hashes = (
            contract.functions.getAgentValidations(
                agent_id
            ).call()
        )

    except Exception as error:

        print(
            "Could not read validation data:"
        )
        print(
            error
        )
        return

    if not request_hashes:

        print(
            "Validation requests: 0"
        )
        print()
        print(
            "No validation requests found."
        )
        print()
        print(
            "========================================"
        )
        return

    print(
        f"Validation requests: {len(request_hashes)}"
    )
    print()

    for index, request_hash in enumerate(
        request_hashes,
        start=1
    ):

        try:

            (
                validator,
                returned_agent_id,
                response,
                response_hash,
                tag,
                last_update
            ) = contract.functions.getValidationStatus(
                request_hash
            ).call()

            print(
                f"Validation {index}"
            )
            print(
                f"Request hash: {request_hash.hex()}"
            )
            print(
                f"Validator:    {validator}"
            )
            print(
                f"Agent ID:     {returned_agent_id}"
            )
            print(
                f"Response:     {response}/100"
            )
            print(
                f"Tag:          {tag or '-'}"
            )
            print(
                f"Last update:  {last_update}"
            )
            print(
                f"Response hash: {response_hash.hex()}"
            )
            print()

        except Exception as error:

            print(
                f"Could not read validation "
                f"{index}:"
            )
            print(
                error
            )
            print()

    try:

        count, average_response = (
            contract.functions.getSummary(
                agent_id,
                [],
                ""
            ).call()
        )

        print(
            f"Validation count:  {count}"
        )
        print(
            f"Average response: {average_response}/100"
        )

    except Exception as error:

        print(
            "Could not calculate validation summary:"
        )
        print(
            error
        )

    print()
    print(
        "========================================"
    )


def submit_validation_request(
    web3,
    account
):

    contract = get_validation_contract(web3)

    print()
    print(
        "========================================"
    )
    print(
        "SUBMIT ERC-8004 VALIDATION REQUEST"
    )
    print(
        "========================================"
    )
    print()

    agent_id_input = input(
        "Enter Agent ID: "
    ).strip()

    if not agent_id_input.isdigit():

        print(
            "Invalid Agent ID."
        )
        return

    agent_id = int(agent_id_input)

    identity_contract = get_contract(web3)

    try:

        owner = identity_contract.functions.ownerOf(
            agent_id
        ).call()

    except Exception as error:

        print(
            f"Could not read agent {agent_id}:"
        )
        print(
            error
        )
        return

    if owner.lower() != account.address.lower():

        print()
        print(
            "You are not the owner of this agent."
        )
        print(
            f"Agent owner:      {owner}"
        )
        print(
            f"Connected wallet: {account.address}"
        )
        return

    print()
    print(
        "Validator address must be an EVM address."
    )
    print(
        "For the first test you can use the"
    )
    print(
        "Sentinel owner we found earlier:"
    )
    print(
        "0x56509b03e85f3cBAe5bA2190ee99B945D2f0AC36"
    )
    print()

    validator_input = input(
        "Enter Validator Address: "
    ).strip()

    try:

        validator_address = Web3.to_checksum_address(
            validator_input
        )

    except Exception:

        print(
            "Invalid validator address."
        )
        return

    print()
    print(
        "Enter a request URI."
    )
    print(
        "This URI should identify the validation"
    )
    print(
        "request and its evaluation data."
    )
    print()

    request_uri = input(
        "Enter Request URI: "
    ).strip()

    if not request_uri:

        print(
            "Request URI cannot be empty."
        )
        return

    request_hash = Web3.keccak(
        text=request_uri
    )

    print()
    print(
        "========================================"
    )
    print(
        "VALIDATION REQUEST"
    )
    print(
        "========================================"
    )
    print()
    print(
        f"Agent ID:       {agent_id}"
    )
    print(
        f"Owner:          {account.address}"
    )
    print(
        f"Validator:      {validator_address}"
    )
    print(
        f"Request URI:    {request_uri}"
    )
    print(
        f"Request Hash:   {request_hash.hex()}"
    )
    print()
    print(
        f"Registry:       {VALIDATION_REGISTRY}"
    )
    print()

    print(
        "This will send a real transaction"
    )
    print(
        "to Arc Testnet."
    )
    print()

    confirmation = input(
        "Submit validation request? (y/n): "
    ).strip().lower()

    if confirmation != "y":

        print(
            "Validation request cancelled."
        )
        return

    nonce = web3.eth.get_transaction_count(
        account.address
    )

    transaction = contract.functions.validationRequest(
        validator_address,
        agent_id,
        request_uri,
        request_hash
    ).build_transaction(
        {
            "from": account.address,
            "nonce": nonce,
            "chainId": CHAIN_ID,
            "gas": 300000,
            "gasPrice": web3.eth.gas_price,
        }
    )

    signed_transaction = account.sign_transaction(
        transaction
    )

    print()
    print(
        "Sending validation request transaction..."
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
            "Validation request transaction failed"
        )

    print()
    print(
        "========================================"
    )
    print(
        "VALIDATION REQUEST SUBMITTED"
    )
    print(
        "========================================"
    )
    print()
    print(
        f"Agent ID:       {agent_id}"
    )
    print(
        f"Validator:      {validator_address}"
    )
    print(
        f"Request URI:    {request_uri}"
    )
    print(
        f"Request Hash:   {request_hash.hex()}"
    )
    print(
        f"Tx Hash:        {tx_hash.hex()}"
    )
    print(
        f"Block:          {receipt.blockNumber}"
    )
    print()
    print(
        "Status:         Confirmed"
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


def update_agent_metadata(
    web3,
    account
):

    contract = get_contract(web3)

    print()
    print(
        "========================================"
    )
    print(
        "UPDATE ERC-8004 AGENT METADATA"
    )
    print(
        "========================================"
    )
    print()

    agent_id_input = input(
        "Enter Agent ID: "
    ).strip()

    if not agent_id_input.isdigit():

        print(
            "Invalid Agent ID."
        )
        return

    agent_id = int(agent_id_input)

    try:

        owner = contract.functions.ownerOf(
            agent_id
        ).call()

        current_uri = contract.functions.tokenURI(
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

    if owner.lower() != account.address.lower():

        print()
        print(
            "You are not the owner of this agent."
        )
        print(
            f"Agent owner:    {owner}"
        )
        print(
            f"Connected wallet: {account.address}"
        )
        return

    print()
    print(
        f"Agent ID:     {agent_id}"
    )
    print(
        f"Current URI:  {current_uri}"
    )
    print()

    new_uri = input(
        "Enter new Metadata URI: "
    ).strip()

    if not new_uri:

        print(
            "Metadata URI cannot be empty."
        )
        return

    if new_uri == current_uri:

        print(
            "New URI is the same as the current URI."
        )
        return

    print()
    print(
        f"New URI:      {new_uri}"
    )
    print()

    confirmation = input(
        "Update metadata? (y/n): "
    ).strip().lower()

    if confirmation != "y":

        print(
            "Update cancelled."
        )
        return

    nonce = web3.eth.get_transaction_count(
        account.address
    )

    transaction = contract.functions.setAgentURI(
        agent_id,
        new_uri
    ).build_transaction(
        {
            "from": account.address,
            "nonce": nonce,
            "chainId": CHAIN_ID,
            "gas": 300000,
            "gasPrice": web3.eth.gas_price,
        }
    )

    signed_transaction = account.sign_transaction(
        transaction
    )

    print()
    print(
        "Sending metadata update transaction..."
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
            "Metadata update transaction failed"
        )

    print()
    print(
        "========================================"
    )
    print(
        "METADATA UPDATED"
    )
    print(
        "========================================"
    )
    print()
    print(
        f"Agent ID:     {agent_id}"
    )
    print(
        f"Old URI:      {current_uri}"
    )
    print(
        f"New URI:      {new_uri}"
    )
    print(
        f"Tx Hash:      {tx_hash.hex()}"
    )
    print(
        f"Block:        {receipt.blockNumber}"
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
        "3. Update agent metadata"
    )
    print(
        "4. Check reputation"
    )
    print(
        "5. Check validation"
    )
    print(
        "6. Submit validation request"
    )
    print(
        "7. Exit"
    )
    print()


def main():

    try:

        web3 = connect_to_arc()

        print()
        print(
            "Connected to Arc Testnet"
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

                account = get_account(
                    web3
                )

                update_agent_metadata(
                    web3,
                    account
                )

            elif choice == "4":

                agent_id = input(
                    "Enter Agent ID: "
                ).strip()

                if not agent_id.isdigit():

                    print(
                        "Invalid Agent ID."
                    )
                    continue

                check_reputation(
                    web3,
                    int(agent_id)
                )

            elif choice == "5":

                agent_id = input(
                    "Enter Agent ID: "
                ).strip()

                if not agent_id.isdigit():

                    print(
                        "Invalid Agent ID."
                    )
                    continue

                check_validation(
                    web3,
                    int(agent_id)
                )

            elif choice == "6":

                account = get_account(
                    web3
                )

                submit_validation_request(
                    web3,
                    account
                )

            elif choice == "7":

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