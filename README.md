## Chandamama Downloader (Python Version)

This project is a Python-based port of the **Chandamama Downloader**, originally written in JavaScript. It is designed to archive issues of the classic "Chandamama" magazine from the official resource archives.

---

### 📌 Credits & References

This implementation is based on the logic and URL structures found in the original repository:

* **Original Author:** Srikanth Bandaru
* **Original Code:** [srikanthbandaru/chandamama-downloader](https://github.com/srikanthbandaru/chandamama-downloader#)

---

### 🚀 Features

* **Automated Downloading:** Iterates through years (1947–2007) and months (01–12) to fetch PDF issues.
* **Corrected URL Formatting:** Uses the updated resource path structure: `http://chandamama.in/resources/{language}/{year}/Chandamama-{year}-{month}.pdf`.
* **Zero-Padding:** Automatically formats months (e.g., `01` instead of `1`) to match the server's naming convention.
* **Direct Downloading:** Unlike the original JavaScript version which requires a CORS proxy for browser execution, this Python version connects directly to the server.

---

### 🛠️ Setup & Usage

#### 1. Prerequisites

Ensure you have Python 3.9+ installed. You will need the `requests` library:

```bash
pip install -r requirements.txt
```

#### 2. Configuration

The script is currently configured for the **English** edition:

* **Language:** `english`
* **Year Range:** 1947 to 2007

#### 3. Running the Script

Simply execute the main Python file:

```bash
python chandamama_downloader.py
```

All files will be saved into a local folder named `chandamama_english`.

---

### 📖 PDF to CBR Conversion (Optional)

If you prefer reading these on a comic book reader, you can convert the downloaded PDFs to **.cbr** files.

* **Process:** The script extracts PDF pages as JPEG images, archives them into a RAR/ZIP structure, and renames the extension to `.cbr`.
* **Requirements:** Requires `pdf2image` and `patool`.
