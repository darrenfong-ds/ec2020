import re
import zlib
from collections import Counter
from pathlib import Path

PDF_EXAM = Path('2015 to 2025_merged.pdf')


def decode_pdf_string(bs: bytes) -> str:
    out=[];i=0
    while i<len(bs):
        b=bs[i]
        if b==0x5c:
            i+=1
            if i>=len(bs):
                break
            c=bs[i]
            mapping={ord('n'):'\n',ord('r'):'\r',ord('t'):'\t',ord('b'):'\b',ord('f'):'\f',ord('('):'(',ord(')'):')',ord('\\'):'\\'}
            if c in mapping:
                out.append(mapping[c]); i+=1; continue
            if 48<=c<=55:
                octd=bytes([c]); i+=1
                for _ in range(2):
                    if i<len(bs) and 48<=bs[i]<=55:
                        octd += bytes([bs[i]]); i+=1
                    else:
                        break
                out.append(chr(int(octd,8))); continue
            out.append(chr(c)); i+=1; continue
        out.append(chr(b)); i+=1
    return ''.join(out)


def extract_pdf_text(pdf_path: Path) -> str:
    data = pdf_path.read_bytes()
    str_pat = re.compile(rb'\((?:\\.|[^\\()])*\)')
    chunks=[]
    for m in re.finditer(rb'stream\r?\n', data):
        s=m.end(); e=data.find(b'endstream', s)
        if e==-1:
            continue
        raw=data[s:e]
        if raw.endswith(b'\r\n'):
            raw=raw[:-2]
        elif raw.endswith(b'\n'):
            raw=raw[:-1]
        try:
            d=zlib.decompress(raw)
        except Exception:
            continue
        if b'Tj' not in d and b'TJ' not in d:
            continue
        strings=[decode_pdf_string(sm.group()[1:-1]) for sm in str_pat.finditer(d)]
        t=''.join(strings)
        if t:
            chunks.append(t)
    return '\n'.join(chunks)


def filter_lines(text: str) -> str:
    out=[]
    for ln in text.splitlines():
        ln=''.join(ch for ch in ln if 32<=ord(ch)<=126)
        ln=re.sub(r'\s+',' ',ln).strip()
        if not ln:
            continue
        words=re.findall(r'[A-Za-z]{3,}',ln)
        if len(words)<3:
            continue
        good=sum(c.isalpha() or c.isspace() or c.isdigit() or c in '(),.:;/-' for c in ln)
        if good/len(ln)<0.85:
            continue
        out.append(ln)
    return '\n'.join(out)


raw = extract_pdf_text(PDF_EXAM)
text = filter_lines(raw)
pat=re.compile(r'\((\d+) ?marks\)')
rows=[]
for m in pat.finditer(text):
    marks=int(m.group(1))
    pre=text[max(0,m.start()-4000):m.start()]
    ys=re.findall(r'University of London\s+(20\d{2})',pre)
    year=int(ys[-1]) if ys else None
    snippet=text[max(0,m.start()-240):min(len(text),m.end()+160)].lower()
    rows.append((year,marks,snippet))

keywords={
'Hypothesis testing & inference':['test','null hypothesis','significance','confidence interval','t-stat','f-test','wald'],
'OLS assumptions/properties':['ols','unbiased','consisten','gauss','blue'],
'Functional form & logs':['log','logarithm','elasticity','adl','error correction','koyck'],
'Stationarity / unit roots / cointegration':['stationary','unit root','cointegr','i(1)','spurious regression'],
'Binary choice models (LPM/Logit/Probit)':['probit','logit','linear probability','binary','probability model'],
'Heteroskedasticity':['heterosk','white','robust standard'],
'Autocorrelation / serial correlation':['autocorrel','serial correlation','ar(1)','durbin'],
'Maximum likelihood estimation':['maximum likelihood','likelihood','ml estimator'],
'Dummy variables / qualitative regressors':['dummy','qualitative','intercept','slope change'],
'Instrumental variables & 2SLS':['instrumental variable','2sls','two-stage','endogenous','identification','simultaneous'],
}

stats=[]
for topic,arr in keywords.items():
    freq=0; mx=0; y1=0; y2=0
    for y,m,s in rows:
        if any(a in s for a in arr):
            freq+=1; mx=max(mx,m)
            if y and y<=2022: y1+=1
            if y and y>=2023: y2+=1
    stats.append((topic,freq,mx,y1,y2))

stats.sort(key=lambda x:(-x[1],-x[2]))

refs={
'Hypothesis testing & inference':'1.2.Contentofchapter ... FundamentalsofHypothesisTesting',
'OLS assumptions/properties':'3.Simpleregressionmodel; 4.Multipleregressionanalysis:Estimation',
'Functional form & logs':'3.2.Contentofchapter ... useoflogarithms',
'Stationarity / unit roots / cointegration':'Chapter13Regressionanalysiswithtimeseriesdata',
'Binary choice models (LPM/Logit/Probit)':'Learning outcomes ... logit and probit',
'Heteroskedasticity':'Learning outcomes ... tests for violations; remedial measures',
'Autocorrelation / serial correlation':'Learning outcomes ... time-series problems such as autocorrelation',
'Maximum likelihood estimation':'Learning outcomes ... principles of maximum likelihood estimation',
'Dummy variables / qualitative regressors':'Chapter6Multipleregressionanalysis:Furtherissuesanduseofqualitativeinformation',
'Instrumental variables & 2SLS':'Learning outcomes ... use of instrumental variables',
}

