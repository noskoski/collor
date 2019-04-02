PREFIX = /usr/local/
install: collor.py
		install -d $(DESTDIR)$(PREFIX)/bin
		install -m 755 collor.py $(DESTDIR)$(PREFIX)/bin/
uninstall: collor.py
	  rm -f $(DESTDIR)$(PREFIX)/bin/collor.py
