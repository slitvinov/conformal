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

L = libconformal.a
$L: $O; ar rv $@ $O && ranlib $@
.c.o:; $(CC) -c $(CFLAGS) $<
install: $L $H
	mkdir -p $(PREFIX)/lib $(PREFIX)/include && \
	cp $L $(PREFIX)/lib/ && cp $H $(PREFIX)/include/
main.o: $H
clean:; rm -f -- $L $O
