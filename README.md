# Arc Agent ID

A Python toolkit for registering, checking and updating AI agent identities on Arc Testnet and Arc Mainnet using ERC-8004.

The project supports separate Testnet and Mainnet agent identities and allows the network to be selected when the toolkit starts.

## Features

* Connect to Arc Testnet or Arc Mainnet
* Select the network interactively
* Check Arc chain ID
* Register a new AI agent
* Check an existing agent
* Read agent owner
* Read agent metadata URI
* Update agent metadata URI
* Verify agent registration
* Check agent reputation
* Check agent validation status on Arc Testnet
* Submit validation requests on Arc Testnet
* Display transaction information
* Use environment variables for private configuration
* Display the correct Arc Explorer transaction link for each network

## Requirements

* Python 3.10+
* Arc Testnet or Mainnet wallet
* Network funds for transaction fees

## Installation

Clone the repository:

```text
git clone https://github.com/Nomad07/arc-agent-id.git
cd arc-agent-id
```

Install dependencies:

```text
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```text
PRIVATE_KEY=your_private_key
NETWORK=testnet
METADATA_URI=ipfs://your_metadata_uri
AGENT_ID=your_agent_id
```

The `NETWORK` variable can be set to:

```text
testnet
```

or:

```text
mainnet
```

The application also allows the network to be selected interactively when it starts.

Never commit `.env` or expose your private key.

## Usage

Run the toolkit:

```text
python main.py
```

The application first asks which Arc network to use:

```text
1. Arc Testnet
2. Arc Mainnet
3. Exit
```

After selecting a network, the ERC-8004 toolkit menu is displayed:

```text
1. Check existing agent
2. Register new agent
3. Update agent metadata
4. Check reputation
5. Check validation
6. Submit validation request
7. Exit
```

## Arc Testnet

The original Testnet agent remains registered and unchanged.

* **Agent ID:** `876991`
* **Chain ID:** `5042002`
* **Owner:** `0x4cd95FD3F59E803e4Bc6b3E7D1E6Fc8f23859aB7`
* **Identity Registry:** `0x8004A818BFB912233c491871b3d84c89A494BD9e`
* **Reputation Registry:** `0x8004B663056A597Dffe9eCcC1965A193B7388713`
* **Validation Registry:** `0x8004Cb1BF31DAf7788923b405b754f57acEB4272`
* **Status:** Registered

### Testnet Metadata

Current Testnet metadata URI:

```text
ipfs://bafkreigmwmty3yc53rcmtmtlanotsr76rviawmxgj4bfn3y673kzdfcgxq
```

### Testnet Validation

Testnet validation is currently supported.

The existing agent has one validation request recorded onchain.

```text
Agent ID:       876991
Validator:      0x56509b03e85f3cBAe5bA2190ee99B945D2f0AC36
Request URI:    arc://erc8004/validation/876991
Request Hash:   6a503f9b9a577f7b6ad3f21630ff9b660a2dbe13d458d3cf7b5855df776997c8
Tx Hash:        38f8d416fa52af8eacf462b3f946d548da1c6e95b6118263128914cd5c2d1f80
Block:          59621350
Status:         Confirmed
```

[View Testnet validation transaction](https://testnet.arcscan.app/tx/0x38f8d416fa52af8eacf462b3f946d548da1c6e95b6118263128914cd5c2d1f80)

The validation request is currently awaiting a validation response.

## Arc Mainnet

A separate ERC-8004 agent was registered on Arc Mainnet after the public Mainnet launch.

* **Agent ID:** `15`
* **Chain ID:** `5042`
* **Owner:** `0x4cd95FD3F59E803e4Bc6b3E7D1E6Fc8f23859aB7`
* **Identity Registry:** `0x8004A169FB4a3325136EB29fA0ceB6D2e539a432`
* **Reputation Registry:** `0x8004BAa17C55a88189AE136b182e5fdA19dE9b63`
* **Status:** Registered

### Mainnet Registration

Agent #15 was registered on Arc Mainnet in block `21231576`.

[View Mainnet registration transaction](https://explorer.arc.io/tx/0xe48fca2e38a32027b4409759c260be2907df5a7d734105ee242afdd76f999b98)

### Mainnet Metadata

The Mainnet agent uses a separate metadata record from the Testnet agent.

Current Mainnet metadata URI:

```text
ipfs://bafkreie4vt7xo2zhnprnamcrkghkg4uhkms7knqz5doafivkk7ramnvexa
```

The Mainnet metadata describes the Arc Mainnet version of the toolkit and links to this repository.

### Mainnet Metadata Update

The metadata for Agent #15 was updated onchain.

[View Mainnet metadata update transaction](https://explorer.arc.io/tx/0xdd75d6f7f4351d06824e7ebf1ea6296cfdc0f50f6dbe90270b0463541ec6dc25)

### Mainnet Reputation

The Mainnet Reputation Registry is configured and readable.

* **Reputation Registry:** `0x8004BAa17C55a88189AE136b182e5fdA19dE9b63`
* **Feedback clients:** `0`

No reputation feedback is currently recorded for Agent #15.

### Mainnet Validation

Mainnet validation is not currently configured because a Validation Registry address has not been confirmed for Arc Mainnet.

Validation checks and validation requests therefore remain available on Arc Testnet only.

## Check an Existing Agent

Select option `1` and enter an ERC-8004 Agent ID.

Example:

```text
Enter Agent ID: 876991
```

The toolkit displays:

* Network
* Chain ID
* Agent ID
* Owner address
* Metadata URI
* Identity Registry address
* Registration status

Example:

```text
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

