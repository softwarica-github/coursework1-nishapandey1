import tkinter as tk
from tkinter import messagebox
import socket

def close():
    root.destroy()

def ip_host(host, port=80):
    try:
        sock = socket.create_connection((host, port), timeout=1)
        return True
    except OSError:
        return False

def ping_sweep():
    network = network_entry.get()
    if not network or "." not in network or len(network.split(".")) != 3:
        messagebox.showerror("Error", "Invalid network address")
        return

    for ip in range(1, 255):
        host = f"{network}.{ip}"
        if ip_host(host):
            hosts_alive_list.insert(tk.END, host)

def scan_ports():
    host = host_entry.get()
    if not host or "." not in host or len(host.split(".")) != 4:
        messagebox.showerror("Error", "Invalid host address")
        return

    ports = list(map(int, port_entry.get().split(",")))
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                result = s.connect_ex((host, int(port)))
                if result == 0:
                    ports_open_list.insert(tk.END, f"Port {port} is open")
                else:
                    ports_closed_list.insert(tk.END, f"Port {port} is closed")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

root = tk.Tk()
root.title("Network Enumeration Tool")
root.configure(bg='steel blue')

tk.Label(root, text="Network address (e.g., 192.168.1):",font=("Times New Roman",16),bg='steelblue', padx=5, pady=5).grid(row=0, column=0)
network_entry = tk.Entry(root, width=20,font=("Times New Roman",13))
network_entry.grid(row=0, column=1)

tk.Label(root, text="Host address (e.g., 192.168.1.10):",font=("Times New Roman",16),bg='steel blue', padx=5, pady=5).grid(row=1, column=0)
host_entry = tk.Entry(root, width=20,font=("Times New Roman",13))
host_entry.grid(row=1, column=1)

tk.Label(root, text="Ports (comma-separated, e.g., 1,80,443):",font=("Times New Roman",16),bg='steel blue', padx=5, pady=5).grid(row=2, column=0)
port_entry = tk.Entry(root, width=20, font=("Times New Roman",13))
port_entry.grid(row=2, column=1)

tk.Button(root, text="Ping Sweep", font=("Times New Roman",14),background="lightgreen", foreground="white",command=ping_sweep, padx=5, pady=5).grid(row=3, column=0)
tk.Button(root, text="Scan Ports",font=("Times New Roman",14), background="lightgreen", foreground="white",command=scan_ports, padx=5, pady=5).grid(row=3, column=1)

tk.Label(root, text="Alive hosts:", font=("Times New Roman",13),padx=5, pady=5).grid(row=4, column=0)
hosts_alive_list = tk.Listbox(root, height=10, bg="lightgray")
hosts_alive_list.grid(row=5, column=0, columnspan=2)

tk.Label(root, text="Open ports:", font=("Times New Roman",13),padx=5, pady=5).grid(row=6, column=0)
ports_open_list = tk.Listbox(root, height=10, bg="lightgray")
ports_open_list.grid(row=7, column=0, columnspan=2)

tk.Label(root, text="Closed ports:",font=("Times New Roman",13), padx=5, pady=5).grid(row=6, column=7)
ports_closed_list = tk.Listbox(root, height=10, bg="lightgray")
ports_closed_list.grid(row=7, column=7, columnspan=2)

tk.Button(root, text="Close",font=("Times New Roman",14), background="red", foreground="white",command=root.destroy, padx=5, pady=5).grid(row=20, column=1)

root.mainloop ()