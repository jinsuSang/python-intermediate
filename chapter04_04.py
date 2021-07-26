# Sequence
# 해시 테이블 : 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict, Set

# immutable Dict
from types import MappingProxyType

d = {'k1': 'v1'}
d_frozen = MappingProxyType(d)

print(d, id(d), type(d))
print(d_frozen, id(d_frozen), type(d_frozen))

# d_frozen['k2'] = 'v2'
# 'mappingproxy' object does not support item assignment

print()

s = {2, 5, 7}
s2 = {2, 7, 7, 8}
s3 = frozenset(s2)
# s3.add('melon')
# AttributeError: 'frozenset' object has no attribute 'add'
print(s, type(s))
print(s2, type(s2))
print(s3, type(s3))

# 선언 최적화
# 바이트 코드 -> 파이선 인터프리터 실행
from dis import dis
print('---------')
print(dis('{10}'))
print('---------')
print(dis('set([10])'))

'''
---------
  1           0 LOAD_CONST               0 (10)
              2 BUILD_SET                1
              4 RETURN_VALUE
None
---------
  1           0 LOAD_NAME                0 (set)
              2 LOAD_CONST               0 (10)
              4 BUILD_LIST               1
              6 CALL_FUNCTION            1
              8 RETURN_VALUE
None

'''

# comprehending Set
from unicodedata import name

