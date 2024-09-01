DOCKER=docker compose -f minio.compose.yml -f spark.compose.yml -f compose.yml


# Setup commands
setup_minio:
	unzip ~/Downloads/kanastra-data-eng-test-datasets.zip -d /tmp/kanastra
	$(DOCKER) up -d mc

setup_kafka:
	echo "Deleting paths"
	sudo rm -r .storage/kafka

	echo "Creting paths"
	mkdir -p .storage/kafka/data

	echo "Grating Write access"
	chmod 777 -R .storage/kafka

# spark commands

cluster_create:
	$(DOCKER) up -d spark spark-worker

cluster_delete:
	$(DOCKER) down spark spark-worker

pipeline:
	$(DOCKER) exec spark spark-submit \
			--packages io.delta:delta-core_2.12:2.3.0 \
			--py-files jobs/dist/functions.py,jobs/dist/etl.py,jobs/dist/trip_staging.py,jobs/dist/vendor_staging.py,jobs/dist/trip_curated.py \
			jobs/dist/pipeline.py


# Others
up_cdc:
	$(DOCKER) up -d mysql zookeeper kafka kafka_connect redpanda_cli

setup_cdc:
	# Debezium MySQL connector
	curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{ "name": "inventory-connector", "config": { "connector.class": "io.debezium.connector.mysql.MySqlConnector", "tasks.max": "1", "database.hostname": "mysql", "database.port": "3306", "database.user": "root", "database.password": "debezium", "database.server.id": "184054", "database.server.name": "mysql", "database.include.list": "inventory", "schema.history.internal.kafka.bootstrap.servers": "kafka:9092", "schema.history.internal.kafka.topic": "dbhistory.inventory", "topic.prefix": "kanastra_"} }'

	# Verify inventory conectors
	curl -H "Accept:application/json" localhost:8083/connectors/

	# Review connectors tasks
	curl -i -X GET -H "Accept:application/json" localhost:8083/connectors/inventory-connector


analytics:
	$(DOCKER) up -d jupyterlab

mysql:
	$(DOCKER) exec mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"'

down:
	$(DOCKER) down