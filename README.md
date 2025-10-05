# SDMO Project 1 – Identifying unique developers in OSS

repositories

This project aims to identify duplicate developer identities across commits in open-source repositories,
based on the approach of Bird et al. (MSR 2006).

## Structure

- `src/` — all source code (collection, preprocessing, baseline, improved methods, evaluation)
- `data/` — input and output datasets
- `tests/` — unit tests for each module
- `reports/` — documentation and report drafts

## Setup

1. Create a Python virtual environment (Python ≥ 3.10).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```