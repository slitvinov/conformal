.POSIX:.
.SUFFIXES:
.SUFFIXES: .o
.SUFFIXES: .c

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
$L: $O; $(LINK) $O $(LDFLAGS) -shared -o $@
.c.o:; $(CC) -c -fPIC $(CFLAGS) $<
install: $L $H $P
	mkdir -p "$(PYTHON_USER_SITE)" && \
	cp $P $L "$(PYTHON_USER_SITE)"

main.o: $H
clean:; rm -f -- $L $O
