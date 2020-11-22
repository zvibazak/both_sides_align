import pytest
from both_sides_align import both_sides_align

def test_basic_text():
	txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus bibendum nulla nec efficitur. Quisque id aliquam enim. Etiam non lectus id risus rhoncus condimentum. Nam ultrices ex quis risus iaculis ullamcorper. Vivamus id venenatis mi, et suscipit ipsum. Nam eu malesuada mauris, et scelerisque tellus. Nunc id dui in lacus varius hendrerit gravida facilisis tellus. Suspendisse commodo, mauris vitae ornare euismod, lorem nulla porttitor elit, eu laoreet odio nulla at arcu. Nulla facilisi. Nam sollicitudin ligula sed malesuada tempus. Praesent vel tristique lorem. Donec ultricies bibendum erat, ac blandit urna semper et. Nulla blandit sagittis nisl eu congue. Morbi pretium felis eget massa lacinia tincidunt."

	align_text = both_sides_align(txt,129,0)
	a=' '.join(align_text.split())
	assert (a == txt)

test_basic_text()