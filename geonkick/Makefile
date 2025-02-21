PROJECT = geonkick
VERSION = 3.5.2
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
SRC_DIR = $(GIT_DIR)/$(PROJECT)
TAR_GZ = ${BUILDDIR}/SOURCES/v$(VERSION).tar.gz
MOCK_REL = fedora-41-x86_64
COPR_REPO = audio

all:
	@echo "Nothing to do, use a specific target"


archive:
ifeq (,$(wildcard $(TAR_GZ)))
	@echo "Creating archive"
	@mkdir -p ${BUILDDIR}/SOURCES
	@spectool -g -S $(PROJECT).spec -C ${BUILDDIR}/SOURCES
	@echo "Archive created : $(TAR_GZ)"
	cp *.patch ${BUILDDIR}/SOURCES
endif

srpm: archive
	@echo "Building SRPM"
	@rpmbuild --define '_topdir $(BUILDDIR)' -bs $(PROJECT).spec

mockbuild: srpm
	@echo "Building RPM in mock"
	@mock -r $(MOCK_REL) --rebuild $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm

coprbuild: srpm
	@echo "Building RPM in copr"
	@copr-cli build --nowait $(COPR_REPO) $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm

show:
	@echo "Project           : $(PROJECT)"
	@echo "Project version   : $(VERSION)"
	@echo "Current directory : $(CURDIR)"
	@echo "Build directory   : $(BUILDDIR)"
	@echo "Tarball           : $(TAR_GZ)"
	@echo "Mock release      : $(MOCK_REL)"
	@echo "Copr repository   : $(COPR_REPO)"

clean:
	@rm -rf $(BUILDDIR)


.PHONY: all archive clone show clean
