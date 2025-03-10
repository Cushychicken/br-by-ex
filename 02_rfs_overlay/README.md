# Example 2 - Rootfs Overlays

* One of the first things you want to be able to to is transfer files onto your target 
* Buildroot has a very straightforward mechanism for this: rootfs overlays 

* Modifications:
	* Added a single target package - `ascii_invaders` (a scrolling Space Invaders clone you can play on the command line)
	* Added support for an external toolchain. We'll talk about this in more detail later; for now, it's enough to say this is to speed up building our software examples. 
