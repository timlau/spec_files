
ifeq ($(ROOT),)
$(error invalid usage)
endif

all: srpm

mockbuild: srpm
	@echo "Building RPM in mock"
	@mock -r $(MOCK_REL) --rebuild $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm
	@echo "--> Build RPMs"
	@tree -P *.rpm -I *.src.rpm $(MOCK_RESULT)

mockinst:
	@sudo dnf install $(MOCK_RESULT)/$(PROJECT)*-$(VERSION)*.x86_64.rpm

coprbuild: srpm
	@echo "Building RPM in copr"
	@copr-cli build --nowait $(COPR_REPO) $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm

clean:
	@rm -rf $(BUILDDIR)


.PHONY: clean mockinst mockbuild coprbuild 
