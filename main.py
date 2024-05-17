import socket
import csv
import time
from threading import Thread
import re

# Server settings
HOST = "192.168.137.1" #'192.168.196.104'  # server IP
PORT = 5005              # server port

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind((socket.gethostname(), 8888))
server.listen(1) # listen for up to 2 connections

CSV_COLUMN_NAMES = ['timestamp_mills_ms', 'GX', 'GY', 'GZ', 'AX', 'AY', 'AZ', 'sync', 'timestamp_listener']
print("Server started, waiting for connections...")

# Collect user ID
user_id = input("Enter a user ID: ")
print("waiting for watches to connect...")
# Initialize connections
conn1, addr1 = server.accept()
#conn2, addr2 = server.accept()

# Receive hand identifiers from watches
hand1 = conn1.recv(1024).decode().strip()
#hand2 = conn2.recv(1024).decode().strip()

# Create csv writers for both watches
file1 = open(f"./data/{user_id}_{hand1}.csv", "w", newline='')
#file2 = open(f"./data/{user_id}_{hand2}.csv", "w", newline='')

writer1 = csv.writer(file1)
#writer2 = csv.writer(file2)

# Write column names to CSV files
writer1.writerow(CSV_COLUMN_NAMES)
#writer2.writerow(CSV_COLUMN_NAMES)

#print(f"Connected to watch1 ({hand1}) at {addr1} and watch2 ({hand2}) at {addr2}")
print(f"Connected to watch1 ({hand1}) at {addr1}")

# Await user command to start
input("Press ENTER to start the test")

# Send 'Start' command to both watches
conn1.sendall(b"Start\n")
#conn2.sendall(b"Start\n")

def handle_watch(conn, writer, watch):
    while True:
            # Receive data from watch
            data = conn.recv(1024).decode().strip()
            if not data or data == "":
                # print("No data...")  # connection closed by client
                pass
            elif data == "End":
                print("Connection teriminated!")
                break
            else:
                # If data received, write to csv and send OK
                #print('Received from ' + watch)
                packages = re.split(r'(?<=[sn])', data)
                for i, p in enumerate(packages):
                    if(len(p) > 1):
                        row = p.split(", ")  # Split received data into CSV rows
                        row.append(str(int(time.time() * 1000)))  # Add timestamp in ms
                        writer.writerow(row)
                        print(watch, i, row)
                        print('Length: ', len(row))
                        print(';    --------------------')
                #conn.sendall(b"OK\n")


# Start threads to handle both watches
thread1 = Thread(target=handle_watch, args=(conn1, writer1, '1'))
#thread2 = Thread(target=handle_watch, args=(conn2, writer2, '2'))

thread1.start()
#thread2.start()

# Await user command to end
input("Press ENTER to end the test")

# Close csv files
file1.close()
#file2.close()

# Send 'End' command to both watches
conn1.sendall(b"End\n")
#conn2.sendall(b"End\n")

# Wait for threads to finish
thread1.join()
#thread2.join()

# Close connections
conn1.close()
#conn2.close()



print("Test ended")