print({name(chr(i), '') for i in range (97, 123)})
# {'', 'LATIN CAPITAL LETTER Z', 'QUESTION MARK', 'PLUS SIGN', 'LATIN CAPITAL LETTER AE', 'LATIN SMALL LETTER A WITH TILDE', 'LATIN CAPITAL LETTER A WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER Y WITH ACUTE', 'APOSTROPHE', 'COLON', 'LATIN CAPITAL LETTER U', 'LATIN SMALL LETTER O WITH GRAVE', 'LATIN SMALL LETTER Y WITH ACUTE', 'LATIN SMALL LETTER B', 'LATIN SMALL LETTER A WITH CIRCUMFLEX', 'FULL STOP', 'LATIN SMALL LETTER E WITH CIRCUMFLEX', 'LATIN SMALL LETTER A WITH RING ABOVE', 'LATIN CAPITAL LETTER D', 'LATIN CAPITAL LETTER Y', 'RIGHT CURLY BRACKET', 'LATIN SMALL LETTER A WITH ACUTE', 'LATIN SMALL LETTER J', 'PLUS-MINUS SIGN', 'LATIN SMALL LETTER U WITH GRAVE', 'SEMICOLON', 'LATIN SMALL LETTER I WITH GRAVE', 'LATIN CAPITAL LETTER U WITH GRAVE', 'LATIN CAPITAL LETTER B', 'LATIN CAPITAL LETTER R', 'LATIN SMALL LETTER THORN', 'COMMA', 'LATIN CAPITAL LETTER U WITH CIRCUMFLEX', 'DIGIT TWO', 'CENT SIGN', 'MICRO SIGN', 'LATIN SMALL LETTER C WITH CEDILLA', 'LATIN CAPITAL LETTER I WITH ACUTE', 'LATIN SMALL LETTER U WITH CIRCUMFLEX', 'LEFT PARENTHESIS', 'LATIN SMALL LETTER W', 'LATIN SMALL LETTER I', 'LATIN CAPITAL LETTER H', 'LATIN SMALL LETTER O WITH ACUTE', 'BROKEN BAR', 'LATIN CAPITAL LETTER E WITH ACUTE', 'MULTIPLICATION SIGN', 'LATIN CAPITAL LETTER E', 'LATIN CAPITAL LETTER L', 'VULGAR FRACTION THREE QUARTERS', 'LATIN SMALL LETTER N', 'INVERTED EXCLAMATION MARK', 'SOFT HYPHEN', 'LATIN SMALL LETTER O WITH CIRCUMFLEX', 'LATIN SMALL LETTER E', 'EQUALS SIGN', 'LATIN CAPITAL LETTER C WITH CEDILLA', 'DIGIT SIX', 'DIGIT FOUR', 'YEN SIGN', 'LATIN CAPITAL LETTER K', 'LATIN SMALL LETTER I WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER N', 'LATIN CAPITAL LETTER W', 'LATIN SMALL LETTER H', 'LATIN CAPITAL LETTER P', 'MASCULINE ORDINAL INDICATOR', 'LATIN CAPITAL LETTER J', 'LATIN SMALL LETTER X', 'LATIN CAPITAL LETTER S', 'LATIN SMALL LETTER K', 'NUMBER SIGN', 'LATIN CAPITAL LETTER F', 'LATIN SMALL LETTER U', 'LATIN SMALL LETTER Z', 'LATIN CAPITAL LETTER O WITH STROKE', 'COPYRIGHT SIGN', 'LOW LINE', 'GRAVE ACCENT', 'LATIN SMALL LETTER E WITH DIAERESIS', 'LATIN CAPITAL LETTER U WITH ACUTE', 'GREATER-THAN SIGN', 'LATIN SMALL LETTER U WITH DIAERESIS', 'LATIN SMALL LETTER A WITH GRAVE', 'LATIN CAPITAL LETTER A WITH RING ABOVE', 'LATIN SMALL LETTER D', 'PERCENT SIGN', 'LATIN CAPITAL LETTER I WITH GRAVE', 'LATIN CAPITAL LETTER X', 'SOLIDUS', 'DOLLAR SIGN', 'LATIN SMALL LETTER Y', 'LATIN CAPITAL LETTER T', 'VERTICAL LINE', 'SUPERSCRIPT THREE', 'QUOTATION MARK', 'LATIN SMALL LETTER M', 'LATIN SMALL LETTER O WITH DIAERESIS', 'LATIN CAPITAL LETTER E WITH GRAVE', 'LATIN CAPITAL LETTER E WITH DIAERESIS', 'LATIN CAPITAL LETTER I', 'LEFT-POINTING DOUBLE ANGLE QUOTATION MARK', 'LATIN SMALL LETTER T', 'DIGIT THREE', 'LATIN CAPITAL LETTER A WITH GRAVE', 'LATIN SMALL LETTER L', 'COMMERCIAL AT', 'MACRON', 'REGISTERED SIGN', 'LEFT CURLY BRACKET', 'DEGREE SIGN', 'LATIN CAPITAL LETTER O WITH GRAVE', 'DIGIT SEVEN', 'DIGIT ZERO', 'LATIN SMALL LETTER O', 'TILDE', 'LATIN SMALL LETTER I WITH ACUTE', 'LATIN SMALL LETTER I WITH DIAERESIS', 'DIAERESIS', 'LATIN CAPITAL LETTER O WITH TILDE', 'LATIN SMALL LETTER SHARP S', 'LATIN CAPITAL LETTER A WITH ACUTE', 'LESS-THAN SIGN', 'NO-BREAK SPACE', 'SECTION SIGN', 'LATIN CAPITAL LETTER N WITH TILDE', 'INVERTED QUESTION MARK', 'RIGHT SQUARE BRACKET', 'LATIN CAPITAL LETTER U WITH DIAERESIS', 'LATIN SMALL LETTER S', 'LATIN SMALL LETTER A', 'LATIN SMALL LETTER V', 'VULGAR FRACTION ONE QUARTER', 'ASTERISK', 'LATIN CAPITAL LETTER A WITH TILDE', 'ACUTE ACCENT', 'LATIN SMALL LETTER Q', 'LEFT SQUARE BRACKET', 'LATIN CAPITAL LETTER I WITH DIAERESIS', 'DIGIT NINE', 'CEDILLA', 'LATIN CAPITAL LETTER M', 'LATIN SMALL LETTER G', 'LATIN CAPITAL LETTER THORN', 'LATIN SMALL LETTER AE', 'DIGIT FIVE', 'LATIN CAPITAL LETTER A', 'MIDDLE DOT', 'DIVISION SIGN', 'LATIN SMALL LETTER E WITH GRAVE', 'LATIN CAPITAL LETTER C', 'REVERSE SOLIDUS', 'DIGIT EIGHT', 'LATIN SMALL LETTER F', 'LATIN SMALL LETTER E WITH ACUTE', 'LATIN CAPITAL LETTER O WITH ACUTE', 'LATIN CAPITAL LETTER Q', 'SUPERSCRIPT ONE', 'LATIN CAPITAL LETTER ETH', 'CURRENCY SIGN', 'LATIN CAPITAL LETTER I WITH CIRCUMFLEX', 'LATIN SMALL LETTER O WITH TILDE', 'RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK', 'LATIN SMALL LETTER ETH', 'EXCLAMATION MARK', 'RIGHT PARENTHESIS', 'NOT SIGN', 'LATIN SMALL LETTER N WITH TILDE', 'PILCROW SIGN', 'SUPERSCRIPT TWO', 'LATIN CAPITAL LETTER A WITH DIAERESIS', 'LATIN CAPITAL LETTER G', 'LATIN CAPITAL LETTER O', 'HYPHEN-MINUS', 'LATIN SMALL LETTER R', 'LATIN CAPITAL LETTER E WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER V', 'DIGIT ONE', 'LATIN SMALL LETTER O WITH STROKE', 'VULGAR FRACTION ONE HALF', 'LATIN SMALL LETTER A WITH DIAERESIS', 'LATIN SMALL LETTER U WITH ACUTE', 'SPACE', 'LATIN SMALL LETTER C', 'LATIN CAPITAL LETTER O WITH CIRCUMFLEX', 'POUND SIGN', 'LATIN CAPITAL LETTER O WITH DIAERESIS', 'CIRCUMFLEX ACCENT', 'LATIN SMALL LETTER Y WITH DIAERESIS', 'AMPERSAND', 'LATIN SMALL LETTER P', 'FEMININE ORDINAL INDICATOR'}



