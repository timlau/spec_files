
ifeq ($(ROOT),)
$(error invalid usage)
endif
DNF_BUILDDEP_INSTALLED = ${BUILDDIR}/DEPS_INSTALLED

all: srpm

localbuild: srpm
	@echo "Building RPM locally"
ifeq (,$(wildcard $(DNF_BUILDDEP_INSTALLED)))
	@sudo dnf builddep -y ${PROJECT}.spec
	@touch $(DNF_BUILDDEP_INSTALLED)
endif	
	@rpmbuild --define "_topdir $(BUILDDIR)" -ba ${PROJECT}.spec
	@echo "--> Build RPMs"
	@tree -P *.rpm -I *.src.rpm $(BUILDDIR)/RPMS	

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

clean-archive:
	@rm -rf $(BUILDDIR)/SOURCES/*


.PHONY: clean mockinst mockbuild coprbuild 
