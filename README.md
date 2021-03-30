# Meraki MX IPsec Failover
Automatic failover of third-party IPsec tunnel using API Based Script.
Meraki MX doesn't support automatic failover of third party ipsec tunnel. If in case tunnel destination IP address is unreachable or down this script will trigger & change the destination ip address to secondary node. 

# Requirements
To use this application you will need:
    Python 3.6+
    Meraki Dashboard
    An account with permissions to push API based changes to network

# Install and Setup
1.	Install Python on windows or linux machine
2.	Generate API Key from Meraki dashboard to send & receive API via particular account
3.	Configure API Based script for third party ipsec tunnels
4.	Test failover of tunnels using API Script
