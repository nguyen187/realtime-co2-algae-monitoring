## dbr library:
# com.datastax.spark:spark-cassandra-connector-assembly_2.12:3.2.0   to connect spark with cassandra
# com.microsoft.azure:azure-eventhubs-spark_2.12:2.3.22   to connect spark with event hub
# datastax:spark-cassandra-connector:2.4.0-s_2.11   to connect cassandra
import random
import psutil
import pandas as pd
import os
import socket
import json
import time
from azure.eventhub import EventHubProducerClient, EventData
import time
from datetime import datetime

event_hub_connection_string = ""
event_hub_name = "ramanplsv1"

# Create a producer client to produce and publish events to the event hub.

producer = EventHubProducerClient.from_connection_string(
    conn_str=event_hub_connection_string, eventhub_name=event_hub_name
)
Cust = "ABC"
Project_ID = "ABC-01"
BatchID = 1

data = pd.read_csv("Offline_raman1.csv")
data.insert(0, "Cust", Cust, True)
data.insert(1, "Project_ID", Project_ID, True)
data.insert(2, "BatchID", BatchID, True)

i = 0
df_json = data.apply(lambda x: x.to_json(), axis=1)
N = df_json.shape[0]
Scan = 0
try:
    for i in df_json.index:
        event_data_batch = (
            producer.create_batch()
        )  # Create a batch. You will add events to the batch later.
        print("Start send .......................")
        print()
        # s = json.dumps(df_json[i]) # Convert the reading into a JSON string.
        # print(s)
        Scan += 1
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        event_data_with_time = json.loads(df_json[i])
        event_data_with_time = {"Scan": Scan, **event_data_with_time}
        event_data_with_time = {"Time stream": current_time, **event_data_with_time}

        print(event_data_with_time)
        event_data_batch.add(
            EventData(json.dumps(event_data_with_time))
        )  # Add event data with current time to the batch as the first column.
        producer.send_batch(event_data_batch)
        time.sleep(1)  # delate every 10s
except KeyboardInterrupt:
    # pass
    producer.close()
