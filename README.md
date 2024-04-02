# make-rules

This MOPS package currently does not work, because MOPS does not support
distributing non-`.mo` files (except of README and LICENSE).

Download `icp.rules` directly from [GitHub](https://github.com/vporton/icp-make-rules).

## Install
```
mops add make-rules
```

## Usage
In `Makefile`

```make
include .mops/make-rules/icp.rules
```