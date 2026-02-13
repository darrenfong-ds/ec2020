# EC2020 Exam Trend Analysis (Best-effort from provided PDFs)

## Data coverage note
- Parsed marks-tagged question text from `2015 to 2025_merged.pdf` using a custom PDF stream extractor.
- Years found with usable marks snippets: 2015, 2016, 2017, 2018, 2019, 2020, 2022, 2023, 2024.
- **No reliable 2025 marks-tagged snippets were extractable** from the provided PDF text streams; 2025 conclusions are therefore inferred conservatively from 2023-2024 pattern continuation only.

## Topic frequency table
| Topic | Frequency | Max Marks | Textbook Section Reference |
|---|---:|---:|---|
| Hypothesis testing & inference | 579 | 10 | 1.2.Contentofchapter ... FundamentalsofHypothesisTesting |
| OLS assumptions/properties | 520 | 10 | 3.Simpleregressionmodel; 4.Multipleregressionanalysis:Estimation |
| Functional form & logs | 308 | 10 | 3.2.Contentofchapter ... useoflogarithms |
| Stationarity / unit roots / cointegration | 181 | 10 | Chapter13Regressionanalysiswithtimeseriesdata |
| Binary choice models (LPM/Logit/Probit) | 151 | 9 | Learning outcomes ... logit and probit |
| Heteroskedasticity | 149 | 8 | Learning outcomes ... tests for violations; remedial measures |
| Autocorrelation / serial correlation | 132 | 8 | Learning outcomes ... time-series problems such as autocorrelation |
| Maximum likelihood estimation | 74 | 8 | Learning outcomes ... principles of maximum likelihood estimation |
| Dummy variables / qualitative regressors | 72 | 8 | Chapter6Multipleregressionanalysis:Furtherissuesanduseofqualitativeinformation |
| Instrumental variables & 2SLS | 69 | 10 | Learning outcomes ... use of instrumental variables |

## Trend split (2015-2022 vs 2023-2025*)
(Using **average mentions per available year** to avoid window-length bias.)

| Topic | 2015-2022 avg/year | 2023-2025* avg/year | Direction |
|---|---:|---:|---|
| Hypothesis testing & inference | 9.6 | 4.5 | Lower recent intensity |
| OLS assumptions/properties | 10.2 | 12.5 | Higher recent intensity |
| Functional form & logs | 3.9 | 3.5 | Lower recent intensity |
| Stationarity / unit roots / cointegration | 3.2 | 5.5 | Higher recent intensity |
| Binary choice models (LPM/Logit/Probit) | 3.4 | 0.0 | Lower recent intensity |
| Heteroskedasticity | 1.9 | 1.0 | Lower recent intensity |
| Autocorrelation / serial correlation | 2.8 | 2.0 | Lower recent intensity |
| Maximum likelihood estimation | 2.4 | 0.0 | Lower recent intensity |
| Dummy variables / qualitative regressors | 1.8 | 0.0 | Lower recent intensity |
| Instrumental variables & 2SLS | 2.8 | 1.0 | Lower recent intensity |

## Revision priorities (exam importance)
1. **Hypothesis testing & inference** (importance score ~ 5790)
2. **OLS assumptions/properties** (importance score ~ 5200)
3. **Functional form & logs** (importance score ~ 3080)
4. **Stationarity / unit roots / cointegration** (importance score ~ 1810)
5. **Binary choice models (LPM/Logit/Probit)** (importance score ~ 1359)
6. **Heteroskedasticity** (importance score ~ 1192)
7. **Autocorrelation / serial correlation** (importance score ~ 1056)
8. **Maximum likelihood estimation** (importance score ~ 592)
9. **Dummy variables / qualitative regressors** (importance score ~ 576)
10. **Instrumental variables & 2SLS** (importance score ~ 690)

## How to read the table
- **Frequency** = how often that topic was matched in marks-tagged snippets.
- **Max Marks** = highest single-part allocation observed for that topic.
- Prioritise topics with both high frequency and high max marks (high expected exam payoff).

## 2026 revision plan (ranked by exam importance)
1. **Hypothesis testing & inference**: absolutely know test setup, null/alternative, test-statistic choice, interpretation and assumptions.
2. **OLS assumptions/properties**: absolutely know unbiasedness/consistency logic, Gauss-Markov assumptions, and what breaks them.
3. **Functional form & logs**: absolutely know level-log/log-log interpretations, elasticity and semi-elasticity, ADL/ECM transformations.
4. **Stationarity / unit roots / cointegration**: know unit-root testing intuition, spurious regression, and cointegration logic.
5. **Binary choice models (LPM/Logit/Probit)**: know when LPM fails and why probit/logit are preferred; know interpretation of marginal effects.
6. **Heteroskedasticity + Autocorrelation**: know diagnostics, consequences, and remedies (robust SE, GLS-style fixes, model re-specification).
7. **IV/2SLS + simultaneous equations**: know identification conditions, first stage, exclusion restrictions, and consistency argument.
8. **Dummy variables + interactions**: know intercept/slope-shift interpretation and testing framework.
9. **Maximum likelihood (general)**: review core properties and score/LR intuition.

## What to skip vs master (time-constrained)
- **Master**: derivation skeletons used repeatedly (OLS properties, hypothesis testing, IV consistency, unit-root/cointegration workflow).
- **Glance-through**: long historical examples or very niche model variants that appear once and do not carry high-mark parts.

## Chapter-level must-know concept checklist
- **Chapter 1 (Mathematics and statistics refresher)**: probability basics, estimators, variance, CI/test fundamentals.
- **Chapter 3 (Simple regression model)**: OLS formulas, assumptions, interpretation, standard errors, t/F testing.
- **Chapter 4 (Multiple regression analysis: Estimation)**: partial effects, omitted variable bias intuition, fit/residual diagnostics.
- **Chapter 6 (Further issues and qualitative information)**: dummy-variable design, interaction effects, interpretation/testing.
- **Chapter 13 (Regression with time series data)**: stationarity, serial correlation, dynamic forms (ADL/ECM).
- **Cointegration/unit-root block**: always connect mechanics to economic interpretation (long-run relation vs spurious fit).