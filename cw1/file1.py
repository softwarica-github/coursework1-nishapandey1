import socket

def ip_host(host, port=80):
    try:
        sock = socket.create_connection((host, port), timeout=1)
        return True
    except OSError:
        return False

def ping_sweep(network):
    for ip in range (1, 255):
        host = f"{network}.{ip}"
        if ip_host(host):
            print(f"Host {host} is alive")

def scan_ports(host, ports):
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                result = s.connect_ex((host, int(port)))
                if result == 0:
                    print(f"Port {port} is open")
                else:
                    print(f"Port {port} is closed")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    network ="192.168.1"

    #check if the network is alive
    if ip_host(network):
        print(f"Network {network}.0 is alive")
        #perform a ping sweep
        ping_sweep(network)

        #scan ports on a target host
        host = f"{network}.10"
        if ip_host(host):
            print(f"Host {host} is alive")
            scan_ports(host, [80, 443, 135, 139, 445])