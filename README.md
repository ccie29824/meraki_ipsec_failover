# Meraki MX IPsec Failover
Automatic failover of third-party IPsec tunnel using API Based Script.
Meraki MX doesn't support automatic failover of third party ipsec tunnel. If in case tunnel destination IP address is unreachable or down this script will trigger & change the destination ip address to secondary node. 

# Requirements
To use this application you will need:
    Python 3.6+
    Meraki Dashboard
    An account with permissions to push API based changes to network

# Install and Setup
1. Clone the code to local machine.
    git clone https://github.com/ccie29824/meraki_ipsec_failover.git
    cd meraki_ipsec_failover

2. Setup Python Virtual Environment (requires Python 3.7+)
    python3.7 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

3.	Generate API Key from Meraki dashboard to send & receive API via particular account
4.	Configure API Based script for third party ipsec tunnels
5.	Test failover of tunnels using API Script
