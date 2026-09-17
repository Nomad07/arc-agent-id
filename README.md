# Arc Agent ID

A Python toolkit for registering, checking and updating AI agent identities on Arc using ERC-8004.

The toolkit supports both **Arc Testnet** and **Arc Mainnet**, with separate agent identities and network-specific ERC-8004 registries.

## Features

* Connect to Arc Testnet or Arc Mainnet
* Switch between networks from the application menu
* Check Arc chain ID
* Register a new AI agent
* Check an existing agent
* Read agent owner
* Read agent metadata URI
* Update agent metadata URI
* Verify agent registration
* Check agent reputation
* Check agent validation status on Testnet
* Submit validation requests on Testnet
* Display transaction information
* Use environment variables for private configuration

## Requirements

* Python 3.10+
* An Arc Testnet or Arc Mainnet wallet
* Network funds for transaction fees
* A private key stored locally in `.env`

## Installation

Clone the repository:

```bash
git clone https://github.com/Nomad07/arc-agent-id.git
cd arc-agent-id
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
NETWORK=testnet
PRIVATE_KEY=your_private_key
METADATA_URI=ipfs://your_metadata_uri
AGENT_ID=876991
```

For Mainnet:

```env
NETWORK=mainnet
PRIVATE_KEY=your_private_key
METADATA_URI=ipfs://your_metadata_uri
AGENT_ID=15
```

`NETWORK` can be set to:

```text
testnet
mainnet
```

The application loads the correct RPC endpoint, Chain ID and ERC-8004 registry addresses automatically based on the selected network.

Never commit `.env` or expose your private key.

## Usage

Run the toolkit:

```bash
python main.py
```

The application provides:

```text
1. Check existing agent
2. Register new agent
3. Update agent metadata
4. Check reputation
5. Check validation
6. Submit validation request
7. Exit
```

The network can be selected when the application starts.

## Check an Existing Agent

Select option `1` and enter an ERC-8004 Agent ID.

The toolkit displays:

* Network
* Chain ID
* Agent ID
* Owner address
* Metadata URI
* Identity Registry address
* Registration status

Example Testnet agent:

```text
Network:      Arc Testnet
Chain ID:     5042002
Agent ID:     876991
Status:       Registered
```

Example Mainnet agent:

```text
Network:      Arc Mainnet
Chain ID:     5042
Agent ID:     15
Status:       Registered
```

## Register a New Agent

Select option `2`.

The toolkit sends an ERC-8004 registration transaction to the Identity Registry of the selected network and displays:

* Agent ID
* Owner address
* Transaction hash
* Block number
* Explorer transaction link

Each network uses its own ERC-8004 Identity Registry, so Testnet and Mainnet agents remain separate.

## Update Agent Metadata

Select option `3`.

Enter the Agent ID and a new metadata URI.

The toolkit verifies that the connected wallet owns the agent before sending the update transaction.

After confirmation, it displays:

* Agent ID
* Previous metadata URI
* New metadata URI
* Transaction hash
* Block number
* Explorer transaction link

## Check Reputation

Select option `4` and enter an ERC-8004 Agent ID.

The toolkit queries the Reputation Registry for the selected network and displays:

* Agent ID
* Reputation Registry address
* Number of feedback clients
* Reputation feedback data

### Mainnet

Mainnet Agent `15` is registered and can be queried through the Mainnet Reputation Registry.

Current state:

```text
Agent ID:           15
Feedback clients:   0
Reputation feedback: None
```

## Check Validation

Select option `5` and enter an ERC-8004 Agent ID.

Validation functionality is currently available for **Arc Testnet**.

The toolkit can display:

* Agent ID
* Validation Registry address
* Validation requests
* Validator address
* Request hash
* Validation response
* Response tag
* Response hash
* Validation count
* Average response

Mainnet validation is not currently configured because a confirmed Mainnet Validation Registry address is not included in the toolkit yet.

## Submit Validation Request

Select option `6`.

The toolkit allows an agent owner to submit an ERC-8004 validation request on Arc Testnet.

The request includes:

* Agent ID
* Validator address
* Request URI
* Request hash

