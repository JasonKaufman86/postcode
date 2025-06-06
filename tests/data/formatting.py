standard_formatting_cases = [
    (
        "SW1W 0NY",
        {
            "area": "SW",
            "district": "1W",
            "sector": "0",
            "unit": "NY",
            "outcode": "SW1W",
            "incode": "0NY",
            "full": "SW1W 0NY",
        },
    ),
    (
        "PO16 7GZ",
        {
            "area": "PO",
            "district": "16",
            "sector": "7",
            "unit": "GZ",
            "outcode": "PO16",
            "incode": "7GZ",
            "full": "PO16 7GZ",
        },
    ),
    (
        "GU16 7HF",
        {
            "area": "GU",
            "district": "16",
            "sector": "7",
            "unit": "HF",
            "outcode": "GU16",
            "incode": "7HF",
            "full": "GU16 7HF",
        },
    ),
    (
        "L1 8JQ",
        {
            "area": "L",
            "district": "1",
            "sector": "8",
            "unit": "JQ",
            "outcode": "L1",
            "incode": "8JQ",
            "full": "L1 8JQ",
        },
    ),
    (
        "M1 1AE",
        {
            "area": "M",
            "district": "1",
            "sector": "1",
            "unit": "AE",
            "outcode": "M1",
            "incode": "1AE",
            "full": "M1 1AE",
        },
    ),
]

crown_formatting_cases = [
    (
        "JE1 1AA",
        {
            "area": "JE",
            "district": "1",
            "sector": "1",
            "unit": "AA",
            "outcode": "JE1",
            "incode": "1AA",
            "full": "JE1 1AA",
        },
    ),
    (
        "JE2 4WD",
        {
            "area": "JE",
            "district": "2",
            "sector": "4",
            "unit": "WD",
            "outcode": "JE2",
            "incode": "4WD",
            "full": "JE2 4WD",
        },
    ),
    (
        "GY1 1AQ",
        {
            "area": "GY",
            "district": "1",
            "sector": "1",
            "unit": "AQ",
            "outcode": "GY1",
            "incode": "1AQ",
            "full": "GY1 1AQ",
        },
    ),
    (
        "IM1 1AF",
        {
            "area": "IM",
            "district": "1",
            "sector": "1",
            "unit": "AF",
            "outcode": "IM1",
            "incode": "1AF",
            "full": "IM1 1AF",
        },
    ),
    (
        "IM2 2BX",
        {
            "area": "IM",
            "district": "2",
            "sector": "2",
            "unit": "BX",
            "outcode": "IM2",
            "incode": "2BX",
            "full": "IM2 2BX",
        },
    ),
]

bfpo_formatting_cases = [
    (
        "BFPO 1",
        {
            "area": None,
            "district": None,
            "sector": None,
            "unit": "1",
            "outcode": "",
            "incode": "1",
            "full": " 1",
        },
    ),
    (
        "BFPO 123",
        {
            "area": None,
            "district": None,
            "sector": None,
            "unit": "123",
            "outcode": "",
            "incode": "123",
            "full": " 123",
        },
    ),
    (
        "BFPO 801",
        {
            "area": None,
            "district": None,
            "sector": None,
            "unit": "801",
            "outcode": "",
            "incode": "801",
            "full": " 801",
        },
    ),
    (
        "BF1 0AA",
        {
            "area": "BF",
            "district": "1",
            "sector": "0",
            "unit": "AA",
            "outcode": "BF1",
            "incode": "0AA",
            "full": "BF1 0AA",
        },
    ),
    (
        "BF1 1AA",
        {
            "area": "BF",
            "district": "1",
            "sector": "1",
            "unit": "AA",
            "outcode": "BF1",
            "incode": "1AA",
            "full": "BF1 1AA",
        },
    ),
]

bot_formatting_cases = [
    (
        "ASCN 1ZZ",
        {
            "area": "ASCN",
            "district": None,
            "sector": "1",
            "unit": "ZZ",
            "outcode": "ASCN",
            "incode": "1ZZ",
            "full": "ASCN 1ZZ",
        },
    ),
    (
        "BBND 1ZZ",
        {
            "area": "BBND",
            "district": None,
            "sector": "1",
            "unit": "ZZ",
            "outcode": "BBND",
            "incode": "1ZZ",
            "full": "BBND 1ZZ",
        },
    ),
    (
        "FIQQ 1ZZ",
        {
            "area": "FIQQ",
            "district": None,
            "sector": "1",
            "unit": "ZZ",
            "outcode": "FIQQ",
            "incode": "1ZZ",
            "full": "FIQQ 1ZZ",
        },
    ),
    (
        "GX11 1AA",
        {
            "area": "GX",
            "district": "11",
            "sector": "1",
            "unit": "AA",
            "outcode": "GX11",
            "incode": "1AA",
            "full": "GX11 1AA",
        },
    ),
    (
        "TKCA 1ZZ",
        {
            "area": "TKCA",
            "district": None,
            "sector": "1",
            "unit": "ZZ",
            "outcode": "TKCA",
            "incode": "1ZZ",
            "full": "TKCA 1ZZ",
        },
    ),
]

non_geographic_formatting_cases = [
    (
        "SE1P 4DD",
        {
            "area": "SE",
            "district": "1P",
            "sector": "4",
            "unit": "DD",
            "outcode": "SE1P",
            "incode": "4DD",
            "full": "SE1P 4DD",
        },
    ),
    (
        "EC1P 1AA",
        {
            "area": "EC",
            "district": "1P",
            "sector": "1",
            "unit": "AA",
            "outcode": "EC1P",
            "incode": "1AA",
            "full": "EC1P 1AA",
        },
    ),
    (
        "W1A 1AA",
        {
            "area": "W",
            "district": "1A",
            "sector": "1",
            "unit": "AA",
            "outcode": "W1A",
            "incode": "1AA",
            "full": "W1A 1AA",
        },
    ),
    (
        "EH99 1SP",
        {
            "area": "EH",
            "district": "99",
            "sector": "1",
            "unit": "SP",
            "outcode": "EH99",
            "incode": "1SP",
            "full": "EH99 1SP",
        },
    ),
    (
        "XM4 5HQ",
        {
            "area": "XM",
            "district": "4",
            "sector": "5",
            "unit": "HQ",
            "outcode": "XM4",
            "incode": "5HQ",
            "full": "XM4 5HQ",
        },
    ),
]

special_formatting_cases = [
    (
        "B1 1HQ",
        {
            "area": "B",
            "district": "1",
            "sector": "1",
            "unit": "HQ",
            "outcode": "B1",
            "incode": "1HQ",
            "full": "B1 1HQ",
        },
    ),
    (
        "BS98 1TL",
        {
            "area": "BS",
            "district": "98",
            "sector": "1",
            "unit": "TL",
            "outcode": "BS98",
            "incode": "1TL",
            "full": "BS98 1TL",
        },
    ),
    (
        "BX1 1LT",
        {
            "area": "BX",
            "district": "1",
            "sector": "1",
            "unit": "LT",
            "outcode": "BX1",
            "incode": "1LT",
            "full": "BX1 1LT",
        },
    ),
    (
        "BX2 1LB",
        {
            "area": "BX",
            "district": "2",
            "sector": "1",
            "unit": "LB",
            "outcode": "BX2",
            "incode": "1LB",
            "full": "BX2 1LB",
        },
    ),
    (
        "CF10 1BH",
        {
            "area": "CF",
            "district": "10",
            "sector": "1",
            "unit": "BH",
            "outcode": "CF10",
            "incode": "1BH",
            "full": "CF10 1BH",
        },
    ),
]
