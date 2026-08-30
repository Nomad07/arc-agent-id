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
* Check agent reputation
* Check agent validation status
* Submit validation requests
* Display transaction information
* Use environment variables for private configuration

## Requirements

* Python 3.10+
* Arc Testnet wallet
* Testnet funds for transaction fees

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
RPC_URL=https://rpc.testnet.arc.network
PRIVATE_KEY=your_private_key
METADATA_URI=ipfs://your_metadata_uri
AGENT_ID=876991
```

Never commit `.env` or expose your private key.

## Usage

Run the toolkit:

```text
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

### Check an Existing Agent

Select option `1` and enter an ERC-8004 Agent ID.

Example:

```text
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

```text
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

### Check Reputation

Select option `4` and enter an ERC-8004 Agent ID.

The toolkit queries the ERC-8004 Reputation Registry and displays:

* Agent ID
* Reputation Registry address
* Number of feedback clients
* Reputation feedback data

Example for the current testnet agent:

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

The agent currently has no reputation feedback.

### Check Validation

Select option `5` and enter an ERC-8004 Agent ID.

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

For the current agent, a validation request has been recorded onchain.

### Submit Validation Request

Select option `6`.

The toolkit allows the agent owner to submit a validation request to a validator.

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

The request was successfully submitted to Arc Testnet.

```text
Agent ID:       876991
Validator:      0x56509b03e85f3cBAe5bA2190ee99B945D2f0AC36
Request URI:    arc://erc8004/validation/876991
Request Hash:   6a503f9b9a577f7b6ad3f21630ff9b660a2dbe13d458d3cf7b5855df776997c8
Tx Hash:        38f8d416fa52af8eacf462b3f946d548da1c6e95b6118263128914cd5c2d1f80
Block:          59621350
Status:         Confirmed
```

The validation request can be viewed on ArcScan:

https://testnet.arcscan.app/tx/38f8d416fa52af8eacf462b3f946d548da1c6e95b6118263128914cd5c2d1f80

The request is currently awaiting a validation response.

## Example

Example output for a registered agent:

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

Example validation status:

```text
========================================
ERC-8004 VALIDATION
========================================

Agent ID:     876991
Registry:     0x8004Cb1BF31DAf7788923b405b754f57acEB4272

Validation requests: 1

Validation 1
Request hash: 6a503f9b9a577f7b6ad3f21630ff9b660a2dbe13d458d3cf7b5855df776997c8
Validator:    0x56509b03e85f3cBAe5bA2190ee99B945D2f0AC36
Agent ID:     876991
Response:     0/100
Tag:          -
Last update:  1788101556
Response hash: 0000000000000000000000000000000000000000000000000000000000000000

Validation count:  0
Average response: 0/100

========================================
```

The validation request has been recorded onchain, but no validation response has been submitted yet.

## Agent Metadata

The project includes a `metadata.json` file containing the metadata used by the registered ERC-8004 agent.

The metadata is stored on IPFS and referenced by the agent through its metadata URI.

Current testnet agent:

```text
Agent ID: 876991
Owner: 0x4cd95FD3F59E803e4Bc6b3E7D1E6Fc8f23859aB7
```

## Arc Testnet

The toolkit is currently designed for Arc Testnet.

* Chain ID: `5042002`
* RPC: `https://rpc.testnet.arc.network`
* Identity Registry: `0x8004A818BFB912233c491871b3d84c89A494BD9e`
* Reputation Registry: `0x8004B663056A597Dffe9eCcC1965A193B7388713`
* Validation Registry: `0x8004Cb1BF31DAf7788923b405b754f57acEB4272`

## ERC-8004

ERC-8004 provides onchain identity infrastructure for AI agents.

This project explores how ERC-8004 agent identities, metadata, reputation and validation can be registered, queried and updated directly from Arc using Python and Web3.

## Project Status

The project is an experimental developer tool built on Arc Testnet.

Current functionality includes:

* Agent registration
* Agent identity lookup
* Owner verification
* Metadata URI lookup
* Metadata URI updates
* Reputation lookup
* Validation lookup
* Validation request submission
* Transaction information
* ArcScan transaction verification

The project is still in an experimental stage. Next I want to explore how metadata, reputation and validation can be integrated into a more complete toolkit for AI agents on Arc.

## Security

The private key is loaded from a local `.env` file.

The `.env` file should never be committed to the repository.

Make sure `.env` is included in `.gitignore` before using a private key.

Never share your private key or seed phrase.

## License

MIT License