lines=[]
lines.append('# EC2020 Exam Trend Analysis (Best-effort from provided PDFs)')
lines.append('')
lines.append('## Data coverage note')
lines.append('- Parsed marks-tagged question text from `2015 to 2025_merged.pdf` using a custom PDF stream extractor.')
lines.append('- Years found with usable marks snippets: 2015, 2016, 2017, 2018, 2019, 2020, 2022, 2023, 2024.')
lines.append('- **No reliable 2025 marks-tagged snippets were extractable** from the provided PDF text streams; 2025 conclusions are therefore inferred conservatively from 2023-2024 pattern continuation only.')
lines.append('')
lines.append('## Topic frequency table')
lines.append('| Topic | Frequency | Max Marks | Textbook Section Reference |')
lines.append('|---|---:|---:|---|')
for t,f,m,y1,y2 in stats:
    if f==0: continue
    lines.append(f'| {t} | {f} | {m} | {refs[t]} |')

lines.append('')
lines.append('## Trend split (2015-2022 vs 2023-2025*)')
lines.append('(Using **average mentions per available year** to avoid window-length bias.)')
lines.append('')
lines.append('| Topic | 2015-2022 avg/year | 2023-2025* avg/year | Direction |')
lines.append('|---|---:|---:|---|')
for t,f,m,y1,y2 in stats:
    if f==0: continue
    left=round(y1/8,1)
    right=round(y2/2,1)
    if right>left: d='Higher recent intensity'
    elif right<left: d='Lower recent intensity'
    else: d='Flat'
    lines.append(f'| {t} | {left} | {right} | {d} |')

lines.append('')
lines.append('## Revision priorities (exam importance)')
for i,(t,f,m,_,_) in enumerate(stats,1):
    if f==0: continue
    score=f*m
    lines.append(f'{i}. **{t}** (importance score ~ {score})')

lines.append('')
lines.append('## How to read the table')
lines.append('- **Frequency** = how often that topic was matched in marks-tagged snippets.')
lines.append('- **Max Marks** = highest single-part allocation observed for that topic.')
lines.append('- Prioritise topics with both high frequency and high max marks (high expected exam payoff).')

lines.append('')
lines.append('## 2026 revision plan (ranked by exam importance)')
lines.append('1. **Hypothesis testing & inference**: absolutely know test setup, null/alternative, test-statistic choice, interpretation and assumptions.')
lines.append('2. **OLS assumptions/properties**: absolutely know unbiasedness/consistency logic, Gauss-Markov assumptions, and what breaks them.')
lines.append('3. **Functional form & logs**: absolutely know level-log/log-log interpretations, elasticity and semi-elasticity, ADL/ECM transformations.')
lines.append('4. **Stationarity / unit roots / cointegration**: know unit-root testing intuition, spurious regression, and cointegration logic.')
lines.append('5. **Binary choice models (LPM/Logit/Probit)**: know when LPM fails and why probit/logit are preferred; know interpretation of marginal effects.')
lines.append('6. **Heteroskedasticity + Autocorrelation**: know diagnostics, consequences, and remedies (robust SE, GLS-style fixes, model re-specification).')
lines.append('7. **IV/2SLS + simultaneous equations**: know identification conditions, first stage, exclusion restrictions, and consistency argument.')
lines.append('8. **Dummy variables + interactions**: know intercept/slope-shift interpretation and testing framework.')
lines.append('9. **Maximum likelihood (general)**: review core properties and score/LR intuition.')

lines.append('')
lines.append('## What to skip vs master (time-constrained)')
lines.append('- **Master**: derivation skeletons used repeatedly (OLS properties, hypothesis testing, IV consistency, unit-root/cointegration workflow).')
lines.append('- **Glance-through**: long historical examples or very niche model variants that appear once and do not carry high-mark parts.')

lines.append('')
lines.append('## Chapter-level must-know concept checklist')
lines.append('- **Chapter 1 (Mathematics and statistics refresher)**: probability basics, estimators, variance, CI/test fundamentals.')
lines.append('- **Chapter 3 (Simple regression model)**: OLS formulas, assumptions, interpretation, standard errors, t/F testing.')
lines.append('- **Chapter 4 (Multiple regression analysis: Estimation)**: partial effects, omitted variable bias intuition, fit/residual diagnostics.')
lines.append('- **Chapter 6 (Further issues and qualitative information)**: dummy-variable design, interaction effects, interpretation/testing.')
lines.append('- **Chapter 13 (Regression with time series data)**: stationarity, serial correlation, dynamic forms (ADL/ECM).')
lines.append('- **Cointegration/unit-root block**: always connect mechanics to economic interpretation (long-run relation vs spurious fit).')

Path('exam_trend_analysis_2015_2025.md').write_text('\n'.join(lines))
print('Wrote exam_trend_analysis_2015_2025.md with',len(rows),'marks snippets')
