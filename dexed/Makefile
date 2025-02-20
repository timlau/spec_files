PROJECT = dexed
VERSION = 0.9.8
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
GIT_DIR = ${BUILDDIR}
GIT_URL = git@github.com:asb2m10/dexed.git  
SRC_DIR = $(GIT_DIR)/$(PROJECT)
TAR_GZ = ${BUILDDIR}/SOURCES/$(PROJECT)-$(VERSION).tar.gz


all:
	@echo "Nothing to do, use a specific target"


archive: clone
ifeq (,$(wildcard $(TAR_GZ)))
	@echo "Creating archive"
	@mkdir -p ${BUILDDIR}/SOURCES
	@cd $(SRC_DIR); git ls-files --recurse-submodules | tar caf $(TAR_GZ) --xform s:^:$(PROJECT)-$(VERSION)/: --verbatim-files-from -T-
	@echo "Archive created : $(TAR_GZ)"
endif

clone:
ifeq (,$(wildcard $(SRC_DIR)))
	@echo "Cloning repository"
	@git clone --recurse-submodules $(GIT_URL) $(SRC_DIR)
endif

srpm: archive
	@echo "Building SRPM"
	@rpmbuild --define '_topdir $(BUILDDIR)' -bs $(PROJECT).spec

show:
	$(eval GIT_REF := $(shell git -C $(SRC_DIR) rev-parse --short HEAD))
	@echo "Project           : $(PROJECT)"
	@echo "Project version   : $(VERSION)"
	@echo "Git URL           : $(GIT_URL)"
	@echo "Current directory : $(CURDIR)"
	@echo "Build directory   : $(BUILDDIR)"
	@echo "Source directory  : $(SRC_DIR)"
	@echo "gitref            : $(GIT_REF)"

clean:
	@rm -rf $(BUILDDIR)


.PHONY: all archive clone show clean
