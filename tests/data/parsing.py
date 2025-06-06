standard_postcodes = [
    "SW1W 0NY",
    "PO16 7GZ",
    "GU16 7HF",
    "L1 8JQ",
    "M1 1AE",
    "W1A 0AX",
    "B33 8TH",
    "CR2 6XH",
    "EC1A 1BB",
    "DN55 1PT",
]

crown_dependency_postcodes = [
    "JE2 4SU",
    "GY1 1AA",
    "GY10 1AA",
    "IM1 1AF",
]

bot_postcodes = [
    "ASCN 1ZZ",
    "BBND 1ZZ",
    "BIQQ 1ZZ",
    "FIQQ 1ZZ",
    "GX11 1AA",
    "PCRN 1ZZ",
    "SIQQ 1ZZ",
    "STHL 1ZZ",
    "TDCU 1ZZ",
    "TKCA 1ZZ",
    "AI-2640",
    "KY1-1102",
    "MSR-1110",
    "VG1110",
    "HM 11",
]

bfpo_postcodes = [
    "BFPO 1",
    "BFPO 123",
    "BFPO 801",
    "BF1 0AA",
    "BF1 1AB",
    "BF1 3EF",
    "BF1 4GH",
]

non_geographic_postcodes = [
    "BX1 1LT",
    "BF1 0AA",
    "BF1 1AB",
    "XX1 1XX",
    "BN50 9AA",
    "BN88 1AH",
    "WV98 1AA",
    "WV99 1XX",
    "EH99 1SP",
    "G58 1SB",
    "CF91 1AA",
    "M60 1NW",
    "GIR 0AA",
    "XM4 5HQ",
    "EC1P 1AA",
    "SE1P 5LX",
    "SW1P 3EU",
    "N1P 1AA",
    "NW1W 1AA",
    "CH25 9AA",
    "LS99 1AA",
]

special_postcodes = [
    "B1 1HQ",
    "BS98 1TL",
    "BX1 1LT",
    "BX2 1LB",
    "BX3 2BB",
    "BX4 7SB",
    "BX5 5AT",
    "CF10 1BH",
    "CF99 1NA",
    "CO4 3SQ",
    "CV4 8UW",
    "CV35 0DB",
    "DA1 1RT",
    "DE99 3GG",
    "DE55 4SW",
    "DH98 1BT",
    "DH99 1NS",
    "E14 5HQ",
    "E14 5JP",
    "E16 1XL",
    "E20 2AQ",
    "E20 2BB",
    "E20 2ST",
    "E20 3BS",
    "E20 3EL",
    "E20 3ET",
    "E20 3HB",
    "E20 3HY",
    "E98 1SN",
    "E98 1ST",
    "E98 1TT",
    "EC2N 2DB",
    "EC2Y 8HQ",
    "EC4Y 0HQ",
    "EC4Y 0JP",
    "EH12 1HQ",
    "EH99 1SP",
    "G58 1SB",
    "GIR 0AA",
    "HA9 0WS",
    "HP5 1WA",
    "IV21 2LR",
    "L30 4GB",
    "LS98 1FD",
    "M50 2BH",
    "M50 2QH",
    "N1 9GU",
    "N81 1ER",
    "NE1 4ST",
    "NG80 1EH",
    "NG80 1LH",
    "NG80 1RH",
    "NG80 1TH",
    "RM11 1QT",
    "PH1 2SJ",
    "PH1 5RB",
    "S2 4SU",
    "S6 1SW",
    "S14 7UP",
    "S70 1GW",
    "SA99 1AA",
    "SE1 0NE",
    "SE1 8UJ",
    "SM6 0HB",
    "SN38 1NW",
    "SR5 1SU",
    "SW1A 0AA",
    "SW1A 0PW",
    "SW1A 1AA",
    "SW1A 2AA",
    "SW1A 2AB",
    "SW1H 0TL",
    "SW1P 3EU",
    "SW1W 0DT",
    "SW1V 1AP",
    "SW1X 1SP",
    "SW11 7US",
    "SW19 5AE",
    "TW8 9GS",
    "W1A 1AA",
    "W1D 4FA",
    "W1N 4DJ",
    "W1T 1FB",
]

invalid_postcodes = [
    None,  # Not a string
    12345,  # Integer type
    "",  # Empty string
    "   ",  # Whitespace only
    "SW1A@1AA",  # Contains invalid character (@)
    "W1A_0AX",  # Contains invalid character (_)
    "EC1A#1BB",  # Contains invalid character (#)
    "123",  # Too short
    "ABCDEFGHIJK",  # Too long (11 characters)
    "A1 1!",  # Invalid character (!)
    "A1@ 1AA",  # Invalid character (@)
    "A1",  # Too short even after stripping
    "A1 1AAAA",  # Inward part too long
    "A65 B2CD",  # Inward code too long
    "E1W-1AA",  # Hyphen in invalid position
]
