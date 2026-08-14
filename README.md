# Arc Agent ID

A Python toolkit for registering, checking and updating AI agent identities on Arc Testnet using ERC-8004.

## Features

* Connect to Arc Testnet
* Check Arc chain ID
* Register a new AI agent
* Check an existing agent
* Read agent owner
* Read agent metadata URI
* Update agent metadata URI
* Verify agent registration
* Display transaction information
* Use environment variables for private configuration

## Requirements

* Python 3.10+
* Arc Testnet wallet
* Testnet funds for transaction fees

## Installation

Clone the repository:

```
git clone https://github.com/Nomad07/arc-agent-id.git
cd arc-agent-id
```

Install dependencies:

```
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```
RPC_URL=https://rpc.testnet.arc.network
PRIVATE_KEY=your_private_key
METADATA_URI=ipfs://your_metadata_uri
```

Never commit `.env` or expose your private key.

## Usage

Run the toolkit:

```
python main.py
```

The application provides:

```
1. Check existing agent
2. Register new agent
3. Update agent metadata
4. Exit
```

### Check an Existing Agent

Select option `1` and enter an ERC-8004 Agent ID.

Example:

```
Enter Agent ID: 876991
```

The toolkit displays:

* Agent ID
* Owner address
* Metadata URI
* Identity Registry address
* Registration status

### Register a New Agent

Select option `2`.

The toolkit sends an ERC-8004 registration transaction to the Arc Identity Registry and displays:

* Agent ID
* Owner address
* Transaction hash
* Block number
* ArcScan transaction link

### Update Agent Metadata

Select option `3`.

Enter the Agent ID and a new metadata URI.

Example:

```
Enter Agent ID: 876991
Enter new Metadata URI: ipfs://...
```

The toolkit verifies that the connected wallet owns the agent before sending the update transaction.

After confirmation, it displays:

* Agent ID
* Previous metadata URI
* New metadata URI
* Transaction hash
* Block number
* ArcScan transaction link

## Example

Example output for a registered agent:

```
========================================
ERC-8004 AGENT
========================================

Network:      Arc Testnet
Chain ID:     5042002
Agent ID:     876991
Owner:        0x4cd95FD3F59E803e4Bc6b3E7D1E6Fc8f23859aB7
Metadata URI: ipfs://...
Registry:     0x8004A818BFB912233c491871b3d84c89A494BD9e

Status:       Registered

========================================
```

Example metadata update:

```
========================================
METADATA UPDATED
========================================

Agent ID:     876991
Old URI:      ipfs://...
New URI:      ipfs://...
Tx Hash:      0x...
Block:        57009346

========================================
```

## Agent Metadata

The project includes a `metadata.json` file containing the metadata used by the registered ERC-8004 agent.

The metadata is stored on IPFS and referenced by the agent through its metadata URI.

Current testnet agent:

```
Agent ID: 876991
Owner: 0x4cd95FD3F59E803e4Bc6b3E7D1E6Fc8f23859aB7
```

## Arc Testnet

The toolkit is currently designed for Arc Testnet.

* Chain ID: `5042002`
* RPC: `https://rpc.testnet.arc.network`
* Identity Registry: `0x8004A818BFB912233c491871b3d84c89A494BD9e`

## ERC-8004

ERC-8004 provides onchain identity infrastructure for AI agents.

This project explores how ERC-8004 agent identities can be registered, queried and updated directly from Arc using Python and Web3.

## Project Status

The project is an experimental developer tool built on Arc Testnet.

Current functionality includes:

* Agent registration
* Agent identity lookup
* Owner verification
* Metadata URI lookup
* Metadata URI updates
* Transaction information

Future versions may explore reputation and validation features.

## Security

The private key is loaded from a local `.env` file.

The `.env` file should never be committed to the repository.

Make sure `.env` is included in `.gitignore` before using a private key.

Never share your private key or seed phrase.

## License

MIT License
