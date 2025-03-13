#######################################################################
#
# Closeblink Application
#
#######################################################################

CLOSEBLINK_VERSION = 1.0
CLOSEBLINK_SITE = $(BR2_EXTERNAL)/package/closeblink
CLOSEBLINK_SITE_METHOD = local

define CLOSEBLINK_BUILD_CMDS
	$(TARGET_CC) $(TARGET_CFLAGS) -o $(@D)/closeblink $(@D)/closeblink.c
endef

define CLOSEBLINK_INSTALL_TARGET_CMDS
	$(INSTALL) -D $(@D)/closeblink $(TARGET_DIR)/usr/bin/closeblink
endef

$(eval $(generic-package))

