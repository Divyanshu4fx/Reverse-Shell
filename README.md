# Reverse Remote Shell Access Tool

This repository contains code for a simple remote shell access tool implemented in Python using sockets. The tool consists of two scripts, one for the server-side and one for the client-side.

## Server Side
- The server script (`server.py`) creates a socket and listens for incoming connections.
- Upon connection, it accepts commands from the client and executes them on the server's machine.
- The server can handle basic shell commands and provides feedback to the client.

## Client Side
- The client script (`client.py`) connects to the server using the specified host and port.
- Once connected, it sends commands to the server and receives the output of these commands.
- The client allows navigation of directories (`cd` command) and execution of shell commands.
- It provides a simple shell interface for interacting with the server remotely.

## Usage
1. Run the client script on the machine you want to control remotely.
2. Run the server script on the machine from which you want to control the client.
3. Enter commands on the server-side terminal to execute them remotely on the client.
4. Use `quit` command to exit the program.

## Note
- This tool provides a basic framework for remote shell access and may require modifications for specific use cases.
- Ensure proper security measures are in place when using this tool over a network, as it involves executing commands remotely.
