# Note: this is a placeholder file
#
# Currently no external packages are part of the project
#
# Text below this line is commented-out example of how to add an external 
# package for future reference


# # Include the custom package directory
# BR2_EXTERNAL_MY_PROJECT_PATH := $(call qstrip,$(BR2_EXTERNAL_MY_PROJECT))

# # Define your packages here
# MY_PROJECT_PACKAGES = my_custom_package

# # Append the packages to Buildroot's package list
# BR2_PACKAGE_OVERRIDE += $(MY_PROJECT_PACKAGES)

# # Example package definition
# my_custom_package:
	# $(info Building my_custom_package)
	# # Custom build logic can go here (if needed)
