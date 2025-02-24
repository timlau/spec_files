
ifeq ($(ROOT),)
$(error invalid usage)
endif

VERSION=$(shell awk '/Version:/ { print $$2 }' ${PROJECT}.spec)
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
GIT_DIR = ${BUILDDIR}
GIT_URL = git@github.com:asb2m10/dexed.git  
GIT_TAG = v$(VERSION)
SRC_DIR = $(GIT_DIR)/$(PROJECT)
TAR_GZ = ${BUILDDIR}/SOURCES/$(PROJECT)-$(VERSION).tar.gz
MOCK_REL = fedora-41-x86_64
MOCK_RESULT = /var/lib/mock/${MOCK_REL}/result
COPR_REPO = audio

all: srpm

archive: clone
ifeq (,$(wildcard $(TAR_GZ)))
	@echo "Creating archive"
	@mkdir -p ${BUILDDIR}/SOURCES
	@cd $(SRC_DIR); git ls-files --recurse-submodules | tar caf $(TAR_GZ) --xform s:^:$(PROJECT)-$(VERSION)/: --verbatim-files-from -T-
	@echo "Archive created : $(TAR_GZ)"
	@$(MAKE) -s copy_pactches
endif

clone:
ifeq (,$(wildcard $(SRC_DIR)))
	@echo "Cloning repository"
	@git clone $(GIT_URL) $(SRC_DIR)
	@cd $(SRC_DIR); git checkout -b release $(GIT_TAG); git submodule update --init --recursive
	@echo "Repository cloned : $(SRC_DIR)"
endif

show:
	@echo "Project           : $(PROJECT)"
	@echo "Project version   : $(VERSION)"
	@echo "Git URL           : $(GIT_URL)"
	@echo "Git tag           : $(GIT_TAG)"
	@echo "Current directory : $(CURDIR)"
	@echo "Build directory   : $(BUILDDIR)"
	@echo "Source directory  : $(SRC_DIR)"
	@echo "Tarball           : $(TAR_GZ)"
	@echo "Mock release      : $(MOCK_REL)"
	@echo "Copr repository   : $(COPR_REPO)"
	@echo "Build from git tag checkout"

.PHONY: archive clone show clean mockinst mockbuild coprbuild srpm update-gitdate

include $(ROOT)/Makefile.build.mk
