from gr4vy import Gr4vyClientWithBaseUrl, Gr4vyClient
from gr4vy.gr4vy_client import Gr4vyError
import json
import csv

def run_report(gr4vy_id, environment, private_key, log_file, output_file,):
  client = Gr4vyClient(gr4vy_id, private_key, environment=environment)
  with open(log_file, 'r') as f:
    data = json.load(f)
    with open(output_file, 'w', newline='') as file:
      fieldnames = ['transaction_id', 'buyer_id', 'cardholderInfo', 'transStatus', 'messageType', 'transStatusReason']
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      for log in data:
          jsonPayload = log.get('jsonPayload')
          transaction_id = jsonPayload.get('transaction_id')
          response = jsonPayload.get('response')
          try:
            buyer = client.get_transaction(transaction_id).get('buyer')
            buyer_id = buyer.get('id')
          except Gr4vyError as e: 
            continue
          writer.writerow({"transaction_id": transaction_id, "buyer_id": buyer_id, "cardholderInfo": response.get('cardholderInfo'), "transStatus": response.get('transStatus'),"messageType": response.get('messageType'),"transStatusReason":response.get('transStatusReason')})