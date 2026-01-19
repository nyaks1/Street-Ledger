#  Street Ledger 🇿🇦
> **Formalizing South Africa’s informal economy through decentralized P2P debt tracking and Stablecoin settlement.**

 **W3Node 2026 Hackathon Submission** **Track:** Payments & Stablecoins

---

## 📽️ Demo Video
*[Link to your 3-minute Google Drive/YouTube demo goes here once recorded]*

---

##  Problem Statement: The "Invisible" Debt Trap
In South Africa, the informal economy is the heartbeat of our communities, valued at over **R900 billion annually**. However, millions of transactions—from taxi fares to small loans between friends and spaza shop credit—happen in cash and are recorded on scraps of paper or purely by memory.

### **Three Major Issues:**
* **Forgetfulness & Friction:** Small "street debts" are often forgotten, leading to social friction and loss of income.
* **Financial Invisibility:** Unrecorded transactions prevent users from proving creditworthiness to banks.
* **High Transaction Costs:** Traditional bank fees often exceed the value of the small debt itself.

##  Our Solution: Street Ledger
Street Ledger is a lightweight, Python-powered decentralized ledger that allows users to log "street-level" debts instantly.

**Key Innovation:** By integrating Stablecoins (**USDC/PYUSD**), we allow users to settle debts for fractions of a cent in fees. Every settled debt is recorded on the blockchain, building a **Decentralized Credit Score**—turning "invisible" street trust into "visible" financial data.

---

##  Technical Stack
* **Backend:** Python 3.x
* **API Framework:** FastAPI
* **Database:** SQLite (Local storage)
* **Web3 Integration:** Web3.py (Base Sepolia Testnet)
* **Smart Contracts:** Solidity



---

##  User Flow
1. **Log a Debt:** User A logs a R20 debt for "Taxi Fare" via the Python API.
2. **Track:** The debt is stored in a local SQLite database, visible to both parties.
3. **Settle:** User B clicks "Settle," triggering a `Web3.py` script to move USDC to User A.
4. **Verify:** Once confirmed on-chain, the debt is automatically marked as **PAID**.

---

## 📦 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/nyaks1/Street-Ledger.git
cd Street-Ledger
2. Install dependencies
Bash

pip install -r requirements.txt
3. Run the API
Bash

uvicorn main:app --reload
Navigate to http://127.0.0.1:8000/docs to test the endpoints.

🗺️ Roadmap
[x] Initial Python logic & Debt classes

[ ] FastAPI endpoint integration

[ ] SQLite database implementation for persistent logging

[ ] Web3.py connection to Base Sepolia Testnet

[ ] Frontend Mobile UI (Planned for v2.0)

# The Team
We are a duo of hard-working developers from the WeThinkCode_ community, dedicated to using technology to solve local South African challenges.
