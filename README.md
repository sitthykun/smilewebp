# smilewebp
What's new 1.0.1
- fix bug
- update doc with smile-third-party

The first version 1.0.0.\
Webp image library for python3.

# Download
### Find package
- https://developers.google.com/speed/webp/download

### Or download any from smile-third-party
There are some versions which compacts some OS such as Mac, Ubuntu, ..etc
- https://github.com/sitthykun/smile-third-party

# Find
```commandline
which cwebp
```
$ /usr/bin/cwebp

# Check version
```commandline
cwebp -version
```
$ 0.6.1

# Start to code
```
from smilewebp.Webp import Webp
# initialize
smile    = Webp()
or
smile    = Webp('/usr/bin/cwebp')
```
*** by default the application located in /usr/bin/cwebp

*** it's able to set to another location via
```
smile.setWebp(path= '/usr/bin/cwebp')
```

# test a filename
# quality value starts 20 to 100, and it's integer
```
smile.compress(
  filename  = '/home/pseth/Download/kara.png'
  , quality = 80
)
```

# verify before use
```
if smile.isError():
  print(f'Everything is okay, the file name is: {smile.getFilename()}')

else:
  print(f'{smile.getErrorMessage()}')
```

# Options
- dirname: can be None
set coy to a new directory for the new file

- newFilename: can be None
set a new copy name

Both can set any value, or None, or one of them.

Let check the example:

Ex 1
```
smile.convert(
  filename      = '/home/pseth/Download/kara.png'
  , quality     = 100
  # move to new directory
  , dirname     = '/home/pseth/Document/'
  , newFilename = 'jojo'
)
```

Ex 2
```
smile.convert(
  filename      = '/home/pseth/Download/kara.png'
  , quality     = 100
  # move to new directory
  , dirname     = '/home/pseth/Document/'
)
```

Ex 3 
```
smile.convert(
  filename      = '/home/pseth/Download/kara.png'
  , quality     = 100
  # move to new directory
  , newFilename = 'jojo'
)
```


It is also available on https://pypi.org/project/smilewebp \
To Support my work, please donate me via <a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/sitthykun"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a Pizza"><span style="margin-left:5px;font-size:28px !important;">Buy me a Coffee</span></a>

