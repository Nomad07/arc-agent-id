# Arc Agent ID

A Python toolkit for interacting with AI agent identities on Arc using ERC-8004.

The project supports both **Arc Mainnet** and **Arc Testnet** with separate agent identities and network-specific registries.

## Features

* Connect to Arc Mainnet or Arc Testnet
* Switch between networks
* Register ERC-8004 agents
* Check existing Agent IDs
* Read agent owners
* Read agent metadata URIs
* Update agent metadata
* Check reputation
* Check validation requests
* Submit validation requests on Testnet
* Display transaction and block information

## Requirements

* Python 3.10+
* An Arc wallet
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
PRIVATE_KEY=your_private_key
METADATA_URI=ipfs://your_metadata_uri
AGENT_ID=
```

The network can be selected from the application menu.

Never commit `.env` or expose your private key.

## Usage

Run the toolkit:

```bash
python main.py
```

The application starts with network selection:

```text
1. Arc Mainnet
2. Arc Testnet
3. Exit
```

After selecting a network, the toolkit provides:

```text
1. Check existing agent
2. Register new agent
3. Update agent metadata
4. Check reputation
5. Check validation
6. Submit validation request
7. Exit
```

## Arc Mainnet

A separate ERC-8004 agent was registered on Arc Mainnet after the public Mainnet launch.

```text
Agent ID: 15
Chain ID: 5042
```

The Mainnet agent has its own identity and metadata and is separate from the Testnet agent.

### Mainnet capabilities

* Agent registration
* Agent ownership checks
* Metadata updates
* Reputation queries

The Mainnet agent was registered successfully and its metadata was later updated onchain.

Mainnet RPC:

```text
https://rpc.mainnet.arc.io
```

Mainnet Identity Registry:

```text
0x8004A169FB4a3325136EB29fA0ceB6D2e539a432
```

Mainnet Reputation Registry:

```text
0x8004BAa17C55a88189AE136b182e5fdA19dE9b63
```

Mainnet validation is not currently configured because a confirmed Mainnet Validation Registry address is not included in the toolkit.

Mainnet explorer:

https://explorer.arc.io

## Arc Testnet

The original ERC-8004 agent is deployed on Arc Testnet.

```text
Agent ID: 876991
Chain ID: 5042002
```

The Testnet agent is used for experimenting with ERC-8004 identity, metadata, reputation and validation.

### Testnet capabilities

* Agent registration
* Agent ownership checks
* Metadata updates
* Reputation queries
* Validation queries
* Validation request submission

A validation request has been successfully submitted for Agent `876991` and recorded onchain.

Testnet RPC:

```text
https://rpc.testnet.arc.network
```

Testnet Identity Registry:

```text
0x8004A818BFB912233c491871b3d84c89A494BD9e
```

Testnet Reputation Registry:

```text
0x8004B663056A597Dffe9eCcC1965A193B7388713
```

Testnet Validation Registry:

```text
0x8004Cb1BF31DAf7788923b405b754f57acEB4272
```

## ERC-8004

ERC-8004 provides onchain identity infrastructure for AI agents.

This project explores how agent identities, metadata, reputation and validation can be managed through ERC-8004 on Arc.

The toolkit keeps Mainnet and Testnet agents separate while providing the same core workflow across both networks.

## Project Status

Current verified agents:

```text
Arc Mainnet → Agent #15
Arc Testnet  → Agent #876991
```

The Mainnet agent is registered and its metadata has been successfully updated onchain.

The Testnet agent remains active with existing validation functionality.

The next area of exploration is connecting validation responses and reputation feedback into a more complete ERC-8004 agent identity workflow.

## Security

The private key is loaded from a local `.env` file.

The `.env` file should never be committed to the repository.

Never share your private key or seed phrase.

## License

MIT License