The toolkit verifies agent ownership before sending the transaction.

### Testnet validation example

The current Testnet agent is Agent `876991`.

```text
Agent ID:       876991
Validator:      0x56509b03e85f3cBAe5bA2190ee99B945D2f0AC36
Request URI:    arc://erc8004/validation/876991
Request Hash:   6a503f9b9a577f7b6ad3f21630ff9b660a2dbe13d458d3cf7b5855df776997c8
Tx Hash:        38f8d416fa52af8eacf462b3f946d548da1c6e95b6118263128914cd5c2d1f80
Block:          59621350
Status:         Confirmed
```

Explorer:

https://testnet.arcscan.app/tx/0x38f8d416fa52af8eacf462b3f946d548da1c6e95b6118263128914cd5c2d1f80

The validation request is recorded onchain and is currently awaiting a validation response.

## Verified Agents

### Arc Testnet

```text
Agent ID:       876991
Owner:          0x4cd95FD3F59E803e4Bc6b3E7D1E6Fc8f23859aB7
Chain ID:       5042002
Status:         Registered
```

### Arc Mainnet

```text
Agent ID:       15
Owner:          0x4cd95FD3F59E803e4Bc6b3E7D1E6Fc8f23859aB7
Chain ID:       5042
Status:         Registered
```

Mainnet registration transaction:

https://explorer.arc.io/tx/0xe48fca2e38a32027b4409759c260be2907df5a7d734105ee242afdd76f999b98

Mainnet metadata update transaction:

https://explorer.arc.io/tx/0xdd75d6f7f4351d06824e7ebf1ea6296cfdc0f50f6dbe90270b0463541ec6dc25

## Agent Metadata

The project includes a `metadata.json` file containing metadata used by the ERC-8004 agents.

The metadata is stored on IPFS and referenced by each agent through its metadata URI.

### Testnet Agent

```text
Agent ID:     876991
Network:      Arc Testnet
```

### Mainnet Agent

```text
Agent ID:     15
Network:      Arc Mainnet
```

The Mainnet metadata was updated successfully onchain after registration.

## Arc Testnet

```text
Chain ID:              5042002
RPC:                   https://rpc.testnet.arc.network
Identity Registry:     0x8004A818BFB912233c491871b3d84c89A494BD9e
Reputation Registry:   0x8004B663056A597Dffe9eCcC1965A193B7388713
Validation Registry:   0x8004Cb1BF31DAf7788923b405b754f57acEB4272
```

Testnet Agent ID: `876991`

## Arc Mainnet

```text
Chain ID:              5042
RPC:                   https://rpc.mainnet.arc.io
Identity Registry:     0x8004A169FB4a3325136EB29fA0ceB6D2e539a432
Reputation Registry:   0x8004BAa17C55a88189AE136b182e5fdA19dE9b63
Validation Registry:   Not configured
```

Mainnet Agent ID: `15`

Mainnet explorer:

https://explorer.arc.io

## ERC-8004

ERC-8004 provides onchain identity infrastructure for AI agents.

This project explores how ERC-8004 agent identities, metadata, reputation and validation can be registered, queried and updated directly from Arc using Python and Web3.

The toolkit keeps Testnet and Mainnet identities separate while using the same application workflow.

## Project Status

The project is an experimental developer tool for exploring ERC-8004 agent identity infrastructure on Arc.

Current functionality includes:

* Agent registration
* Agent identity lookup
* Owner verification
* Metadata URI lookup
* Metadata URI updates
* Network selection
* Testnet reputation lookup
* Mainnet reputation lookup
* Testnet validation lookup
* Testnet validation request submission
* Transaction information
* Testnet and Mainnet explorer verification

Current verified agents:

```text
Arc Testnet  → Agent #876991
Arc Mainnet  → Agent #15
```

The next area of exploration is connecting validation responses and reputation feedback into a more complete ERC-8004 agent identity workflow.

## Security

The private key is loaded from a local `.env` file.

The `.env` file should never be committed to the repository.

Make sure `.env` is included in `.gitignore` before using a private key.

Never share your private key or seed phrase.

## License

MIT License
