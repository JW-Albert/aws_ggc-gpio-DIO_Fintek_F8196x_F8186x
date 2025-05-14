#!/bin/bash
gdk component build
sudo /greengrass/v2/bin/greengrass-cli deployment create \
  --recipeDir $PWD/greengrass-build/recipes \
  --artifactDir $PWD/greengrass-build/artifacts \
  --merge "imcloud.imphm.gpio.DIO_Fintek_F8196x_F8186x=1.0.0"