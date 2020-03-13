PLANTUML ?= ./plantuml.jar
PLANTUML_OPTIONS ?= -nometadata -progress
PLANTUML_CMD ?= java -jar $(PLANTUML) $(PLANTUML_OPTIONS)
PLANTUML_VERSION ?= 1.2019.4
PLANTUML_MIRROR ?= netcologne.dl.sourceforge.net
PLANTUML_SHASUM ?= 792465ea1ba591fd13acbc53413af57fa142efe8fa11b8620bdd503be771a04d
CHECKSUM = `shasum -a 256 $(PLANTUML)`

.PHONY: help download
help:
	@echo "all:                 Fetches dependencies and creates a diagram"
	@echo "create_graphics:     Create the required puml graphics and store them into ../dist folder
	@echo "download:            Download icons from google"

plantuml.jar:
	@wget https://$(PLANTUML_MIRROR)/project/plantuml/$(PLANTUML_VERSION)/plantuml.$(PLANTUML_VERSION).jar -O $(PLANTUML) && \
	case "$(CHECKSUM)" in \
		($(PLANTUML_SHASUM)\ *): ok ;; \
		(*) echo checkum mismatch! expected=$(PLANTUML_SHASUM) got=$(CHECKSUM); \
		echo removing $(PLANTUML); \
		rm $(PLANTUML); \
		exit 1 ;; \
	esac

download: plantuml.jar
	@wget  https://cloud.google.com/icons/files/gcp-icons.zip -O gcp.zip && \
	unzip gcp.zip && \
	mv GCP\ Icons/Products\ and\ services ./Products_and_services && \
	rm -rf GCP\ Icons

create_graphics:
	@python create_graphics.py

clean:
	@rm -f ./plantuml.jar
	@rm -rf __MACOSX gcp.zip
