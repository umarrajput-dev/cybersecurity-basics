# Project 1: Basic Firewall Simulator

# Define blocked IP and ports
blocked_ip = "192.168.1.50"
restricted_ports = [22, 23, 445]

# Get connection details from user
ip = input("Enter incoming IP: ").strip()
port_input = input("Enter Port: ").strip()

# Convert port to integer (Typecasting)
try:
    port = int(port_input)
except ValueError:
    print("[ERROR] Port must be a valid number!")
    exit()

# Firewall logic
print("\nScanning packet...")

if ip == blocked_ip:
    print(f"[BLOCKED] Connection from {ip} is denied. IP is blacklisted.")
elif port in restricted_ports:
    print(f"[BLOCKED] Port {port} is restricted. Connection denied.")
else:
    print(f"[ALLOWED] Connection from {ip} on port {port} is successful.")
