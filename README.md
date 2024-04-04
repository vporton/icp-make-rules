# make-rules

This MOPS package currently does not work, because MOPS does not support
distributing non-`.mo` files (except of README and LICENSE).

Download `icp.rules` directly from [GitHub](https://github.com/vporton/icp-make-rules).

## Install
```
mops add make-rules
```

## Usage
In `Makefile` after installing this into directory `icp-make-rules`
(for example, as a Git submodule, what is recommended):

```make
ICPRULESDIR = icp-make-rules
include $(ICPRULESDIR)/icp.rules

# If missing, points to `out` by default
# DESTDIR = out

# Optional additional settings:
NETWORK = local
IDENTITY = default
MOFLAGS =
DFXCREATEFLAGS =
DFXINSTALLFLAGS =

# List of all your `.mo` files:
MOFILES = \
  src/FILE1.mo \
  src/FILE2.mo
```

Now, to compile `FILE1.mo`, you issue
```
make out/src/FILE1.wasm
```
and to deploy it to the blockchain,
```
make out/src/FILE1.deploy
```
