.POSIX:
.SUFFIXES: .o .c

PREFIX = $(HOME)/.local
CFLAGS = -Ofast -g
CC = c99
LINK = $(CC)

O = \
main.o\
quickselect.o\

H = \
conformal.h

L = libconformal.so
$L: $O; $(LINK) $O $(LDFLAGS) -shared $(M_LDFLAGS) -o $@
.c.o:; $(CC) -c -fPIC $(CFLAGS) $<
install: $L $H
	mkdir -p $(PREFIX)/lib $(PREFIX)/include && \
	cp $L $(PREFIX)/lib/ && cp $H $(PREFIX)/include/
main.o: $H
clean:; rm -f -- $L $O
