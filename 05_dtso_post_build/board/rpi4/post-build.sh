#!/bin/sh

# Ensure the target directory exists
mkdir -p ${BINARIES_DIR}/rpi-firmware/overlays

# Move all compiled overlays from output/images/ to the overlays/ dir
cp ${BINARIES_DIR}/*.dtbo ${BINARIES_DIR}/rpi-firmware/overlays/

