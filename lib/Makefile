.POSIX:.
.SUFFIXES:
.SUFFIXES: .o
.SUFFIXES: .c

AR = ar
RANLIB = ranlib
CFLAGS = -Ofast -g
CC = c99
LINK = $(CC)
PYTHON = python3
PYTHON_USER_SITE = `$(PYTHON) -m site --user-site`

O = \
main.o\
quickselect.o\

P = \
conformal.py

L = libconformal.so
S = libconformal.a
all: $S $L
$L: $O; $(LINK) $O $(LDFLAGS) -shared -o $@
$S: $O; $(AR) rc $@ $O && $(RANLIB) $@
.c.o:; $(CC) -c -fPIC $(CFLAGS) $<
install: $L $S $P
	mkdir -p "$(PYTHON_USER_SITE)" && \
	cp $P $L $S "$(PYTHON_USER_SITE)"

main.o: conformal.h
clean:; rm -f -- $L $O $S
