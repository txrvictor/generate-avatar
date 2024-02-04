import re

DEFAULT_COLOR = '#000000'
DEFAULT_BG_COLOR = '#f0f0f0'

def is_hex_valid(color):
    """
    Validate a hex string. Returns True if valid, otherwise False.
    """
    return re.match(r'^#[a-fA-F0-9]{6}$', color)

def rgb_to_hex(rgb):
    """
    Convert RGB tuple (0-255) to hex string.
    """
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def hash_to_color(hash):
    """
    Convert a sha256 hash to a hex color string.
    """
    # Sanitize the input hash string to replace non-hexadecimal characters with zero
    non_hex_pattern = re.compile(r'[^0-9a-fA-F]')
    sanitized_hash = non_hex_pattern.sub('0', hash)

    try:
        # Extract parts of the hash to represent the RGB values
        r = int(sanitized_hash[0:2], 16)
        g = int(sanitized_hash[8:10], 16)
        b = int(sanitized_hash[16:18], 16)
    except (ValueError, IndexError):
        print("Invalid hash, falling back to default color")
        return DEFAULT_COLOR
    
    return rgb_to_hex((r, g, b))
