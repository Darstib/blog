---
tags:
  - notes
comments: true
dg-publish: true
---

> Learn from [cryptohack](https://cryptohack.org/).

```python title="useful lib"
ord() & chr()
bytes.fromhex() & .hex()
from base64 import b64encode()
from Crypto.Util.number import long_to_bytes, bytes_to_long
from pwn import xor
from math import gcd
from math import mod_inverse
```

- [Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
    - $a^p \equiv a \mod p$
- [Quadratic residue](https://en.wikipedia.org/wiki/Quadratic_residue)
    - the int n in $x^2\equiv n(\mathrm{mod~}p)$ is a quadratic residue
- Legendre's Symbol: $(a/p)≡a^{p−1/2}\mod p$
    - (a/p)= 1 if a is a quadratic residue and $a\not\equiv0 \mod p$
    - (a/p)= -1 if a is a quadratic non-residue mod p
    - (a/p)= 0 if $a\equiv0 \mod p$
- Chinese Remainder Theorem
    - 