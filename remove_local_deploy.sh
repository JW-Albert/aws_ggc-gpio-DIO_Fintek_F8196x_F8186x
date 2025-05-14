#!/bin/bash
sudo /greengrass/v2/bin/greengrass-cli \
    --ggcRootPath /greengrass/v2 deployment create \
    --remove "imcloud.imphm.gpio.DIO_Fintek_F8196x_F8186x"