import hashlib
import requests
from typing import Optional

HIBP_RANGE_URL = "https://api.pwnedpasswords.com/range/{}"

def hash_password(password: str) -> str:
    """
    Return uppercase SHA-1 hash for the given password.
    """
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

def get_pwned_api_data(prefix: str, timeout: int = 10) -> Optional[str]:
    """
    Query HIBP range API for the given prefix (first 5 chars).
    Returns response text on success, or None on error (network / non-200).
    """
    url = HIBP_RANGE_URL.format(prefix)
    try:  
        res = requests.get(url, timeout=timeout)
        if res.status_code == 200:
            return res.text
        else:
            # non-200: treat as error, caller can handle None
            return None
    except requests.RequestException:
        return None

def parse_pwned_count(api_text: str, suffix: str) -> int:
    """
    Parse the API response text and return the breach count for the given suffix.
    api_text: raw response from API (many lines "HASH_SUFFIX:COUNT")
    suffix: remainder of the SHA-1 after the first 5 chars (uppercase)
    Returns integer count (0 means not found or on parse error).
    """
    if not api_text:
        return 0

    for line in api_text.splitlines():
        parts = line.split(':')
        if len(parts) != 2:
            continue
        line_suffix = parts[0].strip().upper()
        count_str = parts[1].strip()
        if line_suffix == suffix:
            try:
                return int(count_str)
            except ValueError:
                return 0
    return 0

def check_password_breach(password: str) -> int:
    """
    Convenience function: given plaintext password, returns breach count.
    This does local hashing, calls HIBP, parses and returns count.
    """
    sha1 = hash_password(password)
    prefix = sha1[:5]
    suffix = sha1[5:]
    api_text = get_pwned_api_data(prefix)
    count = parse_pwned_count(api_text, suffix)
    # best-effort cleanup
    sha1 = None
    del sha1
    return count
