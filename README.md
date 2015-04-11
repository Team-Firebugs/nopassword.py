# Don't store password - generate them on the fly
nopass.py is a determenistic password generator for the command line

## Installation
```bash
pip install nopassword
```

## Usage
The generated passwords are stored in your clipboard, enter a seed/key to generate a password


```bash
nopass.py seed
```

## Example
Generate password using "facebook" as seed
```
nopass.py facebook
6n1eby^@]{dm6T-{]r{5NC^Z^`%vZ9w4.nemgcrN-v&,|,gS3fn]KzXRH,br"$=zf*"v_q@j@
```

Generate password using "github" as seed
```
nopass.py github
k/Mzz-$6AQ\K`1n/mD7]1o0|E'b};RO*ZLzCC]Iuo!oJ#}oB2+a~rx{:o;}&R|O*5k*+u~,%@
```

As this is determenistic, "github" again will generate the same result
```
nopass.py github
k/Mzz-$6AQ\K`1n/mD7]1o0|E'b};RO*ZLzCC]Iuo!oJ#}oB2+a~rx{:o;}&R|O*5k*+u~,%@
```

Commandline help
```bash
nopass.py --help
Usage: /usr/local/bin/nopass.py [OPTIONS] SEED

Required arguments:
 SEED                      Seed to generate password

Optional arguments:
 -a  --alphabet=ascii      Character set used: [alphanumeric, ascii, digits]
 -l  --length=73           Length of generated passwords
 -k  --keyfile=default     Keyfile to use
 -i  --itterations=113     Number of itterations

Switches:
 -h  --help                Display options and commands
 -g  --generate            Generate new keyfile
```

Change alphabet to alphanumeric
```
nopass.py github -a=alphanumeric
jgddAr2RqhMyNYfYOKLkLUZd8cvnVZcb9tu7yJxa8O2ircJLV9EyhHVm9Lo99eHNTVLMzIj0g
```

Set password length to 10
```
nopass.py github -l=10 -a=alphanumeric
3HB8VNJ3dd
```


Set itterations 10
```
nopass.py github -l=10 -a=alphanumeric -i=10
MgHDdXCuUP
```

Set itterations 11, result completly differnt
```
nopass.py github -l=10 -a=alphanumeric -i=11
BBU9FgEamB
```

