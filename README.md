# Interaction with Anthias (Screenly) API

Anthias is the community-supported version of Screenly, a tool for display terminals to run on Raspberry Pi.

## How to use it

```
import os
from anthias import enable

os.environ["ANTHIAS_ROOT_URL"] = "http://infotron-3000/api/v1.2"

enable("IMG_20260328_151930110.jpg")
```
