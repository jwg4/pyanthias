# Interaction with Anthias (Screenly) API

Anthias is the community-supported version of Screenly, a tool for display terminals to run on Raspberry Pi.

If you have an Anthias instance running, there should be a public API which you can use to make 
changes in the assets displayed from your own code.

Currently the code does not do authentication. The API service can have authorization enabled but this is not supported.

## How to use it

```
import os
from anthias import enable

os.environ["ANTHIAS_ROOT_URL"] = "http://infotron-3000/api/v1.2"

enable("IMG_20260328_151930110.jpg")
```

## Resources

[API info on Screenly forum](https://forums.screenly.io/t/command-line-to-manage-assets/367/2)
