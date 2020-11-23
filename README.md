# Both sides align
A python script that aligns text to both sides.

## Examples:
This text: 

```Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus bibendum nulla nec efficitur. Quisque id aliquam enim. Etiam non lectus id risus rhoncus condimentum. Nam ultrices ex quis risus iaculis ullamcorper. Vivamus id venenatis mi, et suscipit ipsum. Nam eu malesuada mauris, et scelerisque tellus. Nunc id dui in lacus varius hendrerit gravida facilisis tellus. Suspendisse commodo, mauris vitae ornare euismod, lorem nulla porttitor elit, eu laoreet odio nulla at arcu. Nulla facilisi. Nam sollicitudin ligula sed malesuada tempus. Praesent vel tristique lorem. Donec ultricies bibendum erat, ac blandit urna semper et. Nulla blandit sagittis nisl eu congue. Morbi pretium felis eget massa lacinia tincidunt.```


Using this code 
```python
from both_sides_align import both_sides_align
both_sides_align(txt,100,3)
```
Will give this text:
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus bibendum nulla nec efficitur.
Quisque id aliquam enim. Etiam non lectus id risus rhoncus condimentum. Nam ultrices  ex quis risus
iaculis ullamcorper. Vivamus id venenatis mi, et suscipit ipsum. Nam eu malesuada mauris, et scele-
risque tellus. Nunc id dui in lacus varius hendrerit gravida facilisis tellus. Suspendisse commodo,
mauris vitae ornare euismod, lorem nulla porttitor elit, eu laoreet odio nulla at arcu. Nulla faci-
lisi. Nam sollicitudin ligula  sed  malesuada tempus. Praesent vel tristique lorem. Donec ultricies
bibendum erat, ac blandit urna semper et. Nulla blandit sagittis nisl eu congue. Morbi pretium fel-
is eget massa lacinia tincidunt.
```

And using this code 
```python
from both_sides_align import both_sides_align
both_sides_align(txt,60,3)
```
Will give this text:
```
Lorem ipsum  dolor  sit  amet, consectetur adipiscing elit.
Nulla luctus bibendum nulla nec efficitur. Quisque id aliq-
uam enim. Etiam non lectus  id risus  rhoncus  condimentum.
Nam ultrices ex quis risus iaculis  ullamcorper. Vivamus id
venenatis mi, et suscipit ipsum. Nam eu  malesuada  mauris,
et scelerisque tellus. Nunc id dui in lacus varius hendrer-
it gravida  facilisis tellus. Suspendisse commodo,   mauris
vitae ornare euismod, lorem nulla porttitor elit, eu laore-
et odio nulla at arcu. Nulla facilisi. Nam sollicitudin li-
gula sed malesuada   tempus.  Praesent vel tristique lorem.
Donec  ultricies bibendum erat, ac blandit urna semper  et.
Nulla blandit sagittis nisl  eu congue. Morbi pretium felis
eget massa lacinia tincidunt.
```

## Columns
You can make some columns, see this code:
```python
txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus bibendum nulla nec efficitur. Quisque id aliquam enim. Etiam non lectus id risus rhoncus condimentum. Nam ultrices ex quis risus iaculis ullamcorper. Vivamus id venenatis mi, et suscipit ipsum. Nam eu malesuada mauris, et scelerisque tellus. Nunc id dui in lacus varius hendrerit gravida facilisis tellus. Suspendisse commodo, mauris vitae ornare euismod, lorem nulla porttitor elit, eu laoreet odio nulla at arcu. Nulla facilisi. Nam sollicitudin ligula sed malesuada tempus. Praesent vel tristique lorem. Donec ultricies bibendum erat, ac blandit urna semper et. Nulla blandit sagittis nisl eu congue. Morbi pretium felis eget massa lacinia tincidunt."
txt2 = "Nulla luctus bibendum nulla nec efficitur. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non lectus id risus rhoncus condimentum. Nam ultrices ex quis risus iaculis ullamcorper. Vivamus id venenatis mi, et suscipit ipsum. Nam eu malesuada mauris, et scelerisque tellus. Nunc id dui in lacus varius hendrerit gravida facilisis tellus. Suspendisse commodo, mauris vitae ornare euismod, lorem nulla porttitor elit, eu laoreet odio nulla at arcu. Nulla facilisi. Nam sollicitudin ligula sed malesuada tempus. Praesent vel tristique lorem. Donec ultricies bibendum erat, ac blandit urna semper et. Nulla blandit sagittis nisl eu congue. Morbi pretium felis eget massa lacinia tincidunt. Quisque id aliquam."
col_len = 40
align_text1 = both_sides_align(txt,col_len,4)
align_text2 = both_sides_align(txt2,col_len,4)
for x,y in zip(align_text1.splitlines(),align_text2.splitlines()):
    print (x.ljust(col_len) + "      " + y)
```
Output:
```
Lorem ipsum dolor sit amet, consectetur       Nulla luctus bibendum nulla nec effici-
adipiscing elit. Nulla luctus  bibendum       tur. Lorem ipsum dolor sit amet, conse-
nulla nec efficitur. Quisque id aliquam       ctetur adipiscing elit. Etiam non lect-
enim. Etiam non lectus id risus rhoncus       us   id risus rhoncus condimentum.  Nam
condimentum. Nam ultrices ex quis risus       ultrices ex quis risus iaculis ullamco-
iaculis ullamcorper. Vivamus id venena-       rper. Vivamus id venenatis mi, et susc-
tis mi, et suscipit ipsum. Nam eu male-       ipit ipsum. Nam eu malesuada mauris, et
suada mauris,  et scelerisque   tellus.       scelerisque tellus. Nunc id dui in lac-
Nunc id dui in lacus  varius  hendrerit       us  varius  hendrerit gravida facilisis
gravida   facilisis tellus. Suspendisse       tellus.     Suspendisse commodo, mauris
commodo,  mauris vitae  ornare euismod,       vitae ornare euismod, lorem nulla port-
lorem nulla porttitor elit,  eu laoreet       titor  elit, eu laoreet   odio nulla at
odio nulla at arcu. Nulla facilisi. Nam       arcu. Nulla facilisi. Nam  sollicitudin
sollicitudin ligula sed malesuada temp-       ligula  sed malesuada  tempus. Praesent
us. Praesent vel tristique lorem. Donec       vel  tristique lorem. Donec   ultricies
ultricies  bibendum erat,    ac blandit       bibendum erat, ac  blandit urna  semper
urna semper  et. Nulla blandit sagittis       et. Nulla blandit sagittis nisl eu con-
nisl eu  congue. Morbi   pretium  felis       gue. Morbi    pretium  felis eget massa
eget massa lacinia tincidunt.                 lacinia tincidunt. Quisque id aliquam.
```
