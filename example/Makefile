.POSIX:
.SUFFIXES:
.SUFFIXES: .c

CFLAGS = -Ofast -g
CC = c99

M = \
main\

all: $M
$M: $O
.c:; $(CC) $< $(CFLAGS) -I../lib -L../lib -static -lconformal -o $@
clean:; rm -f -- $M $O
