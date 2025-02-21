all:
	@echo "Nothing to do, use a specific target"


clean:
	cd dexed && make $@
	cd geonkick && make $@
	cd sfizz && make $@
	

.PHONY: all clean