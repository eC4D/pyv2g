# pyPnC

# Open ISO15118-2 Implementation

This project implements the communication interface between Electric Vehicle Supply Equipment (EVSE) and Electric Vehicles (EV), facilitating the management of the charging process in compliance with ISO15118-2. It consists of two main components: the Supply Equipment Communication Controller (SECC) and the Electric Vehicle Communication Controller (EVCC), which work together to ensure secure, efficient transactions during the charging process.

## Features

- **SECC Server**: Manages and controls the EVSE's charging operations through communication with the EV.
- **EVCC Client**: Handles the EV's communication, initiating requests, and responding to the EVSE's commands.
- **Encoding/Decoding Utilities**: Provides tools for encoding and decoding messages using the Efficient XML Interchange (EXI) format for optimized communication.
- **Python Simulation**: A Python-based simulation of the charging communication process for development and testing.

## Target Audience

This project is designed for developers, researchers, and engineers in the electric vehicle infrastructure and smart grid technology sectors. It serves as a foundational implementation for EV-EVSE communications and can be extended for specific applications.

## Prerequisites

- Python 3.7 or higher
- A basic understanding of Python programming and Docker environments

## Installation

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/eC4D/pyv2g.git
```
Navigate to the project directory:

```bash
cd pyv2g
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

## Starting the Server (SECC)
```bash
python -m secc.secc
```

## Starting the Client (EVCC)
```bash
python -m evcc.evcc
```





