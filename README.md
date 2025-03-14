# br-by-ex

Buildroot by example. A few basic implementations of `buildroot`, showing some simple features and implementations that the working embedded Linux engineer might care about. 

Examples include:

* a basic out-of-tree project
* how to customize the Linux kernel, and store customizations 
* how to customize the device tree
* adding files to the rootfs using overlays
* compiling and installing a custom C application 
* installing a Python runtime to the target
* adding extlinux.conf support, for booting a kernel/DTB in the rootfs
* an impementation of `swupdate`, with A/B dual-copy software updates initated by a user
* an impementation of `swupdate` with signed builds, with updates initiated by a user 

# Setup

1. Clone this repository
2. Navigate into this repo, and run `git submodule --init`.
3. Make an empty directory called `tools/` inside your repo.
4. Run `make -C buildroot raspberrypi4_defconfig`
5. Run `make -C buildroot sdk`. (This will take a while.)
6. When complete, copy the `tar.gz` toolchain file into `tools/` from `buildroot/output/images/`

# Building an Example Project

All projects are structured as out-of-tree buildroot projects. To build a specific project, set `BR2_EXTERNAL` to the specific directory, load the defconfig, and then make.

For example, to build the project in `09-swupdate`, run:

```
make $BR2_EXTERNAL=$PWD/09-swupdate -C buildroot 09_swupdate_defconfig
make $BR2_EXTERNAL=$PWD/09-swupdate -C buildroot
```

Note that, if you've built one of the other projects already, you may wish to run `make -C buildroot clean` before building with a new defconfig. 

This will make your build take longer, but it also ensures your new example won't build with unexpected artifacts that may mess with normal operation. 

# Project Index

Here's an index of what this repository contains. Click down a level to see project-specific READMEs. 

- `01-basic`: simple out of tree buildroot project, with a package added
- `02-rfs-overlay`: very simple rootfs overlay, with test file added
- `03-i2c-support`: add support for I2C, and also a device driver for a time-of-flight sensor
- `04-kernel-fragment`: storing kernel customizations for our I2C sensor
- `05-dtso-post-build`: telling the kernel how to interact with our sensor; plus, some shell scripts to properly load the overlay

# Future Work

Here's a roadmap of what we plan to cover in future projects. These will move up to the Project Index as they are completed.  

- `custom-app`: basic C application that's compiled and installed to target system on `make`
- `python`: install Python on target, along with a basic script, plus a package or two
- `spi-support`: get SPI up and running 
- `extlinux`: using a modern `extlinux.conf` to bundle the Kernel and DTB within the rootfs
- `swupdate`: implement software updates using `swupdate`
- `ab-updates`: make software updates safer with dual copy rootfs'es 
- `rfs-encrypt`: encrypt your `swupdate` builds for code security
- `signed-updates`: add signing to `swupdate` builds to ensure updates are only made from approved sources
- `multiple-boards`: deploy the same application to multiple hardware targets
- `ext-toolchain`: speed up your builds by saving your compilers and tools as a separate tarball
- `init-systemd`: change your init system over to `systemd`, instead of the default `Busybox` 
- `graphics`: run a screen, and build a GUI

