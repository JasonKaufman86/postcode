# UK Postcode Validator & Parser

A Python library for validating, parsing, and formatting UK postcodes.  
Supports both **offline (regex-based)** and **online (API-based)** validation backends, with structured output and extensible handlers.

---

## ✨ Features

- Full support for UK postcode formats (incl. BFPO, BOTs, Crown Dependencies, and non-geographic codes)
- Parses into structured components: `area`, `district`, `sector`, `unit`, `outcode`, and `incode`
- Regex-based validation (offline-first, no network required)
- Optional API-based validation with:
  - [postcodes.io](https://postcodes.io)
  - [Ordnance Survey Data Hub](https://osdatahub.os.uk/)
- Clear `Result` and `Error` handling
- Built-in logging (console + file)

---

## ⚡ Quickstart

```python
import postcode

# Optional: Enable logging
postcode.configure_logger(level="INFO", to_console=True, to_file="data/postcode.log")

# Create the service (offline regex-based)
service = postcode.Service.using_regex()

# Validate a postcode
if service.validate_one("SW1A 1AA"):
    print("Postcode is valid!")

# Parse and inspect a postcode
result = service.parse_one("SW1A 1AA")

if result.valid:
    pc = result.value
    print(f"Full:     {pc.full}")       # => SW1A 1AA
    print(f"Area:     {pc.area}")       # => SW
    print(f"District: {pc.district}")   # => 1A
    print(f"Sector:   {pc.sector}")     # => 1
    print(f"Unit:     {pc.unit}")       # => AA
    print(f"Outcode:  {pc.outcode}")    # => SW1A
    print(f"Incode:   {pc.incode}")     # => 1AA
```

---

## 📚 Examples

### Validate multiple postcodes

```python
service = postcode.Service.using_regex()
validities = service.validate_many([
    "INVALID",
    "SW1W 0NY",
    "L1 8JQ",
])
print(validities)  # [False, True, True]
```

### Parse multiple postcodes

```python
results = service.parse_many([
    "INVALID",
    "SW1W 0NY",
    "L1 8JQ",
])

for result in results:
    print(result.valid, result.value)
```

### Use Postcode.io API

```python
service = postcode.Service.using_postcode_io(timeout=3)
```

### Use Ordnance Survey Data Hub

```python
service = postcode.Service.using_osdatahub(api_key="your-key-here", timeout=3)
```

---

## 📦 Installation

You can install the library in one of two ways:

### Option 1: From GitHub Releases

1. Download the latest `.whl` file from the [Releases](https://github.com/JasonKaufman86/postcode/releases) page
2. Install using pip:

```bash
pip install path/to/postcode-<version>-py3-none-any.whl
```

### Option 2: From Source

Clone the repository and install:

```bash
git clone https://github.com/JasonKaufman86/postcode.git
cd postcode
pip install .
```

---

## 🧪 Testing

Run all tests using:

```bash
make test
```

This runs all pytest-based test suites, including:
- Structural validation
- Crown dependencies, BOTs, BFPO formats
- Format decomposition (area, district, sector, etc.)
- Invalid input scenarios

---

## 🛠 Development

The project includes a `Makefile` to simplify common tasks:

```bash
make setup DEV=1     # Set up virtual environment with dev dependencies
make format          # Format code with black and isort
make lint            # Lint with autofix
make test            # Run all tests
make quality         # Run format, lint, and test in one go
make build           # Build the wheel distribution
make release         # Tag and push a new version
make reset           # Remove the virtual environment
make help            # Show this help message
```
