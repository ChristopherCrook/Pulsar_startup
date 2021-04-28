# Base Experiment (MQ)

This experiment is an extension of the [Base experiment](./Base.md) that is specific to MQ technologies.

## Qualitative Data

These metrics are inspired by Zhuangwei Kang's presentation he shared with us. Fill in with information you discover about your chosen MQ.

| Metric | Value |
| --- | --- |
| Centricity (data-centric or message-centric) ||
| Connection (machine-to-machine or point-to-point) | |
| Underlying Architecture (decentralized or hub-and-spoke) | At the highest level, a Pulsar instance is composed of one or more Pulsar clusters. Clusters within an instance can replicate data amongst themselves.  [More information](https://pulsar.apache.org/docs/en/concepts-architecture-overview/)  |
| Protocol | Pulsar uses a custom binary protocol for communications between producers/consumers and brokers. This protocol is designed to support required features, such as acknowledgements and flow control, while ensuring maximum transport and implementation efficiency [More information](http://pulsar.apache.org/docs/en/develop-binary-protocol/#:~:text=Pulsar%20uses%20a%20custom%20binary,exchange%20commands%20with%20each%20other.) |
| Transport(s) | By default, Apache Pulsar clients communicate with the Apache Pulsar service in plain text. This means that all data is sent in the clear. You can use TLS to encrypt this traffic to protect the traffic from the snooping of a man-in-the-middle attacker.  [More information](https://pulsar.apache.org/docs/en/security-tls-transport/)|
| Data Serialization | Type safety is extremely important in any application built around a message bus like Pulsar.
Producers and consumers need some kind of mechanism for coordinating types at the topic level to avoid various potential problems arise. For example, serialization and deserialization issues. When a schema is enabled, Pulsar does parse data, it takes bytes as inputs and sends bytes as outputs.  [More information](https://pulsar.apache.org/docs/en/schema-get-started/) |
| Supports Queuing | Yes. Pulsar is a great choice for a message queue because it was built with persistent message storage in mind it offers automatic load balancing across consumers for messages on a topic (or custom load balancing if you wish)  [More information](https://pulsar.apache.org/docs/en/cookbooks-message-queue/) |
| Data Type Representation | Pulsar schema is defined in a data structure called SchemaInfo.The SchemaInfo is stored and enforced on a per-topic basis and cannot be stored at the namespace or tenant level.  [More information](https://pulsar.apache.org/docs/en/schema-understand/)|
| QoS Parameters | |
| Supports Dynamic Discovery | |
| Communication Patterns | Publish-Subscribe Pattern  [More information](https://pulsar.apache.org/docs/en/concepts-messaging/) |
| Abstraction Layer | |
| Up-front Complexity | |
| Large Implementations | |

