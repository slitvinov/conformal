.POSIX:
.SUFFIXES: .o .c

PREFIX = $(HOME)/.local
M_CFLAGS = -I$(PREFIX)/include
M_LDFLAGS = -L$(PREFIX)/lib -Wl,-R$(PREFIX)/lib -lconformal
CCFLAGS = -Ofast -g
CC = c99
LINK = $(CC)

O = \
main.o\

M = \
main\

all: $M
$M: $O
.c.o:; $(CC) -c $(CFLAGS) $(M_CFLAGS) $<
.o:; $(LINK) $O $(LDFLAGS) $(M_LDFLAGS) -o $@
clean:; rm -f -- $M $O