## Register a New Agent

Select option `2`.

The toolkit sends an ERC-8004 registration transaction to the Identity Registry of the selected Arc network and displays:

* Network
* Chain ID
* Agent ID
* Owner address
* Transaction hash
* Block number
* Arc Explorer transaction link

The project currently has:

* Testnet Agent #876991
* Mainnet Agent #15

## Update Agent Metadata

Select option `3`.

Enter the Agent ID and a new metadata URI.

Example:

```text
Enter Agent ID: 876991
Enter new Metadata URI: ipfs://...
```

The toolkit verifies that the connected wallet owns the agent before sending the update transaction.

After confirmation, it displays:

* Network
* Agent ID
* Previous metadata URI
* New metadata URI
* Transaction hash
* Block number
* Arc Explorer transaction link

## Check Reputation

Select option `4` and enter an ERC-8004 Agent ID.

The toolkit queries the Reputation Registry for the selected network and displays:

* Agent ID
* Reputation Registry address
* Number of feedback clients
* Reputation feedback data

Example for the current Testnet agent:

```text
========================================
ERC-8004 REPUTATION
========================================

Agent ID:     876991
Registry:     0x8004B663056A597Dffe9eCcC1965A193B7388713

Feedback clients: 0

No reputation feedback found.

========================================
```

The current Mainnet agent also has no reputation feedback.

## Check Validation

Select option `5` and enter an ERC-8004 Agent ID.

Validation functionality is currently available on Arc Testnet.

The toolkit queries the ERC-8004 Validation Registry and displays:

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

For the current Testnet agent, one validation request has been recorded onchain.

## Submit Validation Request

Select option `6`.

The toolkit allows the agent owner to submit a validation request to a validator on Arc Testnet.

The request includes:

* Agent ID
* Validator address
* Request URI
* Request hash

The toolkit verifies agent ownership before sending the transaction.

Example request:

```text
Agent ID:       876991
Validator:      0x56509b03e85f3cBAe5bA2190ee99B945D2f0AC36
Request URI:    arc://erc8004/validation/876991
```

The request was successfully submitted to Arc Testnet and confirmed onchain.

## ERC-8004

ERC-8004 provides onchain identity infrastructure for AI agents.

This project explores how ERC-8004 agent identities, metadata, reputation and validation can be registered, queried and updated directly from Arc using Python and Web3.

## Project Status

The project is an experimental developer toolkit for ERC-8004 agent identities on Arc.

Current functionality includes:

* Arc Testnet support
* Arc Mainnet support
* Interactive network selection
* Agent registration
* Agent identity lookup
* Owner verification
* Metadata URI lookup
* Metadata URI updates
* Reputation lookup
* Testnet validation lookup
* Testnet validation request submission
* Transaction information
* Arc Explorer transaction verification

Current registered agents:

```text
Arc Testnet
Agent ID: 876991
Status: Registered

Arc Mainnet
Agent ID: 15
Status: Registered
```

The project remains experimental and is intended for exploring ERC-8004 identity, metadata, reputation and validation capabilities on Arc.

## Project Structure

```text
arc-agent-id/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .env
```

`.env` is local configuration and is excluded from version control.

## Security

The private key is loaded from a local `.env` file.

The `.env` file should never be committed to the repository.

Make sure `.env` is included in `.gitignore` before using a private key.

Never share your private key or seed phrase.

## License

MIT License
