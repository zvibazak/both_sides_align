# Both sides align
A python script that aligns text to both sides.

## Example:
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
