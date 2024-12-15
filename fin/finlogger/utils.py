import re

def extract_mpesa_details(message):
    transactions = []

    
    details = {}

    # Transaction ID
    tx_id_match = re.search(r'^[A-Z0-9]+', message)
    if tx_id_match:
        details['Transaction ID'] = tx_id_match.group()

    # Amount
    amount_match = re.search(r'Ksh([0-9,]+\.\d{2})', message)
    if amount_match:
        details['Amount'] = amount_match.group(1).replace(",", "")

    # Recipient/Sender
    if "sent to" in message:
        recipient_match = re.search(r'sent to ([A-Za-z\s]+\d+)', message)
        if recipient_match:
            details['Recipient'] = recipient_match.group(1).strip()
            details['type_of_transaction'] = 'sent'

    if "paid to" in message:
        recipient_match = re.search(r'paid to ([A-Za-z\s]+)', message)
        print(recipient_match)
        if recipient_match:
            details['Recipient'] = recipient_match.group(1).strip()
            details['type_of_transaction'] = 'paid'
    elif "received" in message:
        sender_match = re.search(r'from ([A-Za-z\s]+\d+|CO-OP BANK \d+)', message)
        if sender_match:
            details['Sender'] = sender_match.group(1).strip()
            details['type_of_transaction'] = 'received'

    # Date and Time
    date_time_match = re.search(r'on (\d+/\d+/\d{2}) at ([\d:]+\s[AP]M)', message)
    if date_time_match:
        details['Date'] = date_time_match.group(1)
        details['Time'] = date_time_match.group(2)

    # New M-PESA balance
    balance_match = re.search(r'New M-PESA balance is Ksh([0-9,]+\.\d{2})', message)
    if balance_match:
        details['New Balance'] = balance_match.group(1).replace(",", "")

    # Transaction cost
    cost_match = re.search(r'Transaction cost, Ksh([0-9,]+\.\d{2})', message)
    if cost_match:
        details['Transaction Cost'] = cost_match.group(1).replace(",", "")

    # Amount you can transact
    limit_match = re.search(r'Amount you can transact within the day is ([0-9,]+\.\d{2})', message)
    if limit_match:
        details['Daily Transaction Limit'] = limit_match.group(1).replace(",", "")

    transactions.append(details)

    return details

# Sample messages
mpesa_messages = [
    "SJ94J7IV2W Confirmed. Ksh2,000.00 sent to caroline  wanjira 0706315010 on 9/10/24 at 9:18 PM. New M-PESA balance is Ksh35,061.37. Transaction cost, Ksh33.00. Amount you can transact within the day is 488,710.00. Thank you for being our valued customer, we appreciate you.",
    "SJ97J7IV2F Confirmed. Ksh2,500.00 sent to eric  ndururi 0708472693 on 9/10/24 at 9:18 PM. New M-PESA balance is Ksh38,107.37. Transaction cost, Ksh33.00. Amount you can transact within the day is 491,710.00. Thank you for being our valued customer, we appreciate you.",
    "SJ71B959XT Confirmed. Ksh100.00 paid to STANLEY MATHENGE WAIRIMU. on 7/10/24 at 11:03 PM.New M-PESA balance is Ksh22,898.87. Transaction cost, Ksh0.00. Amount you can transact within the day is 497,545.00. Download new M-PESA app on http://bit.ly/mpesappsm & get 500MB FREE data.",
    "SJ91IFDAQJ Confirmed.You have received Ksh25,000.00 from CO-OP BANK 149444 on 9/10/24 at 6:57 PM New M-PESA balance is Ksh41,992.37.  Separate personal and business funds through Pochi la Biashara on *334#.",
    "SJ91IFDAQJ Confirmed.You have received Ksh2,000.00 from James Njuguna on 9/10/24 at 6:57 PM New M-PESA balance is Ksh41,992.37.  Separate personal and business funds through Pochi la Biashara on *334#.",
    "SJ91IFDAQJ Confirmed.You have received Ksh5,000.00 from eric ndngi on 9/10/24 at 6:57 PM New M-PESA balance is Ksh41,992.37.  Separate personal and business funds through Pochi la Biashara on *334#."

]


# Extract details
# parsed_transactions = extract_mpesa_details(mpesa_messages)

# Display extracted details
# for i, transaction in enumerate(parsed_transactions, 1):
#     print(f"Transaction {i}:")
#     for key, value in transaction.items():
#         print(f"  {key}: {value}")
#     print()