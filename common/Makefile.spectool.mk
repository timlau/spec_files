
ifeq ($(ROOT),)
$(error invalid usage)
endif

VERSION=$(shell awk '/Version:/ { print $$2 }' ${PROJECT}.spec)
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
SRC_DIR = $(GIT_DIR)/$(PROJECT)
TAR_GZ = ${BUILDDIR}/SOURCES/$(VERSION).tar.gz
MOCK_REL = fedora-41-x86_64
MOCK_RESULT = /var/lib/mock/${MOCK_REL}/result
COPR_REPO = audio
DNF_BUILDDEP_INSTALLED = ${BUILDDIR}/DEPS_INSTALLED

all: srpm

archive:
ifeq (,$(wildcard $(TAR_GZ)))
	@echo "Creating archive"
	@mkdir -p ${BUILDDIR}/SOURCES
	@spectool -g -S $(PROJECT).spec -C ${BUILDDIR}/SOURCES
	@echo "Archive created : $(TAR_GZ)"
	@$(MAKE) -s copy_pactches
endif

show:
	@echo "Project           : $(PROJECT)"
	@echo "Project version   : $(VERSION)"
	@echo "Current directory : $(CURDIR)"
	@echo "Build directory   : $(BUILDDIR)"
	@echo "Tarball           : $(TAR_GZ)"
	@echo "Mock release      : $(MOCK_REL)"
	@echo "Copr repository   : $(COPR_REPO)"
	@echo "Build from spectool downloaded sources"


.PHONY: archive clone show

include $(ROOT)/Makefile.build.mk
