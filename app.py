import streamlit as st
from breach_checker import hash_password, get_pwned_api_data, parse_pwned_count
import time

st.set_page_config(page_title="Password Breach Checker", page_icon="🔐", layout="centered")
st.title("🔐 Password Breach Checker")
st.write("Check whether a password has appeared in known data breaches (Have I Been Pwned).")

with st.expander("How it works (short)"):
    st.markdown("""
    - We hash your password locally using SHA-1.  
    - We send only the first 5 characters of the hash to HIBP (k-anonymity).  
    - HIBP returns many suffixes and counts; we check locally for a match.
    """)

with st.sidebar:
    st.header("Options")
    cache_api = st.checkbox("Cache API responses by prefix (recommended)", value=True)
    st.markdown("---")
    st.markdown("Tip: Do not paste production secrets on shared machines.")

password = st.text_input("Enter password to check", type="password", help="Typing is hidden.")

# Use a button so user controls when to check (avoids firing on each keystroke)
if st.button("Check Password"):
    if not password:
        st.warning("⚠️ Please enter a password first.")
    else:
        # Immediately hash and clear plaintext variable
        sha1_hash = hash_password(password)
        password = None
        try:
            del password
        except Exception:
            pass

        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]

        # Optionally cache API responses by prefix
        if cache_api:
            @st.cache_data(ttl=60 * 60)
            def fetch_api(pref):
                return get_pwned_api_data(pref)
            api_text = fetch_api(prefix)
        else:
            api_text = get_pwned_api_data(prefix)

        with st.spinner("Checking breach database..."):
            # small delay for UX; optional
            time.sleep(0.2) 
            count = parse_pwned_count(api_text or "", suffix)

        # clear sha1
        sha1_hash = None
        try:
            del sha1_hash
        except Exception:
            pass

        if api_text is None:
            st.error("Could not reach HIBP API (network or server error). Try again later.")
        elif count > 0:
            st.warning(f"🚨 This password was found **{count:,}** times in data breaches.")
            st.markdown("""
            **What to do next:**  
            - Stop using this password anywhere.  
            - Change it on important accounts now.  
            - Use a password manager to create strong, unique passwords.  
            - Enable multi-factor authentication (MFA) where possible.
            """)
        else:
            st.success("✅ Good news — this password was NOT found in the HIBP dataset.")

        with st.expander("Developer: raw API response (first 1000 chars)"):
            st.code(api_text[:1000] if api_text else "No data", language="text")

else:
    st.info("Type a password and click 'Check Password' to begin.")
