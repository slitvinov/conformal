.POSIX:
.SUFFIXES: .o .c

PREFIX = $(HOME)/.local
CFLAGS = -Ofast -g
CC = c99
LINK = $(CC)
PYTHON = python3
PYTHON_USER_SITE = `$(PYTHON) -m site --user-site`

O = \
main.o\
quickselect.o\

H = \
conformal.h

P = \
conformal.py

L = libconformal.so
$L: $O; $(LINK) $O $(LDFLAGS) -shared $(M_LDFLAGS) -o $@
.c.o:; $(CC) -c -fPIC $(CFLAGS) $<
install: $L $H $P
	mkdir -p $(PREFIX)/lib $(PREFIX)/include $(PYTHON_USER_SITE) && \
	cp $P "$(PYTHON_USER_SITE)" && \
	cp $L $(PREFIX)/lib && \
	cp $H $(PREFIX)/include

main.o: $H
clean:; rm -f -- $L $O
