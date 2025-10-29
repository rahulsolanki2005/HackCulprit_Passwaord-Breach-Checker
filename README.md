# 🔐 Password Breach Checker

### **Hack Culprit Virtual Internship - Project Report**

**Project Title:** Password Breach Checker  
**Submitted by:** Rahul Solanki  
**Internship Role:** Virtual Intern  
**Organization:** Hack Culprit  
**GitHub Profile:** https://github.com/rahulsolanki2005                           
**Project Duration:** 7/10/2025 – 14/10/2025                                
**Project Repository:** https://github.com/rahulsolanki2005/HackCulprit_Passwaord-Breach-Checker

---

## 🧠 Executive Summary
The **Password Breach Checker** is a lightweight, privacy-focused tool built using **Python** and **Streamlit** during the Hack Culprit Virtual Internship.  
It checks whether a password has appeared in known data breaches using the **Have I Been Pwned (HIBP)** API — without revealing the actual password, thanks to **k-anonymity hashing** (only the first 5 characters of the SHA-1 hash are sent to the API).

---

## 🚨 Problem Statement
In the modern digital landscape, password reuse and weak credentials are a major threat. Users often don’t know if their password has already been leaked.  
This project helps them verify that securely, using a fast and privacy-preserving check against HIBP’s database.

---

## 🎯 Project Objectives
- Get practical experience in secure application development.  
- Apply cryptography (SHA-1 hashing) safely.  
- Learn API integration and error handling.  
- Strengthen Git/GitHub collaboration skills.  
- Deliver a functional cybersecurity tool that addresses a real-world problem.

---

## 🧩 Development Approach
| Stage | Description |
|--------|--------------|
| **1. Requirement Analysis & Planning** | Defined project scope, toolchain, and API structure. |
| **2. Development** | Built core logic in `breach_checker.py` and UI in `app.py`. |
| **3. Testing & Debugging** | Verified functionality, handled API/network edge cases. |
| **4. Documentation & Deployment** | Structured code, wrote README, and prepared for GitHub. |

---

## ⚙️ Tools & Technologies

| Category | Tools / Technologies Used |
|-----------|----------------------------|
| Programming | Python |
| UI Framework | Streamlit |
| Networking | Requests |
| Hashing | hashlib (SHA-1) |
| Dev Tools | Git, GitHub, VS Code |

---

## 🧰 Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Steps to Run
```bash
# Clone the repository
git clone https://github.com/rahulsolanki2005/HackCulprit_Passwaord-Breach-Checker

# (Optional) create & activate a virtual environment
python -m venv myenv
# Windows
myenv\Scripts\activate
# macOS / Linux
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt
# or manually:
pip install streamlit requests

# Run the Streamlit app
streamlit run app.py
Note: Passwords are hashed locally — only the first 5 characters of the SHA-1 hash are sent to the HIBP API (k-anonymity model).

```

## 🌟 Key Features
  - 🔐 Privacy-preserving password breach checking.
  - ⚡ Fast results via cached API responses.
  - 🧠 Secure local SHA-1 hashing, no password ever leaves your machine.
  - 🧾 Clean and modular Python codebase.
  - 💬 Developer expander to view raw API response for debugging.

## 📸 Demonstration
  - Run the app → type any password → click Check Password.
  - The tool will display:
     : 🚨 Warning if the password was found in breaches (with count).
  - ✅ Success message if not found.


## 🧗 Challenges Faced
  - Dealing with network failures or API timeouts.
  - Parsing the HIBP response efficiently (line format HASH_SUFFIX:COUNT).
  - Avoiding in-memory retention of plaintext passwords.
  - Ensuring responsive and clean Streamlit UX.

## 🚀 Future Enhancements
  - Deploy app to cloud platforms (e.g., Render, Heroku).
  - Add batch password check (from a local CSV file).
  - Integrate unit tests and CI/CD pipeline.
  - Add Dockerfile for reproducibility.
  - Implement dark mode UI and localization.

## 🏁 Conclusion
  - The Password Breach Checker provided practical exposure to secure app design, Python web development, and cybersecurity principles.
  - It’s a compact, educational, and functional project that demonstrates both privacy-first thinking and professional coding discipline.

## 🙏 Acknowledgements
  - Thanks to the Hack Culprit Team for the virtual internship opportunity, mentorship, and support.
  - Special thanks to peers who provided guidance during the development process.

## 📜 License
  - This project is licensed under the MIT License — see LICENSE for details.
