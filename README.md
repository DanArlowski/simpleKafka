run
```bash
oc new-project myproject
oc apply -f deployment/strimzi.yaml
oc apply -f deployment/kafka-persistent-single.yaml
oc apply -f deployment/users.yaml
oc apply -f deployment/producer.yaml
oc apply -f deployment/consumer.yaml

```