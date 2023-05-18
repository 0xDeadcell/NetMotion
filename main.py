import ipaddress
import random
import csv

# Define the subnet groups
subnet_groups = [
    ipaddress.ip_network('10.0.0.0/8'),
    ipaddress.ip_network('192.168.0.0/16'),
    ipaddress.ip_network('172.16.0.0/12'),
    ipaddress.ip_network('10.192.0.0/10'),
    ipaddress.ip_network('192.168.192.0/18'),
    ipaddress.ip_network('172.18.0.0/15'),
    ipaddress.ip_network('10.128.0.0/9'),
    ipaddress.ip_network('192.168.240.0/20'),
    ipaddress.ip_network('172.42.0.0/15'),
    ipaddress.ip_network('10.16.0.0/12'),
    ipaddress.ip_network('192.168.224.0/19'),
    ipaddress.ip_network('172.66.0.0/15')
]

# Create a dictionary to store IP addresses for each subnet group
ip_addresses = {}

# Generate IP addresses for each subnet group
for subnet_group in subnet_groups:
    ip_addresses[subnet_group] = []

    # Get the available IP range, excluding the first 5 and the last 10 addresses
    available_ips = list(subnet_group.hosts())[5:-10]

    # Generate random IP addresses within the available range
    num_addresses = random.randint(100, 500)
    for _ in range(num_addresses):
        random_ip = random.choice(available_ips)
        ip_addresses[subnet_group].append(str(random_ip))
        available_ips.remove(random_ip)

# Write the IP addresses to a CSV file
with open('ip_addresses.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the subnet groups as column headers
    writer.writerow([str(subnet_group) for subnet_group in subnet_groups])

    # Write the IP addresses row by row under each column
    for i in range(max(len(ip_addresses[subnet_group]) for subnet_group in subnet_groups)):
        row = [ip_addresses[subnet_group][i] if i < len(ip_addresses[subnet_group]) else "" for subnet_group in subnet_groups]
        writer.writerow(row)

print("IP addresses generated and saved to ip_addresses.csv.")
