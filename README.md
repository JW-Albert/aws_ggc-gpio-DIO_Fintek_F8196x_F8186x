# AWS Greengrass GPIO Component for Fintek F81866/F81966

This project implements a Greengrass component for monitoring and controlling GPIO pins on Fintek F81866/F81966 chips. It provides real-time GPIO state monitoring and updates the AWS IoT Device Shadow with the current state.

## Features

- Real-time GPIO state monitoring
- AWS IoT Device Shadow integration
- Support for Fintek F81866/F81966 chips
- Configurable logging levels
- Automatic state synchronization

## Prerequisites

- AWS Greengrass Core v2
- Python 3.7 or later
- Fintek F81866/F81966 chip
- Root permissions for GPIO access

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The component requires the following parameters:

- `--thing-name`: AWS IoT Thing name
- `--shadow-name`: AWS IoT Shadow name
- `--log-level`: Logging level (default: INFO)

## Usage

The component can be deployed as a Greengrass component. It will:

1. Initialize the GPIO pins
2. Monitor GPIO state changes
3. Update the AWS IoT Device Shadow with current states
4. Provide real-time logging of state changes

## Development

The project structure:
```
.
├── src/
│   ├── main.py          # Main component logic
│   ├── justRead.py      # GPIO reading utilities
│   └── lib/             # Fintek chip libraries
├── recipe.yaml         # Greengrass component recipe
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## License

[Add your license information here]
