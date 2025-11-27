# Credit Risk Assessment Using Probability and Statistics

## Overview

This project demonstrates a **Credit Risk Assessment simulation** using **Python**, **probability theory**, and **statistical modeling**. The goal is to evaluate the risk of loan defaults in a portfolio of borrowers and estimate the **Expected Loss (EL)** for each loan.

The project covers:

- Simulating a portfolio of borrowers with realistic features.
- Calculating the **Probability of Default (PD)** based on risk factors.
- Simulating default events using **binomial distribution**.
- Estimating **Loss Given Default (LGD)** and **Expected Loss (EL)**.
- Portfolio-level metrics and summaries.

---

## Features

1. **Simulated Borrower Dataset**  
   - `income` – Annual income of the borrower  
   - `loan_amount` – Amount of loan granted  
   - `credit_score` – Credit score (300–900)  
   - `age` – Borrower age  
   - `loan_to_income` – Loan-to-income ratio  

2. **Probability of Default (PD) Calculation**  
   - Uses a simplified formula to simulate default probability:  
     ```
     PD = 0.05 + 0.4 * loan_to_income + 0.0005 * (700 - credit_score)
     ```
   - Values are clipped to `[0, 1]` to ensure valid probabilities.

3. **Default Simulation**  
   - Uses `np.random.binomial` to simulate binary default events (0 = no default, 1 = default).

4. **Loss Calculation**  
   - `LGD` (Loss Given Default) is assumed constant (e.g., 60%).  
   - `EAD` (Exposure at Default) is the loan amount.  
   - **Expected Loss (EL) per borrower** is calculated as:  
     ```
     EL = PD * LGD * EAD
     ```

5. **Portfolio-Level Metrics**  
   - Total Expected Loss  
   - Average Probability of Default  
   - Average Expected Loss per borrower

---

## Requirements

- Python 3.x  
- Libraries:
  - `numpy`
  - `pandas`

Install dependencies using:

```bash
pip install numpy pandas
