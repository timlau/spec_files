SUBDIRS = dexed geonkick sfizz AIDA-X neural-amp-modeler 

all:
	@echo "Nothing to do, use a specific target"
clean:
	@for dir in $(SUBDIRS); do \
		echo "Cleaning $$dir"; \
		$(MAKE) -s -C $$dir clean; \
	done

.PHONY: all clean