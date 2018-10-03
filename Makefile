BINDIR = $(DESTDIR)/usr/bin
SRC = listfunds.sh
DEST = listfunds

install:
	cp $(SRC) $(DEST)
	install --mode=755 $(DEST) $(BINDIR)/
	rm $(DEST)

uninstall:
	rm $(BINDIR)/$(NAME)
