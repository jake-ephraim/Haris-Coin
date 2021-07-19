# Haris Coin: A Transparent Centralized Electronic Cash System
## Abstract:
This electronic cash will try to solve governmental issues towards crypto currency as they cannot be regulated or accounted for, while still maintaining the blockchain’s open ledger and a level of anonymity. Most attributes of cyptocurrency are maintained except the network is partially centralized, such that, the “mother node” with power to distribute the coin from her reserves is control by a centralized body unlike other crypto currencies which can be mined to put the coin in circulation. Like bitcoin, the network processes signed transaction by hashing them into an ongoing chain of hash-based proof-of-work, forming a record that cannot be changed without redoing the proof-of-work. Nodes can leave and rejoin the network at will, accepting the Mothers node Proof-of-work chain as proof of what happened while they were away.
## Introduction:
Haris Coin is a transparent digital currency based on blockchain technology in which everyone in the network has access to the blockchain and all its data. It is a network of three (3) different types of nodes namely: 
* Mother Node
* First Node
* Child Node.

![Haris Network](data/HRC-Network.png)

All communicate independently and through the mother node which is maintained by a central authority. The mother node is able to broadcast messages to all nodes as well as to release the coins from her reserves into circulation. The mother node is the only one able to add first nodes to her network.                                                                                                                         
The Fist node's can be controlled by registered individuals or institutions to process and add transactions to the block. Child node's are the users of the network, as they can only make transactions and access the block chain. Both the parent and mother node must have a child node, in other to be able to hold or transfer the coin. Therefore, the network in a way is actually a network of child node's. The first and child nodes are anonymous in the network and only the mother node is known. All transactions go the mother node pool where the first node compete to authorise the transaction and add it to the blockchain.

## Transactions
A child node transfer the coin to the next child node by signing the transaction details with the public key of the next child node, so that the next child node can verify the transaction with it's private key. The transactions block can be added to the chain by hashing the previous hash and the current block with a certain difficulty. The block is then broadcasted to the mother node and first nodes for verification before being added to the chain. The transaction with next transaction id is considered first and if the next transaction's id does not match the next, it is negleted.
