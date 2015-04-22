# Don't store password - generate them on the fly
nopassword is a determenistic two factor password generator for the command line

## Installation
```bash
pip install nopassword
```

## Usage
The generated passwords are stored in your clipboard, enter a seed/key to generate a password


```bash
nopassword seed
```

## Example
Generate password using "facebook" as seed
```
nopassword facebook
6n1eby^@]{dm6T-{]r{5NC^Z^`%vZ9w4.nemgcrN-v&,|,gS3fn]KzXRH,br"$=zf*"v_q@j@
```

Generate password using "github" as seed
```
nopassword github
k/Mzz-$6AQ\K`1n/mD7]1o0|E'b};RO*ZLzCC]Iuo!oJ#}oB2+a~rx{:o;}&R|O*5k*+u~,%@
```

As this is determenistic, "github" again will generate the same result
```
nopassword github
k/Mzz-$6AQ\K`1n/mD7]1o0|E'b};RO*ZLzCC]Iuo!oJ#}oB2+a~rx{:o;}&R|O*5k*+u~,%@
```

Commandline help
```bash
nopassword --help
Usage: /usr/local/bin/nopassword [OPTIONS] SEED

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
nopassword github -a=alphanumeric
jgddAr2RqhMyNYfYOKLkLUZd8cvnVZcb9tu7yJxa8O2ircJLV9EyhHVm9Lo99eHNTVLMzIj0g
```

Set password length to 10
```
nopassword github -l=10 -a=alphanumeric
3HB8VNJ3dd
```


Set itterations 10
```
nopassword github -l=10 -a=alphanumeric -i=10
MgHDdXCuUP
```

Set itterations 11, result different
```
nopassword github -l=10 -a=alphanumeric -i=11
BBU9FgEamB
```

Generate new keyfile
```
nopassword -k=my_organisation -g
Keyfile my_organisation created
```

Use keyfile
```
nopassword github -l=10 -a=alphanumeric -i=11 -k=my_organisation
pZv645w04Z
```


## Keyfiles
Keyfiles are stored in json format in the ~/.nopassword/ directory.
Keyfiles kan be shared between devices and individuals, copy the .json file.

```
ls -lh ~/.nopassword/
total 216K
-r-------- 1 oskar oskar 99K apr 11 12:31 default.json
-r-------- 1 oskar oskar 99K apr 11 19:21 my_organisation.json
```

## Two factor password generator?
I'd like to think so.
Something you got: **key file** and something you know: **seed**, **iterations** and **alphabet**.

So for a attacker to be able to generate your password they need the keyfile and the parameters.

