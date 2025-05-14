import time
import argparse
import logging
import ctypes
import os
import json
import sys

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
import lib.f81866 as f81866
import lib.f81866_gpio as gpio

logger = logging.getLogger ( __name__ )

# Configure logging settings
def configure_logging ( log_level: str ) -> None :
    # Set the log level based on user input
    level = getattr( logging ,log_level.upper() ,logging.INFO )
    logging.basicConfig( stream=sys.stdout ,level=level )
    logger.setLevel( level )

# Initial GPIO state
val_lastTime = [ 1 ,1 ,1 ,1 ]

# Function to update the shadow with GPIO state
def update_shadow ( ipc_client ,gpio_state ,THING_NAME ,SHADOW_NAME ) -> None :
    """
    Upload the GPIO state to the Shadow's reported state ,
    allowing delta to be received by DIO_map.
    """
    payload = {
        "state": {
            "reported": {
                "gpio_state": gpio_state
            }
        }
    }

    # Update the shadow on the Greengrass core
    ipc_client.update_thing_shadow(
        thing_name=THING_NAME,
        shadow_name=SHADOW_NAME,
        payload=json.dumps(payload)
    )
    logger.info( f"[SHADOW] Reported GPIO state: {gpio_state}" )

def main () -> int :
    global val_lastTime

    # Argument parser for Greengrass component configuration
    parser = argparse.ArgumentParser( description="DIO Greengrass component" )

    parser.add_argument("--thing-name",
                        type=str,
                        required=True,
                        help="Greengrass Thing name")

    parser.add_argument("--shadow-name",
                        type=str,
                        required=True,
                        help="Greengrass shadow name")

    parser.add_argument("--log-level",
                        type=str,
                        default="INFO",
                        help="Log level (default: INFO)")

    # Parse arguments
    args = parser.parse_args()
    configure_logging( args.log_level )

    try:
        # Initialize Greengrass IPC client
        ipc_client = GreengrassCoreIPCClientV2()
    except Exception as e:
        logger.error( "Failed to create Greengrass IPC client: %s" ,e )
        sys.exit( 1 )

    # Retrieve Thing name and Shadow name from arguments
    THING_NAME = args.thing_name
    SHADOW_NAME = args.shadow_name

    logger.info( "Initialize GPIO..." )

    # Set to root permission for GPIO control
    try:
        os.setuid( 0 )
    except Exception as e:
        logger.error( "Error: %s" ,e )
        logger.error( "Error: Cannot set GPIO root permission" )
        return -1

    # Set I/O permissions
    if ctypes.CDLL( "libc.so.6" ).iopl(3) != 0:
        logger.error( "Error: Cannot set I/O permission" )
        return -1

    # Initialize F81866 chip
    if f81866.init() != 0:
        logger.error( "Error: Cannot find F81866 chip" )
        return -1

    # Initialize GPIO
    gpio.init_gpio()

    logger.info( "Get initial GPIO state..." )
    # Retrieve the initial state of the GPIO pins
    val_lastTime = [ gpio.get_gpio_input(i) for i in range(4) ]
    logger.info( "Original state: %s" ,val_lastTime )

    # Report the initial Shadow state
    update_shadow( ipc_client ,val_lastTime ,THING_NAME ,SHADOW_NAME )

    logger.info( "Start monitoring GPIO..." )
    # Start monitoring the GPIO pins for state changes
    while True:
        val = [ gpio.get_gpio_input(i) for i in range(4) ]

        # Check if the GPIO state has changed
        if val != val_lastTime:
            logger.info("GPIO state changed: %s -> %s" ,val_lastTime ,val)
            val_lastTime = val

            # Report the updated Shadow state
            update_shadow( ipc_client ,val ,THING_NAME ,SHADOW_NAME )
            
        time.sleep ( 0.01 )

if __name__ == "__main__":
    main()
