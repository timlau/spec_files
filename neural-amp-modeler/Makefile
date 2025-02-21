PROJECT = neural-amp-modeler
VERSION=$(shell awk '/Version:/ { print $$2 }' ${PROJECT}.spec)
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
GIT_DIR = ${BUILDDIR}
#GIT_URL = git@github.com:mikeoliphant/neural-amp-modeler-lv2.git 
GIT_URL = git@github.com:timlau/neural-amp-modeler-lv2.git
GIT_TAG = v$(VERSION)
SRC_DIR = $(GIT_DIR)/$(PROJECT)
TAR_GZ = ${BUILDDIR}/SOURCES/$(PROJECT)-$(VERSION).tar.gz
MOCK_REL = fedora-41-x86_64
COPR_REPO = audio

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
	@git clone $(GIT_URL) $(SRC_DIR)
#	@cd $(SRC_DIR); git checkout -b release $(GIT_TAG); git submodule update --init --recursive
	@cd $(SRC_DIR); git submodule update --init --recursive
	@echo "Repository cloned : $(SRC_DIR)"
endif

update-gitdate:
	$(eval GITDATE := .git$(shell date +%Y%m%d).$(shell git -C $(SRC_DIR) rev-parse --short HEAD))
	@echo "Updating spec file with git date : $(GITDATE)"
	@sed -i -e "s/\.git[0-9]*\.[0-9a-f]*/$(GITDATE)/" $(PROJECT).spec

srpm: archive update-gitdate
	@echo "Building SRPM"
	$(eval GITDATE := .git$(shell date +%Y%m%d).$(shell git -C $(SRC_DIR) rev-parse --short HEAD))
#	@rpmbuild --define '_topdir $(BUILDDIR)' -bs $(PROJECT).spec
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
	@echo "Git URL           : $(GIT_URL)"
	@echo "Git tag           : $(GIT_TAG)"
	@echo "Current directory : $(CURDIR)"
	@echo "Build directory   : $(BUILDDIR)"
	@echo "Source directory  : $(SRC_DIR)"
	@echo "Tarball           : $(TAR_GZ)"
	@echo "Mock release      : $(MOCK_REL)"
	@echo "Copr repository   : $(COPR_REPO)"

clean:
	@rm -rf $(BUILDDIR)


.PHONY: all archive clone show clean update-gitdate
