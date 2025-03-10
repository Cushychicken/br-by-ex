# Example 1 - Basic Out of Tree Buildroot Project

* This is a bare bones example of an RPi4 defconfig file that's been extremely lightly customized
* Edited just a little bit from the `raspberrypi4_defconfig` for flavoring

* Modifications:
	* Added a single target package - `ascii_invaders` (a scrolling Space Invaders clone you can play on the command line)
	* Added support for an external toolchain. We'll talk about this in more detail later; for now, it's enough to say this is to speed up building our software examples. 
