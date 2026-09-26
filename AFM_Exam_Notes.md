# Advanced Financial Management — Complete Exam Notes

**Purpose.** A dense, exam-ready pack prepared from all uploaded class materials: M1–M6 teaching PDFs, Module 1 TVM, the supplementary M2 handout, both M3 practice/teaching sets, the M6 question set, and *Question & Solution.docx*.

**Modest disclaimer.** Based on uploaded class materials; no outcome guarantee.

# RAPID FORMULA AND DECISION SHEET

## Page 1 — Notation used everywhere

| Symbol | Meaning | Timing/unit rule |
|---|---|---|
| t, n | time period; total periods/project life | T0 is now; T1 is end of period 1 unless stated |
| CFₜ | net cash flow at time t | inflow +; outflow − |
| PV₀, FVₙ | value now; value at end of n | always state valuation date |
| r, k | return/discount rate per period | match rate period to cash-flow period |
| PMT | equal periodic cash flow | ordinary annuity means period-end |
| I₀ | initial investment at T0 | normally an outflow |
| τ | corporate tax rate | state same-year or delayed payment |
| g, h | specific growth/inflation; general inflation | distinguish current-price from Year-1 data |
| WCₜ, ΔWCₜ | required working-capital balance; change | invest increases; recover balance at end |
| EBIT, EBT, PAT | operating profit; profit before tax; profit after tax | EBT = EBIT − interest |
| D, E, V | market value of debt, equity, firm | V = D + E |
| Kd, Ke, K₀ | debt cost, equity cost, overall cost/WACC | use market-value weights unless told otherwise |
| Rf, Rm, β | risk-free return, market return, systematic-risk beta | CAPM uses market risk premium Rm − Rf |
| σ, CV | standard deviation; coefficient of variation | CV = σ/expected value |
| N | ordinary shares outstanding | keep share units consistent |
| EPS, P₀ | earnings per share; market price per share | P/E = P₀/EPS |
| x, y, a, b | sales; working capital; intercept; slope | regression y = a + bx |
| q | M&A exchange ratio | acquirer shares issued per target share |

**Universal timing line:** `T0 | T1 | T2 | … | Tn`. Put every cash flow under its actual date before choosing a formula.

## Page 1 — TVM, valuation and capital budgeting

| Need | Use this correct form | Decision/check |
|---|---|---|
| Lump-sum FV | FVₙ = PV₀(1+r)ⁿ | compounding moves right |
| Lump-sum PV | PV₀ = FVₙ/(1+r)ⁿ | discounting moves left |
| Nominal j, m compounds/year | FV = PV(1+j/m)ᵐⁿ | j is assumed nominal |
| Uneven FV, end deposits | FVₙ = Σ CFₜ(1+r)ⁿ⁻ᵗ | exponents n−1 down to 0 |
| Uneven FV, beginning deposits | FVₙ = Σ CFₜ(1+r)ⁿ⁻ᵗ⁺¹ | **Use this correct form:** exponents n down to 1 |
| Ordinary-annuity FV | FVₙ = PMT[(1+r)ⁿ−1]/r | each payment at period-end |
| Ordinary-annuity PV | PV₀ = PMT[1−(1+r)⁻ⁿ]/r | one period before first receipt |
| NPV | NPV = Σ CFₜ/(1+k)ᵗ | accept if NPV > 0 |
| Fisher relation | 1+i = (1+r)(1+h) | nominal flows with nominal rate |
| IRR interpolation | IRR ≈ L + NPV_L/(NPV_L−NPV_H) × (H−L) | accept conventional project if IRR > k |
| Profitability index | PI = PV future inflows/PV outflows | accept if PI > 1 |
| Discounted payback | full years + unrecovered PV/next-year PV | shorter is less exposed; still ignores later value |

**Integrated NPV order:** initial fixed asset → opening WC → nominal operating lines → depreciation/tax → after-tax operating CF → WC changes → scrap/disposal tax → final WC recovery → discount.

\pagebreak

## Page 2 — Leverage, financing and capital structure

**Profit ladder:** Sales − variable cost = **Contribution**; Contribution − fixed operating cost = **EBIT**; EBIT − interest = **EBT**; EBT − tax = **PAT**; PAT/N = **EPS**.

| Need | Formula | Interpretation |
|---|---|---|
| Operating leverage | DOL = Contribution/EBIT | sales sensitivity of EBIT |
| Financial leverage | DFL = EBIT/EBT | EBIT sensitivity of EPS |
| Combined leverage | DCL = Contribution/EBT = DOL×DFL | sales sensitivity of EPS |
| EPS plan | EPS = (EBIT−I)(1−τ)/N | choose higher EPS at stated EBIT only |
| EBIT indifference | (EBIT−I₁)/N₁ = (EBIT−I₂)/N₂ | common tax factor cancels |
| CAPM | Ke = Rf + β(Rm−Rf) | required return for systematic risk |
| After-tax WACC | K₀ = (E/V)Ke + (D/V)Kd(1−τ) | market-value weights |

| Theory | Calculation order | Prediction/decision |
|---|---|---|
| Net Income (no tax) | I=KdD; NI=EBIT−I; E=NI/Ke; V=E+D; K₀=EBIT/V | Kd, Ke constant; more debt raises V and lowers K₀ |
| Traditional | repeat NI calculation at each debt level | moderate debt helps; choose maximum V/minimum K₀ |
| Net Operating Income | V=EBIT/K₀; E=V−D; NI=EBIT−I; Ke=NI/E | V and K₀ constant; Ke rises |
| MM without tax | VU=EBIT/KeU; VL=VU; E=VL−D | leverage does not alter V |
| MM with tax | VU=EBIT(1−τ)/KeU; **VL=VU+τD** | tax shield increases value |

**MM equity costs:** no tax `KeL = KeU + (KeU−Kd)(D/E)`; with tax `KeL = KeU + (KeU−Kd)(1−τ)(D/E)`.

**Decision split:** EPS question → maximize EPS at given EBIT. Valuation question → apply named theory. Financing recommendation → mention return **and** risk; EPS alone is not shareholder wealth.

## Page 2 — Risk analysis

| Method | Formula/step | Decision |
|---|---|---|
| Expected value | E(X)=Σxp | probability-weighted mean |
| Variance/SD | σ²=Σx²p−[E(X)]²; σ=√σ² | lower means lower absolute risk |
| Coefficient of variation | CV=σ/E(X) | lower risk per unit of expected return |
| Certainty equivalent | CE(CFₜ)=αₜE(CFₜ); discount at Rf | accept CE-NPV > 0 |
| Risk-adjusted rate | RADR=Rf+β(Rm−Rf) | discount project CF at RADR |
| Sensitivity margin | base NPV/PV of affected variable ×100 | lower margin = more sensitive |
| Life sensitivity | (base life−break-even life)/base life | report as positive allowable reduction |
| Rate sensitivity | IRR−current k | state percentage-point headroom |

**Do not double-count risk:** use CE-adjusted cash flows at Rf **or** unadjusted cash flows at RADR, unless the question explicitly says otherwise.

\pagebreak

## Page 3 — Working capital and M&A

**Working capital:** `WC = current assets − current liabilities`.

**Cash-conversion cycle:**
`CCC = R + W + F + D − C`, where
`R = avg raw material / daily raw-material consumption`,
`W = avg WIP / daily cost of production`,
`F = avg finished goods / daily COGS`,
`D = avg receivables / daily credit sales`,
`C = avg payables / daily credit purchases`.

`WCR = CCC × annual operating cost/365 + separately stated contingency cash`.

**Trade-credit cost (365-day assumption):**
`cost = discount/(100−discount) × 365/(final due day−discount day)`.

**Regression forecast:** `WC = a + b(Sales)`; `b = Σ(x−x̄)(y−ȳ)/Σ(x−x̄)²`; `a = ȳ−bx̄`. Keep x and y in their stated lakh/million units.

**M&A exchange:** define `q = acquirer shares per target share`.

| Need | Formula | Trap |
|---|---|---|
| Ratio by metric M | q = M_target/M_acquirer | announce ratio orientation |
| New/total shares | q×target shares; acquirer shares + new shares | do not round q early |
| Combined EPS | combined earnings/post-merger shares | add synergy only if supported |
| Target EPS on acquirer-share basis | **target EPS/q** | division, not multiplication |
| Entitlement per old target share | q×post-merger EPS | different comparison basis |
| Offer value | q×acquirer pre-deal price | premium = offer−target price |
| P/E and price | P/E=P₀/EPS; P₀=P/E×EPS | retain exact EPS |
| Synergy value | VAB−(VA+VB) | positive only if combined value is larger |

**Decision order for every numerical answer:**
1. **Given/data:** dates, units, assumptions and unknown.
2. **Formula:** one consistent formula.
3. **Working/table:** substitution with full precision.
4. **Decision/interpretation:** amount, date, accept/reject or comparison.

**High-risk source corrections to remember:** beginning deposits compound for n…1 periods; Contribution/EBT is **DCL**; Plan Y debt is ₹10 lakh; MM-tax adds `VU + τD`; tax, depreciation and WC must sit in their proper time columns; life sensitivity is a positive reduction margin; use 365 days unless told otherwise; M&A target EPS conversion divides by q; do not create market-cap gain by early rounding.

\pagebreak

# TABLE OF CONTENTS

[TOC]

\pagebreak

# MODULE 1 — FINANCE FUNCTION AND TIME VALUE OF MONEY

## 1.1 Financial environment and finance function

### WRITE THIS IN THE EXAM — Financial management

**Definition:** Financial management is the **efficient and effective management of money** to achieve the **objectives of the organisation**.

1. **Planning:** decide financial goals, policies and actions.
2. **Forecasting:** estimate future sales, costs, cash flows and finance needs.
3. **Resource allocation:** direct limited funds to the best uses.
4. **Performance management and control:** compare actual performance with plans and correct deviations.
5. **Financial reporting:** communicate financial position and performance to users.

The uploaded framework groups these roles as **Enabling** (planning, forecasting, resource allocation), **Shaping** (performance management and control), and **Narrating** (financial reporting). In the digital-age “diamond” model, automation supports routine work and allows finance to contribute more to shaping decisions and explaining results.

### WRITE THIS IN THE EXAM — Financial environment

1. **Financial markets:** places/channels where claims are issued and traded. The **money market** handles short-term funds; the **capital market** handles long-term funds. The **primary market** issues new securities; the **secondary market** trades existing securities.
2. **Financial institutions:** intermediaries such as banks, investment companies, insurance companies and pension funds.
3. **Financial instruments:** contractual claims, chiefly **equity**, **debt** and **derivatives**.
4. **Regulatory framework:** rules and supervision by bodies such as SEBI/SEC and central banks such as RBI/Federal Reserve.

### WRITE THIS IN THE EXAM — Fundamental ethical principles

1. **Integrity:** be straightforward and honest.
2. **Objectivity:** do not allow bias, conflict of interest or improper influence.
3. **Professional competence:** maintain knowledge and perform work carefully.
4. **Confidentiality:** protect information unless disclosure is authorised or legally required.
5. **Professional behaviour:** follow laws and avoid conduct that discredits the profession.

**COMMON MISTAKES:** listing activities without their role groups; confusing primary with secondary markets; writing “competence” without the need for due care; describing automation as replacing every finance judgement.
**Memory aid:** **M-I-I-R; E-S-N; I-O-C-C-P** = markets, institutions, instruments, regulation; enabling, shaping, narrating; ethics principles.

## 1.2 Time value of money foundations

### WRITE THIS IN THE EXAM — Meaning

**Time value of money (TVM)** means a rupee today is worth more than the same nominal rupee later because today’s money can earn a return. **Compounding** moves present money to a future date; **discounting** converts future money to present value.

The five inputs are **present value**, **future value**, **periodic payment**, **number of periods** and **interest/discount rate**. The rate and period must match: annual cash flows use an annual effective rate; half-yearly cash flows use a half-yearly rate.

### EXAM METHOD — Single sum and compounding frequency

1. **Given/data:** identify PV or FV, valuation date, r per period and n periods.
2. **Formula:** `FVₙ = PV₀(1+r)ⁿ` or `PV₀ = FVₙ/(1+r)ⁿ`.
3. **Working/table:** draw T0…Tn and substitute. If nominal annual j is compounded m times, use `r=j/m` and `periods=mn`.
4. **Decision/interpretation:** report value and date; compare options only after using the same date.

### WORKED SOURCE EXAMPLE 1 — Annual versus half-yearly compounding

**Given/data:** ₹1,00,000 for 5 years at nominal 10% p.a.; compare annual and half-yearly compounding.

**Formula:** annual `FV=100,000(1.10)⁵`; half-yearly `FV=100,000(1+0.10/2)¹⁰`.

**Working:** annual FV = ₹1,61,051.00. Half-yearly FV = ₹1,62,889.46.

**Decision:** half-yearly compounding produces ₹1,838.46 more because nominal 10% convertible half-yearly has an effective annual rate of 10.25%.

### WORKED SOURCE EXAMPLE 2 — Present value of a future sum

**Given/data:** receive ₹10,00,000 after 5 years; effective discount rate 6%.

**Formula:** `PV₀ = 1,000,000/(1.06)⁵`.

**Working:** PV factor = 0.747258; PV = ₹7,47,258.17.

**Decision:** ₹7,47,258.17 invested now at 6% grows to ₹10,00,000 in five years.

## 1.3 Uneven cash flows and timing

### EXAM METHOD — Uneven future value

1. **Given/data:** mark each deposit at its exact beginning/end date.
2. **Formula:** end-period `FVₙ=ΣCFₜ(1+r)ⁿ⁻ᵗ`; beginning-period `FVₙ=ΣCFₜ(1+r)ⁿ⁻ᵗ⁺¹`.
3. **Working/table:** write each cash flow and its own exponent.
4. **Decision:** state accumulated value at Tn.

### WORKED SOURCE EXAMPLE 3 — End-of-year deposits

**Given/data:** ₹1,000, ₹2,000, ₹3,000, ₹4,000 and ₹5,000 deposited at ends of Years 1–5; r=8%; value at end of Year 5.

**Working:**
`FV₅ = 1,000(1.08)⁴ + 2,000(1.08)³ + 3,000(1.08)² + 4,000(1.08) + 5,000`
`= 1,360.49 + 2,519.42 + 3,499.20 + 4,320 + 5,000 = ₹16,699.11`.

**Decision:** accumulated fund at T5 is **₹16,699.11**.

### WORKED SOURCE EXAMPLE 4 — Beginning-of-year deposits

**Given/data:** ₹1,000, ₹2,000 and ₹3,000 at beginnings of Years 1–3; r=12%; value at end of Year 3.

**Use this correct form:** beginning of Year 1 is T0, so exponents are 3, 2 and 1—not 2, 1 and 0.

**Working:** `FV₃=1,000(1.12)³+2,000(1.12)²+3,000(1.12)=₹7,273.73`.

**Decision:** T3 value is **₹7,273.73**.

### EXAM METHOD — Uneven present value

1. **Given/data:** list CF₁…CFₙ and k.
2. **Formula:** `PV₀=ΣCFₜ/(1+k)ᵗ`.
3. **Working/table:** discount each amount separately; do not add amounts first.
4. **Decision:** quote today’s equivalent.

### WORKED SOURCE EXAMPLE 5 — Uneven PV

Cash flows in Years 1–4 are ₹20,000, ₹40,000, ₹20,000 and ₹10,000; k=10%.

`PV = 20,000/1.10 + 40,000/1.10² + 20,000/1.10³ + 10,000/1.10⁴`
`= 18,181.82 + 33,057.85 + 15,026.30 + 6,830.13 = ₹73,096.10`.

At 8%, the same stream is worth ₹76,039.01. **Interpretation:** a higher discount rate lowers PV of positive future cash flows.

## 1.4 Ordinary annuities

### WRITE THIS IN THE EXAM — Definition

An **annuity** is an equal cash flow at regular intervals for a fixed number of periods. An **ordinary annuity** occurs at each period-end. The uploaded numerical examples are ordinary annuities unless a beginning date is expressly stated.

### EXAM METHOD — Ordinary annuity

1. **Given/data:** PMT, r, n, end-of-period timing and whether PV or FV is required.
2. **Formula:** PV=`PMT[1−(1+r)⁻ⁿ]/r`; FV=`PMT[(1+r)ⁿ−1]/r`.
3. **Working:** calculate factor without premature rounding.
4. **Decision:** name date of PV/FV.

### WORKED SOURCE EXAMPLE 6 — PV annuity

Receive ₹50,000 at each year-end for 5 years; r=5%.

`PV₀ = 50,000[1−(1.05)⁻⁵]/0.05 = 50,000(4.329477) = ₹2,16,473.83`.

**Decision:** invest **₹2,16,474 now** to fund the promised receipts at 5%.

### WORKED SOURCE EXAMPLE 7 — FV annuity

Deposit ₹50,000 at each year-end for 5 years; r=5%.

`FV₅ = 50,000[(1.05)⁵−1]/0.05 = 50,000(5.525631) = ₹2,76,281.56`.

**Decision:** fund at end of Year 5 is **₹2,76,282**.

### ADDITIONAL SOURCE PRACTICE — Mixed beginning deposits

**Given/data:** deposits at beginnings of Years 1–5 are ₹5,000, ₹10,000, nil, ₹15,000 and ₹25,000; r=8%; find value at end of Year 5.

**Formula:** a beginning-of-year deposit receives interest through that year. Thus exponents for Years 1–5 are 5, 4, 3, 2 and 1.

**Working:** `FV₅=5,000(1.08)⁵+10,000(1.08)⁴+0(1.08)³+15,000(1.08)²+25,000(1.08)` `=₹7,346.64+₹13,604.89+₹17,496+₹27,000=₹65,447.53`.

**Decision:** the fund at end of Year 5 is **₹65,447.53**. The nil Year-3 deposit is a genuine zero cash flow; do not close the timeline gap or change later exponents.

### ADDITIONAL SOURCE PRACTICE — Annuity choice checks

A ₹10,000 year-end deposit for four years at 10% accumulates to `10,000[(1.10)⁴−1]/.10=₹46,410`. A ₹20,000 year-end receipt for six years discounted at 10% is worth `20,000[1−1.10⁻⁶]/.10=₹87,105.21` now. These two answers are a useful direction check: FV exceeds total deposits because interest is added; PV is below total receipts because future amounts are discounted.

### WRITE THIS IN THE EXAM — TVM comparison and explanation

When comparing alternatives, first move every cash flow to the **same valuation date**. A larger future value is preferable for investments with the same present outlay and risk; a smaller present cost is preferable for identical future benefits. State why the result changes: a higher rate increases FV but decreases PV, a longer time magnifies both effects, and more frequent compounding increases FV when the quoted nominal annual rate is held constant.

For an annuity answer, identify three marks explicitly: (1) equal cash flows, (2) fixed regular intervals, and (3) period-end timing. If payment occurs at each period-beginning, first calculate the ordinary-annuity value and move it one extra period by multiplying by `(1+r)`. The uploaded source does not develop a separate annuity-due problem, so use this only when the question clearly states beginning timing.

A timeline also resolves deferred streams. Value the annuity one period before its first cash flow, then discount that lump-sum value back to T0. Do not change the core annuity formula or invent a new exponent pattern. For unequal flows, retain the summation method because an annuity factor applies only to equal payments.

### QUICK REASONABLENESS TESTS

1. FV of positive deposits should exceed their undiscounted total when r>0, except a final deposit receiving no interest does not change.
2. PV of positive future receipts should be below their undiscounted total when r>0.
3. Raising the discount rate lowers PV.
4. A beginning deposit must produce a larger FV than the same end deposit.
5. Half-yearly compounding at a nominal annual quote normally exceeds annual compounding.
6. Always attach “today,” “end of Year n,” or another date to the answer.

**COMMON MISTAKES:** mismatching annual rate and half-year periods; giving the last end-year deposit one year’s interest; using end-period exponents for beginning deposits; discounting all unequal flows by the same exponent; calling end-of-year payments an annuity due; rounding factors early.
**Memory aid:** **Move right: multiply. Move left: divide. Beginning means one extra period.**

\pagebreak

# MODULE 2 — CAPITAL STRUCTURE DECISION

## 2.1 Long-term finance, cost and risk

### WRITE THIS IN THE EXAM — Debt and equity

1. **Debt** gives lenders a fixed contractual return; interest is normally tax-deductible, but payment is unavoidable and increases financial risk. Forms include bonds, debentures, convertible bonds and syndicated loans.
2. **Equity** carries residual, uncertain returns through dividends and price growth; investors therefore usually demand a higher return. It can be raised by rights issue, public issue or private placement.
3. The financing objective is an **optimal capital structure** that maximises shareholder wealth and firm value while minimising overall cost of capital, subject to risk and practical constraints.

### WRITE THIS IN THE EXAM — WACC, CAPM and beta

`K₀=(E/V)Ke+(D/V)Kd(1−τ)` when tax relief is available. Use **market-value weights** unless a question directs otherwise. CAPM gives `Ke=Rf+β(Rm−Rf)`.

**Beta** measures systematic market risk: β>1 means above-market systematic risk; β<1 means lower systematic risk. `β=Cov(Rp,Rm)/Var(Rm)`. A quoted-company beta includes business and financial risk, so a proxy with different gearing needs care.

The source names dividend growth and earnings growth methods but does not develop full examples; do not invent a method-specific numerical convention in an answer unless the question supplies it.

## 2.2 Operating, financial and combined leverage

### WRITE THIS IN THE EXAM

1. **Operating leverage** arises from fixed operating cost and magnifies the effect of sales changes on EBIT.
2. **Financial leverage** arises from fixed finance charges, mainly interest, and magnifies the effect of EBIT changes on EPS.
3. **Combined leverage** links sales changes directly to EPS changes.

`DOL=Contribution/EBIT`; `DFL=EBIT/EBT`; `DCL=DOL×DFL=Contribution/EBT`.

### EXAM METHOD — Leverage

1. **Given/data:** output, price, variable cost, fixed operating cost, debt/interest and tax.
2. **Formula:** prepare the profit ladder, then apply DOL, DFL and DCL.
3. **Working/table:** Sales → Contribution → EBIT → Interest → EBT → Tax → PAT → EPS.
4. **Decision:** interpret “times,” and state that coefficients apply around the given activity level.

### WORKED SOURCE EXAMPLE 1 — Sunrise

At 50,000 units, source workings give contribution ₹30,00,000, fixed operating cost ₹20,00,000, EBIT ₹10,00,000, interest ₹1,00,000 and EBT ₹9,00,000.

`DOL=30/10=3.00`; `DFL=10/9=1.1111`; `DCL=30/9=3.3333`.

With the source tax/share data, EPS rises from ₹0.63 at 50,000 units to ₹1.05 at 60,000 units. Sales/output rises 20%, while EPS rises 66.67%; `66.67%/20%=3.3335`, confirming DCL.

**Decision:** near this level, a 1% sales change causes about a 3.33% EPS change in the same direction; risk is high because fixed operating and financing costs amplify changes.

### WORKED SOURCE EXAMPLE 2 — Blue Horizon correction

Sales ₹1,60,00,000; contribution ₹64,00,000; EBIT ₹34,00,000; interest ₹1,20,000; EBT ₹32,80,000.

`DOL=64/34=1.8824`; `DFL=34/32.8=1.0366`; `DCL=64/32.8=1.9512`.

**Use this correct form:** Contribution/EBT = **DCL**, not DFL.

**COMMON MISTAKES:** using sales/EBIT as DOL; labelling Contribution/EBT as DFL; using debt instead of interest; applying ratios at EBIT or EBT near zero without warning; ignoring preference dividends where present.
**Memory aid:** **C over EBIT, EBIT over EBT, C over EBT.**

## 2.3 EBIT–EPS analysis and indifference

### WRITE THIS IN THE EXAM

**EBIT–EPS analysis** compares financing plans by the EPS produced at a stated EBIT. `EPS=(EBIT−I)(1−τ)/N`. The **indifference EBIT** makes the plans’ EPS equal. With the same tax rate:
`(EBIT−I₁)/N₁=(EBIT−I₂)/N₂`.

Above the indifference point, the plan with fewer shares and more fixed interest normally gives higher EPS; below it, the more-equity plan normally gives higher EPS. EPS comparison does **not** by itself measure market value, distress risk or debt capacity.

### WORKED SOURCE EXAMPLE 3 — Sunshine financing plan

**Given/data:** ₹20,00,000 required. Plan X: all equity, 2,00,000 shares. Plan Y: 1,00,000 shares plus debt. EBIT ₹5,00,000; debt interest 8%; tax 30%.

**Correction:** Plan Y debt is **₹10,00,000**, confirmed by the ₹80,000 interest (`10,00,000×8%`).

| Item | Plan X | Plan Y |
|---|---:|---:|
| EBIT | ₹5,00,000 | ₹5,00,000 |
| Interest | 0 | ₹80,000 |
| EBT | ₹5,00,000 | ₹4,20,000 |
| PAT at 30% | ₹3,50,000 | ₹2,94,000 |
| Shares | 2,00,000 | 1,00,000 |
| EPS | ₹1.75 | ₹2.94 |

**Decision:** select Plan Y on EPS at this EBIT, but separately discuss its greater financial risk.

### WORKED SOURCE EXAMPLE 4 — Indifference point

Plan A: equity 60m and debt 20m at 12%, so interest 2.4m and relative share count 60. Plan B: equity 40m and debt 40m at 12%, so interest 4.8m and relative shares 40; same par value and tax assumed.

`(EBIT−2.4)/60=(EBIT−4.8)/40`; `40EBIT−96=60EBIT−288`; `EBIT=9.6m`.

**Decision:** below 9.6m choose A on EPS; above 9.6m choose B; at 9.6m EPS is equal.

## 2.4 Capital-structure theories

### Comparison answer — WRITE THIS IN THE EXAM

| Theory | Key assumptions | Effect of more debt | Optimum under model |
|---|---|---|---|
| Net Income | Kd and Ke constant; Kd<Ke; no tax | V rises, K₀ falls | maximum debt |
| Traditional | Kd/Ke rise after moderate gearing | V first rises, then falls | max V/min K₀ at moderate debt |
| Net Operating Income | K₀ and Kd constant; Ke adjusts | V and K₀ unchanged | no unique optimum |
| MM without tax | perfect markets, rational investors, equal borrowing access, no tax | Ke rises to offset cheap debt | financing irrelevant |
| MM with tax | corporate interest tax shield | V rises by τD; WACC falls | theoretical near-total debt |

Practical limits to MM-tax’s extreme result include **bankruptcy/distress risk**, **agency and covenant cost**, **tax exhaustion**, limited debt capacity, differing risk tolerance and rising borrowing cost.

### EXAM METHOD — Net Income approach

1. **Given/data:** EBIT, D, Kd and Ke; no tax unless stated.
2. **Formula:** `I=KdD`; `NI=EBIT−I`; `E=NI/Ke`; `V=E+D`; `K₀=EBIT/V`.
3. **Working:** value equity before adding debt.
4. **Decision:** compare V and K₀ across gearing levels.

### WORKED SOURCE EXAMPLE 5 — NI approach

EBIT ₹1,00,000; debt ₹4,00,000; Kd=10%; Ke=12.5%.

Interest=`₹4,00,000×10%=₹40,000`; NI=`₹60,000`; E=`60,000/0.125=₹4,80,000`; V=`4,80,000+4,00,000=₹8,80,000`; K₀=`1,00,000/8,80,000=11.36%`.

**Decision:** under NI assumptions, the firm is worth ₹8,80,000.

### EXAM METHOD — Traditional approach

Repeat the NI table for every proposed debt level using the Kd and Ke stated for that level. Choose the row with **highest V** and **lowest K₀**.

### WORKED SOURCE EXAMPLE 6 — Traditional optimum

EBIT ₹2,00,000, no tax.

| Debt/Kd/Ke | Interest | Equity value (EBIT−I)/Ke | Firm value | K₀ |
|---|---:|---:|---:|---:|
| ₹0; —; 10% | 0 | ₹20,00,000 | ₹20,00,000 | 10.00% |
| ₹4,00,000; 5%; 11% | ₹20,000 | ₹16,36,364 | ₹20,36,364 | 9.82% |
| ₹6,00,000; 6%; 13% | ₹36,000 | ₹12,61,538 | ₹18,61,538 | 10.74% |

**Decision:** ₹4,00,000 debt is optimal among the choices because V is maximum and K₀ minimum.

### EXAM METHOD — NOI approach

1. Compute `V=EBIT/K₀`.
2. Compute `E=V−D`.
3. Compute `NI=EBIT−KdD` and `Ke=NI/E`.
4. Explain that V and K₀ stay fixed while Ke rises with gearing.

### WORKED SOURCE EXAMPLE 7 — NOI approach

EBIT ₹5,00,000; K₀=16%; debt ₹20,00,000 at 14%.

`V=5,00,000/0.16=₹31,25,000`; `E=₹11,25,000`; interest=`₹2,80,000`; NI=`₹2,20,000`; `Ke=2,20,000/11,25,000=19.56%`.

**Decision:** total firm value is ₹31,25,000; leverage raises required equity return rather than total value.

### EXAM METHOD — MM without tax

`VU=EBIT/KeU`; `VL=VU`; `E=VL−D`; `KeL=KeU+(KeU−Kd)(D/E)`.

### WORKED SOURCE EXAMPLE 8 — MM without tax

EBIT ₹24,00,000; KeU=12%; debt ₹1,00,00,000 at 8%.

`VU=24,00,000/0.12=₹2,00,00,000=VL`; `E=₹1,00,00,000`; `KeL=12%+(12%−8%)(1)=16%`.

WACC=`0.5(16%)+0.5(8%)=12%`. **Decision:** leverage changes Ke but not firm value or WACC.

### EXAM METHOD — MM with tax

`VU=EBIT(1−τ)/KeU`; `VL=VU+τD`; `E=VL−D`; use after-tax debt cost in WACC.

### WORKED SOURCE EXAMPLE 9 — Tax shield value

Unlevered after-tax operating income ₹12,500 and KeU=10%, so `VU=₹1,25,000`. Levered firm debt ₹1,00,000; tax 50%.

Tax shield PV=`τD=0.50×1,00,000=₹50,000`; `VL=1,25,000+50,000=₹1,75,000`.

**Use this correct form:** `VL=VU+τD`, never `VU×τD`.

### ADDITIONAL SOURCE PRACTICE — Traditional approach across many debt levels

**Given/data:** EBIT ₹1,00,000, no tax. Candidate debt is ₹0 to ₹7,00,000 with the Kd and Ke stated for each source row. Apply the whole-row interest rate to the whole debt balance.

| Debt ₹ | Firm value V ₹ | K₀=EBIT/V | Reading |
|---:|---:|---:|---|
| 0 | 10,00,000 | 10.0000% | all equity |
| 1,00,000 | 10,14,286 | 9.8592% | value rises |
| 2,00,000 | 10,36,364 | 9.6491% | value rises |
| 3,00,000 | 10,45,690 | 9.5631% | highest value |
| 4,00,000 | 10,45,161 | 9.5679% | almost equal, but slightly lower |
| 5,00,000 | 10,37,037 | 9.6429% | value begins falling |
| 6,00,000 | 10,00,000 | 10.0000% | advantage exhausted |
| 7,00,000 | 9,20,000 | 10.8696% | over-geared |

**Decision:** choose debt ₹3,00,000 because it produces the maximum firm value and minimum K₀. The ₹3 lakh and ₹4 lakh rows are extremely close, so premature rounding can reverse the ranking.

### ADDITIONAL SOURCE PRACTICE — MM-tax rate check

EBIT ₹7,00,000; tax **30%**; KeU=12%; debt ₹4,00,000. `VU=7,00,000(.70)/.12=₹40,83,333.33`; tax shield=`.30×4,00,000=₹1,20,000`; `VL=₹42,03,333.33`.

**Decision:** the debt adds ₹1,20,000 of value under MM-tax assumptions. Use the question’s 30% rate; a stray 40% label in the source solution is inconsistent with both its data and arithmetic.

### WRITE THIS IN THE EXAM — Balanced financing recommendation

A complete recommendation does not stop at a calculated EPS or WACC. Number the answer: (1) return effect—EPS, NPV or value; (2) liquidity and fixed-interest commitment; (3) gearing, distress and covenant risk; (4) tax-shield availability; (5) control dilution under equity; and (6) flexibility/debt capacity. Conclude with the calculation’s model limitations.

**COMMON MISTAKES:** book-value weights in WACC without instruction; subtracting interest before calculating VU under MM-tax; mixing NI and NOI calculation orders; choosing lowest Kd rather than max V in Traditional theory; treating theoretical MM-tax optimum as a practical recommendation; using the source’s stray 40% where a question clearly states/calculates 30%; combining inconsistent data instead of stating it.
**Memory aid:** **NI values equity first; NOI values firm first; MM-tax adds the shield.**

\pagebreak

# MODULE 3 — INVESTMENT APPRAISAL

## 3.1 Relevant cash flow and NPV

### WRITE THIS IN THE EXAM — Relevant cash flow

A **relevant cash flow** is **future**, **incremental** and caused by accepting the project. Use cash flow, not accounting profit.

1. Include acquisition, installation and setup at T0.
2. Include incremental revenues and cash costs during operation.
3. Include opportunity costs and side effects where supplied.
4. Exclude sunk cost already incurred.
5. Include tax effects and tax-allowable depreciation.
6. Invest working capital when required and recover the remaining balance at the end.
7. Include after-tax disposal/scrap proceeds.

`NPV=Σₜ₌₀ⁿ CFₜ/(1+k)ᵗ`. Accept if NPV>0 because it adds value at the required return.

### EXAM METHOD — Basic NPV

1. **Given/data:** T0 investment, year-end CFs, k and life.
2. **Formula:** NPV formula above.
3. **Working/table:** Time | CF | DF | PV; retain full precision.
4. **Decision:** accept/reject and state value added.

### WORKED SOURCE EXAMPLE 1 — Uneven NPV

| Time | CF ($) | PV at 10% ($) |
|---|---:|---:|
| 0 | (100,000) | (100,000.00) |
| 1 | 30,000 | 27,272.73 |
| 2 | 40,000 | 33,057.85 |
| 3 | 50,000 | 37,565.74 |
| **NPV** |  | **(2,103.68)** |

**Decision:** reject; the project destroys about $2,104 of value at 10%.

## 3.2 Inflation: nominal and real methods

### WRITE THIS IN THE EXAM

**General inflation** affects the overall price level; **specific inflation** affects a particular revenue or cost line. Under the **nominal method**, inflate each line at its specific rate and discount at a nominal rate. Under the **real method**, keep flows in constant purchasing power and discount at a real rate.

`1+i=(1+r)(1+h)`; therefore `i=(1+r)(1+h)−1` and `r=(1+i)/(1+h)−1`.

Use the real method only when cash flows move with general inflation consistently. The nominal method is safer with different inflation rates, tax and working capital.

### EXAM METHOD — Inflation-adjusted NPV

1. Identify whether each stated amount is **current/base-year** or already **Year 1**.
2. Current amount: `Xₜ=X₀(1+g)ᵗ`; Year-1 amount: `Xₜ=X₁(1+g)ᵗ⁻¹`.
3. Calculate each nominal revenue/cost separately.
4. Discount nominal net flows at nominal k and decide.

### WORKED SOURCE EXAMPLE 2 — Different inflation rates

Year-1 revenue ₹15,000 grows 4%; Year-1 cost ₹5,000 grows 2%; initial cost ₹60,000.

| Year | Revenue | Cost | Net CF |
|---|---:|---:|---:|
| 0 |  |  | (₹60,000) |
| 1 | ₹15,000 | ₹5,000 | ₹10,000 |
| 2 | ₹15,600 | ₹5,100 | ₹10,500 |
| 3 | ₹16,224 | ₹5,202 | ₹11,022 |
| 4 | ₹16,872.96 | ₹5,306.04 | ₹11,566.92 |

**Interpretation:** never inflate only the final net amount when revenue and cost have different inflation rates.

### WORKED SOURCE EXAMPLE 3 — Fisher consistency

Constant-price annual net flow $30,000 for four years; real rate 10%; general inflation 5%.

Real NPV=`−60,000+30,000×[1−1.10⁻⁴]/0.10 = $35,095.96`.

Nominal rate=`1.10×1.05−1=15.5%`. Nominal flows are $31,500, $33,075, $34,728.75, $36,465.19; discounting at 15.5% gives the same NPV (subject to rounding).

**Decision:** either method is valid only when cash-flow/rate types match.

## 3.3 Working-capital timing in projects

### WRITE THIS IN THE EXAM

Working capital is a **balance**, not an annual expense. At T0 record the opening requirement as an outflow. During the project record only each increase `−ΔWC`. At termination recover the outstanding balance as an inflow.

If WC is required “at the beginning of each year,” Year-1 WC is at T0; the increase for Year 2 is at T1.

### WORKED SOURCE EXAMPLE 4 — Inflation plus WC

Initial fixed investment $150,000. Annual current-price inflow $45,000 inflates 5% for four years. WC equals 10% of each year’s nominal inflow and is needed at the beginning of the year. Real rate 12%; general inflation 5%; nominal rate=`1.12×1.05−1=17.6%`.

| Time | Operating inflow | WC cash flow | Net CF |
|---|---:|---:|---:|
| 0 | — | (4,725.00) | (154,725.00) |
| 1 | 47,250.00 | (236.25) | 47,013.75 |
| 2 | 49,612.50 | (248.06) | 49,364.44 |
| 3 | 52,093.13 | (260.47) | 51,832.66 |
| 4 | 54,697.78 | +5,469.78 recovery | 60,167.56 |

NPV at 17.6% ≈ **−$15,725**. **Decision:** reject. The source’s constant-price WC illustration differs because its WC bases are not exactly equivalent; use the nominal integrated method.

## 3.4 Tax-allowable depreciation and disposal

### WRITE THIS IN THE EXAM

**Tax-allowable depreciation (TAD)** is a non-cash deduction that reduces taxable profit. It is deducted to calculate tax and added back to cash flow. Its cash benefit is the **tax shield** `τ×TAD`.

`Taxable profit = revenue − cash operating cost − TAD`.
`Operating CF after tax = taxable profit(1−τ)+TAD`.

Under WDV, TAD=`opening tax WDV×rate`. At disposal, proceeds below tax WDV create a **balancing allowance**; proceeds above tax WDV create a **balancing charge**, subject to the question’s tax rules. Unless told otherwise in these source examples, tax is paid in the same year. If a one-year tax lag is specified, shift tax one column right.

### EXAM METHOD — Integrated tax NPV

1. **Given/data:** asset basis, depreciation method, tax rate/timing, operating amounts, WC, scrap.
2. **Formula:** calculate TAD and taxable profit before tax cash payment.
3. **Working/table:** separate operating CF, WC movement and terminal items.
4. **Decision:** discount total net CF and apply NPV rule.

### WORKED SOURCE EXAMPLE 5 — WDV and balancing allowance

Asset $100,000; 30% WDV TAD; four-year life; disposal $5,000; tax 30%; operating receipts less cash costs $30,000 each year; same-year tax.

TAD: Year 1 $30,000; Year 2 $21,000; Year 3 $14,700. Tax WDV before disposal after Year 3 is $34,300. Disposal $5,000 creates Year-4 balancing allowance **$29,300**.

| Year | Pre-TAD operating surplus | TAD | Taxable profit | Tax 30% | Total CF incl. disposal |
|---|---:|---:|---:|---:|---:|
| 1 | 30,000 | 30,000 | 0 | 0 | 30,000 |
| 2 | 30,000 | 21,000 | 9,000 | 2,700 | 27,300 |
| 3 | 30,000 | 14,700 | 15,300 | 4,590 | 25,410 |
| 4 | 30,000 | 29,300 | 700 | 210 | 29,790 + 5,000 = 34,790 |

NPV at 10%=`−100,000+30,000/1.1+27,300/1.1²+25,410/1.1³+34,790/1.1⁴=−$7,312.34`.

**Decision:** reject.

### WORKED SOURCE EXAMPLE 6 — Straight-line, WC and terminal value

Amounts ₹000: machine 10,000; scrap 2,000; life 5; initial WC 1,000; annual saving before depreciation 3,000; tax 30%; k=10%.

TAD=`(10,000−2,000)/5=1,600`; taxable profit=`3,000−1,600=1,400`; tax=`420`; annual operating CF=`1,400−420+1,600=2,580`.

Timeline: T0 `(11,000)`; T1–T4 `2,580` each; T5 `2,580+2,000 scrap+1,000 WC recovery=5,580`.

NPV=`₹642.99 thousand`, approximately **₹643 thousand**. **Decision:** accept.

### WORKED SOURCE EXAMPLE 7 — Integrated specific inflation case

Machine ₹4,000,000; four years; 1,000 units/year. Year-1 price ₹12,000 inflates 4%; unit variable cost ₹6,000 inflates 6%; fixed cash cost ₹1,000,000 inflates 4%; straight-line TAD ₹1,000,000; tax 30% same year; WC 10% of revenue at each year-beginning; nominal k=14%.

Operating CFs are ₹3,800,000; ₹3,856,000; ₹3,909,200; ₹3,959,185.60. WC balances are ₹1,200,000; ₹1,248,000; ₹1,297,920; ₹1,349,836.80.

Net timeline: T0 `−₹5,200,000`; T1 `₹3,752,000`; T2 `₹3,806,080`; T3 `₹3,857,283.20`; T4 `₹5,309,022.40` including WC recovery.

NPV at 14% ≈ **₹6,766,807**. **Decision:** accept under the stated same-year tax and no-disposal-adjustment assumptions.

**COMMON MISTAKES:** treating depreciation as cash outflow; forgetting installation in asset basis; taxing cash flow rather than taxable profit; adding back TAD before computing tax; charging the full WC balance each year; putting beginning-year WC at year-end; omitting terminal recovery; mixing real and nominal rates; rounding discount factors before summing.
**Memory aid:** **Inflate line by line; tax profit; add back TAD; move only ΔWC; recover at the end.**

## 3.5 IRR, MIRR, discounted payback and PI

### WRITE THIS IN THE EXAM — IRR

**IRR** is the discount rate at which NPV equals zero. For a conventional independent project, accept if IRR exceeds the required return. Limitations: it assumes reinvestment at IRR, may give multiple/no IRR for non-conventional flows, and may rank mutually exclusive projects differently from NPV. NPV should control where rankings conflict.

### EXAM METHOD — IRR interpolation

1. Find L with positive NPV and H with negative NPV.
2. Use `IRR≈L+[NPV_L/(NPV_L−NPV_H)](H−L)`.
3. State interpolation is approximate.
4. Compare with required return.

### WORKED SOURCE EXAMPLE 8 — IRR

Cash flows: −2,500; 600; 600; 700; 700; 820. Source trial NPVs: +198 at 8%, −78 at 12%.

`IRR≈8%+[198/(198−(−78))]×4%=10.87%` from rounded NPVs. Exact solution is about 10.81%.

**Decision:** accept if required return is 9%.

### WRITE THIS IN THE EXAM — MIRR

**MIRR** separates the investment phase and return phase and uses a realistic finance/reinvestment rate. The source names this concept but gives no full numerical example. Use the exact formula specified by the examiner; conceptually, compound positive flows at the reinvestment rate, discount negative flows at the finance rate, and find the single rate linking them over n periods.

### EXAM METHOD — Discounted payback

Discount each CF at k; cumulate PVs. `DPP=completed years+unrecovered amount/PV in recovery year`.

### WORKED SOURCE EXAMPLE 9 — DPP

Initial $2,500k; discounted inflows at 9% approximately $1,009k, $724k, $541k, $510k and $533k. After Year 3, unrecovered amount is $226k.

`DPP=3+226/510=3.44 years`.

**Decision:** compare 3.44 years with the required cutoff; remember value after payback is ignored.

### WORKED SOURCE EXAMPLE 10 — Profitability index

Using the same project, rounded PV inflows total $3,317k.

`PI=3,317/2,500=1.33`. **Decision:** accept because PI>1.

## 3.6 Capital rationing

### WRITE THIS IN THE EXAM

**Capital rationing** exists when positive-NPV projects exceed available funds. **Hard/external rationing** comes from difficulty raising finance, weak track record or poor credit rating. **Soft/internal rationing** comes from management policy, ratio targets or a deliberate hurdle.

1. **Divisible projects:** rank by PI and use residual funds for a fraction of the next project.
2. **Indivisible projects:** compare feasible combinations and choose maximum total NPV.
3. **Mutually exclusive projects:** choose the feasible single project with highest NPV, not automatically highest PI.

### WORKED SOURCE EXAMPLE 11 — $1m budget

| Project | Investment $000 | NPV $000 | PI |
|---|---:|---:|---:|
| A | 300 | 50 | 1.17 |
| B | 200 | 40 | 1.20 |
| C | 500 | 70 | 1.14 |
| D | 400 | 60 | 1.15 |
| E | 250 | 45 | 1.18 |

**Divisible:** B + E + A use $750k; invest remaining $250k in 62.5% of D. NPV=`40+45+50+0.625(60)=$172.5k`.

**Indivisible:** A+B+C uses $1m and gives **$160k**, the best feasible source combination.

**Mutually exclusive:** choose C because its NPV is highest at $70k.

### ADDITIONAL SOURCE PRACTICE — Multiple specific inflation rates

Amounts $000. Fixed investment 5,000. Current revenue 2,500 inflates 8%; wages 300 inflate 4%; maintenance 500 inflates 5%; WC is 12% of each year’s nominal revenue, required at the beginning. The exact nominal discount rate from a 10% real rate and 4.56% general inflation is about 15.02%.

Nominal revenues for Years 1–5 are 2,700; 2,916; 3,149; 3,401; 3,673. Wages are about 312; 324; 337; 351; 365. Maintenance is 525; 551; 579; 608; 638. WC balances are 324, 349.92, 377.91, 408.14 and 440.76; record only increases of about 25.92, 27.99, 30.23 and 32.62, then recover 440.76 at T5.

The source’s rounded net flows are `−5,324; 1,837; 2,012; 2,203; 2,410; 3,111`. Discounting unrounded flows at 15.02% gives NPV about **$2.164m**; the rounded source table at 15% reports about $2.170m. **Decision:** accept; the difference is presentation rounding, not a decision change.

### ADDITIONAL SOURCE PRACTICE — Unspecified disposal-tax assumption

Plant ₹100,000 plus installation ₹20,000; WC ₹30,000; ten-year life; 5,000 units/year at price ₹20 and variable cost ₹12; fixed cash cost ₹5,000; tax 50%; straight-line depreciation ignores salvage.

Sales=`₹100,000`; variable cost=`₹60,000`; pre-depreciation surplus=`₹35,000`; TAD=`₹120,000/10=₹12,000`; taxable profit=`₹23,000`; tax=`₹11,500`; annual operating CF=`₹23,500`. Initial outlay is `₹120,000+₹30,000=₹150,000`.

If ₹5,000 scrap is not taxed, Year-10 total CF is `₹23,500+₹5,000+₹30,000=₹58,500`. If the fully depreciated asset’s scrap is taxable, after-tax scrap is ₹2,500 and Year-10 CF is ₹56,000. **Exam treatment:** expose the assumption because the practice question does not state disposal-tax policy.

### WRITE THIS IN THE EXAM — NPV versus the other methods

NPV directly measures value added, uses all project cash flows and applies the required return. IRR is intuitive but can mis-rank scale/timing differences. Discounted payback highlights liquidity and exposure but ignores post-cutoff value. PI is useful for divisible single-period rationing but can mis-rank indivisible or mutually exclusive choices. Therefore, where methods conflict, use NPV unless the question imposes a funding rule.

**COMMON MISTAKES:** ranking indivisible projects by PI without testing combinations; selecting highest IRR rather than NPV for mutually exclusive projects; calling ordinary payback discounted payback; presenting interpolated IRR as exact; using PI `(NPV/investment)` instead of `(NPV+investment)/investment`.
**Memory aid:** **Independent: accept positive NPV. Divisible constraint: PI. Indivisible: combinations. Exclusive: highest NPV.**

\pagebreak

# MODULE 4 — RISK ANALYSIS

## 4.1 Risk, uncertainty and methods

### WRITE THIS IN THE EXAM

**Risk** is quantifiable variability because probabilities can be assigned. **Uncertainty** exists when reliable probabilities cannot be assigned.

Methods named in the materials are: probability/expected value, standard deviation, certainty equivalent, risk-adjusted discount rate, sensitivity analysis and decision-tree analysis. Decision trees are named only; no source method/example is developed.

## 4.2 Expected value, standard deviation and CV

### WRITE THIS IN THE EXAM

`E(X)=Σxp`; `σ²=Σx²p−[E(X)]²`; `σ=√σ²`; `CV=σ/E(X)`.

Expected value is the probability-weighted mean. SD measures **absolute dispersion**. CV measures **risk per unit of expected return**, so it is more useful when expected values differ. Lower SD/CV means lower risk, but the final choice also depends on expected return and the decision-maker’s risk attitude.

### EXAM METHOD — Probability distribution

1. **Given/data:** outcomes x and probabilities p; confirm Σp=1.
2. **Formula:** calculate xp and x²p.
3. **Working/table:** sum columns; then variance, SD and CV.
4. **Decision:** compare return and risk separately.

### WORKED SOURCE EXAMPLE 1 — Two proposals

| Proposal | E(X) | Σx²p | SD | CV |
|---|---:|---:|---:|---:|
| A: 2,000(.3), 4,000(.4), 6,000(.3) | 4,000 | 18,400,000 | 1,549.19 | 38.73% |
| B: 1,000(.1), 3,000(.1), 5,000(.4), 7,000(.3), 9,000(.1) | 5,400 | 33,800,000 | 2,154.07 | 39.89% |

For A: `σ=√(18,400,000−4,000²)=1,549.19`. For B: `σ=√(33,800,000−5,400²)=2,154.07`.

**Decision:** A has lower absolute and relative risk; B has higher expected value. Without a stated risk-return preference, there is no unconditional winner.

### WORKED SOURCE EXAMPLE 2 — Expected project NPV

Initial ₹1,40,000; k=10%. Year-1 expected CF=`100,000(.3)+80,000(.5)+10,000(.2)=₹72,000`. Year-2 expected CF=`40,000(.5)+70,000(.3)+60,000(.2)=₹53,000`.

`E(NPV)=−140,000+72,000/1.10+53,000/1.10²=−₹30,743.80` (source rounded-table result −₹30,774).

**Decision:** reject on expected NPV. Joint scenario/failure probabilities require a joint distribution; do not multiply annual probabilities unless independence is stated.

## 4.3 Certainty-equivalent approach

### WRITE THIS IN THE EXAM

A **certainty equivalent (CE)** converts a risky expected cash flow into a riskless-equivalent amount. For an inflow, `CE(CFₜ)=αₜE(CFₜ)` with lower α indicating more risk; discount adjusted flows at **Rf**. Risky outflows may require a larger equivalent amount.

### EXAM METHOD — CE-NPV

1. Multiply each expected cash inflow by its year-specific α.
2. Discount CE cash flows at the risk-free rate.
3. Subtract the initial outlay (adjust it only if specifically risky).
4. Accept if CE-NPV>0.

### WORKED SOURCE EXAMPLE 3 — Golden Era

Initial $15,000; expected inflows $10,000, $8,000, $6,000; CE factors .70, .65, .60; Rf=6%.

CE flows=`$7,000, $5,200, $3,600`. PVs using source rounded factors .943, .890, .840 are `$6,601, $4,628, $3,024`.

CE-NPV=`−15,000+6,601+4,628+3,024=−$747` (full precision about −$746).

Conventional NPV at 12% was about +$4,578, but risk adjustment reverses the decision. **Decision:** reject under CE.

### WORKED SOURCE EXAMPLE 4 — Mutually exclusive machines

Risk-free rate 5% (used by the source solution although omitted from the question). Machine X CE-adjusted flows T0–T4: −30,000; 14,250; 12,750; 7,000; 6,500. CE-NPV ≈ $6,528. Machine Y: −40,000; 22,500; 16,000; 10,500; 6,000. CE-NPV ≈ $9,942.

**Decision:** both acceptable; choose Y because projects are mutually exclusive and Y has the larger CE-NPV.

## 4.4 Risk-adjusted discount rate

### WRITE THIS IN THE EXAM

The **RADR** incorporates project systematic risk in the discount rate. Under the source CAPM approach, `RADR=Rf+β(Rm−Rf)`. Higher β gives higher RADR and lower PV of positive future cash flows.

### WORKED SOURCE EXAMPLE 5 — CAPM and NPV

Initial $150,000; inflows $60,000, $70,000, $80,000; β=.9; Rf=3%; Rm=9%.

`RADR=3%+.9(9%−3%)=8.4%`.

`NPV=−150,000+60,000/1.084+70,000/1.084²+80,000/1.084³=$27,728.33` (source rounded result $27,750).

**Decision:** accept. Assumption: supplied beta is an appropriate project beta and CAPM is applicable.

## 4.5 Sensitivity analysis

### WRITE THIS IN THE EXAM

**Sensitivity analysis** measures how far one input can move adversely before NPV becomes zero, with other inputs unchanged. `Sensitivity margin=base NPV/PV of affected variable×100`. A **lower margin** means greater sensitivity.

Directional interpretation:
1. Initial cost or operating cost: allowable **increase**.
2. Revenue, price, volume or inflow: allowable **decrease**.
3. Life: allowable reduction from base life to discounted break-even life.
4. Discount rate: IRR is the break-even rate; clearly distinguish percentage points from relative percentage change.

### EXAM METHOD — Sensitivity

1. Compute base NPV accurately.
2. Identify PV contribution of one variable.
3. Divide NPV by that PV and state adverse direction.
4. Rank absolute margins only when measured on comparable bases.

### WORKED SOURCE EXAMPLE 6 — Four-year annuity project

Initial cost ₹1,00,000; annual inflow ₹40,000 for four years; k=10%. Source rounded PV inflows total ₹1,26,760; NPV ₹26,760.

- Initial-cost margin=`26,760/100,000=26.76%` increase.
- Inflow margin=`26,760/126,760=21.11%` decrease.
- Cumulative PV after Year 3 leaves ₹560 unrecovered; break-even life=`3+560/27,320=3.02 years`. Allowable reduction=`(4−3.02)/4=24.49%`.
- IRR=21.86%; discount-rate headroom=`21.86%−10%=11.86 percentage points`, equivalent to a 118.6% relative increase.

**Use this correct form:** write “life may decrease by **24.49%**,” or signed change −24.49%; do not present a bare negative sensitivity as if it were a smaller margin.

**Decision:** among comparable cost/inflow/life margins, inflow is most sensitive because 21.11% is lowest.

### ADDITIONAL SOURCE PRACTICE — Probability-of-failure extension

For the two-year expected-NPV example, the source provides separate annual distributions but no joint distribution. If annual outcomes are expressly assumed independent, combine every Year-1 outcome with every Year-2 outcome, calculate each scenario NPV and multiply probabilities. Under that added assumption, the worst combination is ₹10,000 in Year 1 and ₹40,000 in Year 2: `NPV=−140,000+10,000/1.10+40,000/1.10²=−₹97,851.24`; probability=`.2×.5=10%`. The derived probability of negative NPV is 85%, positive NPV 15%, and SD of NPV about ₹31,302.

These are **derived conditional results**, not printed source answers. Without independence or joint probabilities, only expected annual cash flows and expected NPV are uniquely available.

### WRITE THIS IN THE EXAM — Strengths and limits of sensitivity analysis

1. It is simple and identifies the variables requiring control.
2. It gives a break-even margin that managers can compare with forecast error.
3. It changes one variable at a time, so it ignores simultaneous/correlated movements.
4. It gives no probability of the tested movement.
5. Results depend on a sound base case and linearity assumption.
6. Scenario or probability analysis is needed when variables move together.

### EXAM INTERPRETATION — Choosing the risk tool

Use probability analysis when objective probabilities exist; CE when the question gives risk-adjustment coefficients; RADR when systematic risk/beta is supplied; sensitivity when asked “how much can this variable change?”; and a decision tree only when sequential decisions/conditional branches are supplied. Do not force a named technique where its required data are absent.

**COMMON MISTAKES:** probabilities not summing to one; comparing SD alone where means differ; choosing low CV while ignoring return; assuming independence without saying so; discounting CE flows at ordinary WACC; using both CE and RADR and double-counting risk; treating sensitivity as probability; confusing discount rate with a period discount factor.
**Memory aid:** **EV gives centre; SD gives spread; CV scales spread; CE changes cash flow; RADR changes rate; sensitivity finds break-even movement.**

\pagebreak

# MODULE 5 — WORKING CAPITAL DECISIONS

## 5.1 Meaning, types and financing

### WRITE THIS IN THE EXAM — Working capital

`Working capital = current assets − current liabilities`. Current assets include cash, receivables, inventory and marketable securities. Current liabilities include payables, short-term debt, accruals and interest payable.

Adequate WC supports **liquidity**, smooth operations and timely payment; excess WC may reduce profitability, while inadequate WC can disrupt production and damage credit.

**Working-capital management** controls individual current assets/liabilities. **Working-capital financing** chooses the funding source.

1. **Permanent WC:** continuing minimum need, normally financed by long-term sources.
2. **Temporary WC:** seasonal/fluctuating extra need, which may be financed short term.

This is the **maturity-matching principle**. The source does not separately teach named aggressive/conservative policies.

### WRITE THIS IN THE EXAM — Sources

Short-term sources: **trade credit**, cash credit, overdraft, bill/invoice discounting, commercial paper, line of credit, bank guarantee, customer advances and securitisation. Long-term sources: equity and long-term debt.

- **Cash credit:** bank limit secured commonly by hypothecated stocks/receivables; interest on amount drawn.
- **Overdraft:** permission to overdraw an account up to a limit; interest on utilisation.
- **Discounting:** sell/discount a bill or invoice before maturity for cash less a charge.
- **Pledge of receivables:** receivables secure borrowing; lender applies an **advance rate**.
- **Floating charge on inventory:** inventory can be used/sold normally until default.
- **Fixed charge:** specified inventory cannot be disposed of without permission.

Factors affecting WC are nature of business, market conditions, production-cycle length, price levels, business cycle, inventory policy, supplier credit and customer credit policy.

### EXAM METHOD — Cost of rejecting cash discount

1. **Given/data:** discount d%, discount day, final due day, and 365/360 convention.
2. **Formula:** `[d/(100−d)]×[365/(final day−discount day)]`.
3. **Working:** annualise the periodic opportunity cost.
4. **Decision:** compare with alternative annual borrowing cost.

### WORKED SOURCE EXAMPLE 1 — Terms 2/10, net 60

`Cost=(2/98)×(365/50)=14.90% p.a.` using 365 days.

**Decision:** if short-term borrowing costs less than 14.90%, borrow and take the discount, ignoring qualitative constraints.

### WRITE THIS IN THE EXAM — Trade-credit interpretation

The 14.90% is an **opportunity cost**, not an invoice interest charge. By paying on Day 60 instead of Day 10, the buyer keeps 98 for 50 extra days but gives up a discount of 2. Compare the annualised cost with the firm’s alternative short-term finance rate on the same day-count and tax basis. Also consider whether early payment would strain minimum cash, whether the supplier reliably grants the discount, and whether late behaviour could damage credit reputation.

If the firm already lacks cash, “take the discount” is not automatic: borrowing capacity, security and transaction charges matter. Conversely, a zero-stated-interest trade period can still be expensive when a cash discount is sacrificed. Show the formula and decision rather than merely describing trade credit as free.

## 5.2 Aggregate operating cycle

### WRITE THIS IN THE EXAM

The **operating cycle** is the time from buying materials, through production and sale, to cash collection. Supplier credit reduces the firm-funded period.

`ICP=average inventory/COGS×365`; `RCP=average receivables/net credit sales×365`; `PDP=average payables/credit purchases×365`; `net cycle=ICP+RCP−PDP`; `WCR=net cycle×annual operating expenses/365`.

Use credit purchases for payable days when available. COGS is only a stated proxy if purchases are unavailable.

### WORKED SOURCE EXAMPLE 2 — Aggregate method

Average inventory $200,000; COGS $1,000,000; average receivables $150,000; credit sales $900,000; average payables $100,000; annual operating expense $800,000. Purchases unavailable, so COGS is used as payable denominator.

`ICP=73 days`; `RCP=60.8333 days`; `PDP=36.5 days`; net cycle=`97.3333 days`.

`WCR=97.3333×800,000/365=$213,333.33`.

**Decision:** about $213,333 of operating funding is required under the stated averages.

## 5.3 Detailed cash-conversion cycle

### EXAM METHOD — CCC and WCR

1. **Given/data:** compute average balances `(opening+closing)/2`.
2. Reconstruct annual flows where needed:
   - RM consumed=`purchases+opening RM−closing RM`.
   - cost of production=`RM consumed+conversion cost+opening WIP−closing WIP`.
   - COGS=`production cost+opening FG−closing FG`.
3. **Formula:** `CCC=R+W+F+D−C` using matched daily flow denominators.
4. **Working/table:** retain precise daily rates; assume 365 days unless told otherwise.
5. **Decision:** `WCR=CCC×operating cost/365`, then add explicit contingency cash.

### WORKED SOURCE EXAMPLE 3 — NovaTech

Average balances: RM 55,000; WIP 43,150; FG 65,190.50; receivables 123,561.50; payables 60,289.50.

Annual RM consumed=`400,000+45,000−65,000=380,000`; production=750,000; COGS=915,000; credit sales=1,100,000; credit purchases=400,000.

| Component | Calculation | Days |
|---|---|---:|
| R | 55,000/(380,000/365) | 52.82895 |
| W | 43,150/(750,000/365) | 20.99967 |
| F | 65,190.5/(915,000/365) | 26.00156 |
| D | 123,561.5/(1,100,000/365) | 40.99995 |
| C | 60,289.5/(400,000/365) | 55.01088 |
| **CCC** | R+W+F+D−C | **85.81935** |

Operating cost 950,000: `WCR=85.81935×950,000/365=223,365.43`; cycles/year=`365/85.81935=4.25`.

**Use this correct form:** daily RM consumption is `380,000/365=1,041.10`, not 1,040.10.

### WORKED SOURCE EXAMPLE 4 — Reconstructed-flow case (₹ lakh)

RM consumed=`810+230−250=790`; production cost=`790+600+50−52=1,388`; COGS=`1,388+260−300=1,348`; operating cost=`1,348+240=1,588`.

Averages: RM 240, WIP 51, FG 280, debtors 415, creditors 275. Assume all ₹2,000 lakh sales are credit sales.

Precise days: `R=110.8861`; `W=13.4114`; `F=75.8160`; `D=75.7375`; `C=123.9198`. CCC=`151.9312 days`.

WCR including ₹4.75 lakh contingency=`151.9312×1,588/365+4.75=₹665.75 lakh`.

**Use this correct form:** the source’s printed component line was copied from another example. Its ₹667.23 lakh result also reflects early rounding; full-precision working gives **₹665.75 lakh**.

## 5.4 Sales–working-capital regression

### WRITE THIS IN THE EXAM

Regression estimates WC from historical sales: `y=a+bx`. `b=Σ(x−x̄)(y−ȳ)/Σ(x−x̄)²`; `a=ȳ−bx̄`. Correlation `r` measures linear direction/strength from −1 to +1.

The intercept is estimated WC when **sales x=0**, not when slope is zero. Correlation does not prove causation, and extrapolation far outside the data should be qualified.

### EXAM METHOD — Regression forecast

1. Define x=sales and y=WC with units.
2. Calculate means/deviations or raw totals.
3. Calculate b, then a, and write equation with units.
4. Substitute forecast sales in the same scale; report r if asked.

### WORKED SOURCE EXAMPLE 5 — Dollar millions

For five observations, Σx=75, Σy=17.5, Σx²=1,205, Σxy=276.5; x̄=15, ȳ=3.5.

`b=[5(276.5)−75(17.5)]/[5(1,205)−75²]=0.175`; `a=3.5−0.175(15)=0.875`.

`WC ($m)=0.875+0.175 Sales ($m)`.
At sales $22m, `WC=0.875+0.175(22)=$4.725m`; `r≈0.98995`.

**Decision:** forecast WC is $4.725m; relationship is strongly positive, subject to regression assumptions.

### WORKED SOURCE EXAMPLE 6 — Rupee lakhs and unit correction

x̄=600, ȳ=147, Σdx²=25,000, Σdy²=1,830, Σdxdy=6,750.

`b=6,750/25,000=0.27`; `a=147−0.27(600)=−15 lakh`; `r=6,750/√(25,000×1,830)=0.99795`.

`WC (₹ lakh)=−15+0.27 Sales (₹ lakh)`.
At sales ₹800 lakh, WC=`−15+216=₹201 lakh` = ₹20.1 million = ₹2.01 crore.

**Use this correct form:** ₹201 **lakh**, not “201 million.”

## 5.5 Working-capital leverage

### WRITE THIS IN THE EXAM

**Working-capital leverage** measures EBIT sensitivity to WC: `WCL=% change in EBIT/% change in working capital`. A larger coefficient means a small WC change has a larger profitability effect. The source provides the concept but no full numerical example; do not manufacture an unsupported question pattern.

### ADDITIONAL SOURCE PRACTICE — Direct daily-rate CCC

Balances and matched daily flows (same currency scale): raw material 150/10, WIP 250/20, finished goods 170/17, debtors 250/20 and creditors 160/8.

`R=15 days`; `W=12.5`; `F=10`; `D=12.5`; `C=20`. Therefore `CCC=15+12.5+10+12.5−20=30 days`.

If annual operating expense is $1,200,000, `WCR=30×1,200,000/365=$98,630.14`.

**Decision:** about $98,630 must fund the 30-day net cycle. Every ratio works only because its numerator and denominator use the same unit scale.

### WRITE THIS IN THE EXAM — Financing trade-off

Short-term finance can be flexible and interest is often charged only on use, but it creates refinancing and rate risk. Long-term finance is more stable but may cost more and remain outstanding when temporary needs disappear. Apply maturity matching: finance permanent WC with stable long-term funds and seasonal WC with suitable short-term funds. Then discuss liquidity, security, covenants, cost, availability and supplier/bank relationships.

### WRITE THIS IN THE EXAM — Operating-cycle improvement

1. Reduce raw-material days without risking stock-outs.
2. Shorten production/WIP time through process efficiency.
3. Improve finished-goods turnover and demand forecasting.
4. Tighten credit assessment and collection to reduce debtor days.
5. Use agreed supplier credit effectively without damaging reputation or losing valuable discounts.
6. Forecast minimum cash separately; do not fund avoidable idle current assets.

The objective is not simply the shortest possible cycle: over-aggressive cuts may stop production, lose sales or damage supplier/customer relationships.

**COMMON MISTAKES:** using closing rather than average balances; matching payables with sales; adding creditor days; mixing 360 and 365 days; multiplying gross cycle rather than net cycle by operating cost; rounding daily amounts before periods; losing lakh/million units; interpreting a negative regression intercept literally; calling permanent WC short-term financed as the normal rule.
**Memory aid:** **Stock ÷ matched daily flow gives days; add operating stages and debtors, subtract creditors.**

\pagebreak

# MODULE 6 — MERGERS AND ACQUISITIONS

## 6.1 Definitions, forms and rationale

### WRITE THIS IN THE EXAM — Meaning and integration

A **merger** combines companies, often of similar size, into one entity. An **acquisition** occurs when one company obtains control and absorbs another. A deal is **friendly** when the target board supports it and **hostile** when control is pursued without that support.

1. **Horizontal integration:** firms at a similar industry/market level.
2. **Vertical integration:** firms at different production or distribution stages.
3. **Conglomerate integration:** firms in unrelated industries, mainly for diversification.

### WRITE THIS IN THE EXAM — Reasons and synergy

Reasons include **synergy**, increased market share/power, faster access to capabilities and growth, diversification, and use of target tax losses where law permits.

`Synergy value = VAB−(VA+VB)`. Positive synergy exists when combined value exceeds standalone values.

- **Revenue synergy:** market power, cross-selling or complementary resources.
- **Cost synergy:** economies of scale and elimination of duplicate cost.
- **Financial synergy:** financing capacity, diversification effects or tax shields/losses.

## 6.2 Process and consideration

### WRITE THIS IN THE EXAM — Transaction process

1. **Preliminary assessment:** identify target, prepare information memorandum and sign NDA.
2. **Negotiation/letter of intent:** agree broad terms and identify competition, employment, licensing and tax issues.
3. **Due diligence:** investigate financial, legal, tax, commercial and operational risks; support pricing and bargaining.
4. **Final agreement and closing:** execute share-purchase or asset-purchase agreement and obtain required approvals.
5. **Post-merger integration:** combine people, systems and operations so expected synergy is actually realised.

Approval procedures are jurisdiction/date specific; use the legal route stated in the question rather than memorising an outdated court label.

### WRITE THIS IN THE EXAM — Form of consideration

1. **Cash:** certain and liquid for target holders; can be fast, but may use debt/new equity and worsen gearing.
2. **Share exchange:** preserves cash and lets target holders participate, but dilutes ownership/EPS and exposes both groups to price risk.
3. **Mixed offer:** balances cash certainty and continuing participation while reducing immediate cash need.

## 6.3 Bid strategy, defences and related structures

### WRITE THIS IN THE EXAM — Pre-bid defences

1. **Poison pill:** discounted rights dilute a hostile acquirer.
2. **Staggered board:** directors retire in classes, delaying board control.
3. **Golden parachute:** costly benefits payable to executives after control change.
4. **Shark repellent/supermajority:** charter rules require enhanced approval.
5. **Dual-class shares:** insiders retain superior voting rights.
6. **Fair-price amendment:** protects holders against unequal/two-tier terms.

### WRITE THIS IN THE EXAM — Post-bid defences

1. **White knight:** invite a friendlier bidder.
2. **Pac-Man:** target counterbids for the acquirer.
3. **Greenmail:** repurchase hostile holder’s block at a premium.
4. **Crown-jewel sale:** dispose of attractive assets.
5. **Leveraged recapitalisation:** add debt to fund repurchase/dividend and alter control economics.
6. **Litigation:** challenge the bid and delay or improve terms.

Each defence has cost: it may protect bargaining power but can destroy value, increase leverage or entrench management.

### WRITE THIS IN THE EXAM — LBO, MBO, JV and restructuring

An **LBO** uses substantial debt, often secured on target assets, reducing initial equity but creating high financial risk. An **MBO** is an acquisition led by the target’s management. A **joint venture** pools resources and risk for a project; it may be a separate equity entity or contractual arrangement. **Portfolio restructuring** realigns holdings to improve returns, diversify risk, release capital or fit strategy.

## 6.4 Financial analysis and valuation

### WRITE THIS IN THE EXAM

Review historical revenue, cost and sustainable earnings; liquidity and profitability; leverage and interest capacity; then valuation.

The source groups valuation as:
1. **Asset valuation:** agreed asset value less liabilities.
2. **Relative valuation:** market price per unit of earnings or another attribute.
3. **Cash-flow valuation:** present value of future dividends or free cash flows.

Ratios named in the source include current ratio, quick ratio, gross/operating margin, ROA, debt/equity and interest cover; no complete ratio numerical is supplied.

## 6.5 Share-exchange numericals

### EXAM METHOD — Exchange ratio and EPS

1. **Given/data:** define `q=acquirer shares per target share`; standardise rupees/lakhs and per-share figures.
2. **Formula:** `q=Mtarget/Macquirer`; new shares=`q×target shares`; combined EPS=`combined earnings/total shares`.
3. **Working/table:** derive earnings from shares×EPS; keep q exact.
4. **Decision:** discuss both parties, dilution/accretion and whether the ratio preserves value.

### WORKED SOURCE EXAMPLE 1 — A acquires B by NAV/EPS/market price

₹10 face-value equity capital: A ₹2,00,000 → 20,000 shares; B ₹1,00,000 → 10,000 shares. Preference capital A ₹40,000; debentures A ₹30,000/B ₹10,000; assets A ₹3,46,000/B ₹1,22,000; PAT after preference dividend A ₹48,000/B ₹30,000; market prices ₹24/₹27.

**NAV basis:** A equity NAV=`346,000−30,000−40,000=₹276,000`, or ₹13.80/share. B NAV=`122,000−10,000=₹112,000`, or ₹11.20/share. `q=11.20/13.80=0.811594`; exact mechanical new shares 8,115.94, so actual terms need rounding/fraction settlement.

**EPS basis:** A EPS=`48,000/20,000=₹2.40`; B=`30,000/10,000=₹3`; `q=3/2.4=1.25`; issue 12,500 shares.

**Market-price basis:** `q=27/24=1.125`; issue 11,250 shares.

**Decision:** A prefers NAV on least-dilution grounds, but target B may reject because `0.811594×₹24≈₹19.48`, below B’s ₹27 market price. “Fewest shares” is not proof of fair value.

**Use this correct form:** share count is equity share capital divided by **face value**, not market price.

### WORKED SOURCE EXAMPLE 2 — Relative EPS and conversion basis

X: 4,00,000 shares, EPS ₹6, price ₹30. Y: 1,00,000 shares, EPS ₹4.50, price ₹20. Earnings X=`₹24,00,000`; Y=`₹4,50,000`; combined=`₹28,50,000`.

**Relative-EPS ratio:** `q=4.5/6=0.75`. Issue 75,000 shares; total 4,75,000; post EPS=`28,50,000/4,75,000=₹6`. X has no EPS dilution; each old Y share receives .75 share and retains `.75×₹6=₹4.50` earnings entitlement.

**Alternative offer 4 X for 5 Y:** `q=.80`. Issue 80,000; total 4,80,000; post EPS=`₹5.9375`. X dilution=`(6−5.9375)/6=1.0417%`.

**Use this correct form:** Y pre-deal EPS on one X-share basis=`₹4.50/.80=₹5.625`—**division**, not multiplication. It rises to ₹5.9375, a 5.5556% accretion. Equivalent old-Y-share view: `.80×₹5.9375=₹4.75` versus ₹4.50, also +5.5556%.

## 6.6 Offer premium, P/E and market capitalisation

### EXAM METHOD — Share offer valuation

1. Offer value per target share=`q×acquirer pre-deal price`.
2. Premium=`offer value−target price`; premium%=premium/target price.
3. Combined EPS=`combined earnings/exact total shares`.
4. If a combined P/E is imposed, price=`P/E×exact EPS`; check cap=`price×shares=P/E×earnings`.

### WORKED SOURCE EXAMPLE 3 — Sunny Lamps/Moon Lamps

Amounts in lakhs except per-share figures. Sunny: PAT 16, shares 3.2 lakh, EPS ₹5, price ₹30, P/E 6. Moon: PAT 4, shares 1 lakh, EPS ₹4, price ₹20, P/E 5. Exchange `q=.7`; ignore operating synergy/economies of scale.

Offer value=`.7×₹30=₹21`; headline premium=`₹1/₹20=5%`. New shares=.7 lakh; total=3.9 lakh. Combined PAT=₹20 lakh.

Exact combined EPS=`20/3.9=₹5.128205128`. Earnings-weighted P/E=`6(16/20)+5(4/20)=5.8`. Exact post price=`5.8×5.128205128=₹29.743589744`.

Post market cap=`₹29.743589744×3.9 lakh shares=₹116 lakh` exactly. Direct check=`5.8×₹20 lakh=₹116 lakh`, equal to standalone caps ₹96 lakh + ₹20 lakh.

**Use this correct form:** do not round EPS to ₹5.13 before price. That creates a false ₹4,060 market-cap gain even though the no-synergy weighted-P/E assumption preserves ₹116 lakh.

### WRITE THIS IN THE EXAM — Interpretation cautions

EPS accretion is not automatically value creation. NAV may omit revaluation, goodwill and contingent liabilities. A weighted P/E is an assumption, not a market law. State transaction costs, tax, synergy and financing effects only when supported. Explain how fractional shares are settled.

### ADDITIONAL SOURCE PRACTICE — Exact dilution and accretion checks

For X/Y at q=.80, old X EPS falls from ₹6 to ₹5.9375: absolute dilution ₹0.0625 and percentage dilution `0.0625/6=1.0417%`. Each old Y share receives .80 X share, so post-deal earnings entitlement is `.80×₹5.9375=₹4.75`, versus pre-deal ₹4.50: accretion ₹0.25 or 5.5556%.

The same Y result on an X-share basis is pre-deal `₹4.50/.80=₹5.625`, compared with ₹5.9375 post-deal. The two presentations reconcile because one is per old target share and the other per acquirer-equivalent share.

### WRITE THIS IN THE EXAM — Evaluating an exchange offer

1. State q and calculate the headline value/premium at pre-bid prices.
2. Check EPS effect for old acquirer and target holders.
3. Check control dilution and number of new shares.
4. Recalculate value only under a stated post-deal multiple or synergy assumption.
5. Discuss transaction cost, integration risk and financing effects.
6. Conclude separately for acquirer and target; a ratio attractive to one side may be unacceptable to the other.

### WRITE THIS IN THE EXAM — Defence evaluation paragraph

A takeover defence may improve bargaining power and protect target shareholders from an inadequate bid, but it may also entrench management or destroy value. Evaluate legality, cost, time gained, effect on debt/liquidity, treatment of all shareholders and whether a superior offer is likely. Merely naming poison pill, white knight or crown-jewel sale earns less than explaining its mechanism and shareholder effect.

### FINAL M&A VALUE CHECK

Under Sunny/Moon’s no-synergy weighted-P/E assumption, aggregate pre-deal market capitalisation is `3.2 lakh×₹30 + 1 lakh×₹20 = ₹116 lakh`. Therefore any correctly calculated post price and share count must multiply to ₹116 lakh. If the answer shows a small gain, first test for early rounding before claiming synergy.

**COMMON MISTAKES:** reversing q; multiplying target EPS by q when converting to acquirer-share basis; dividing post EPS when converting back to old target entitlement; mixing lakh share counts with rupee PAT; rounding q/EPS early; calling a premium synergy; assuming aggregate market value rises without a stated value source; giving takeover defences without their cost.
**Memory aid:** **Target over acquirer gives q; issue q×target shares; compare target EPS by dividing by q; round last.**

# SOURCE-CORRECTION LEDGER — USE THESE FORMS

This ledger consolidates source slips already explained beside the relevant method. In an exam, write the corrected calculation naturally; there is no need to criticise the class material.

| Module/source issue | Use this correct form | Why it matters |
|---|---|---|
| M1 beginning-period FV | exponents run n, n−1, …, 1 | first deposit is at T0 and earns n periods |
| M1 PV notation | `PV=FV/(1+r)ⁿ` with one symbol for future amount | prevents symbol mismatch |
| M2 leverage label | `Contribution/EBT=DCL` | DFL is `EBIT/EBT` |
| M2 Sunshine Plan Y | debt ₹10,00,000; interest ₹80,000 at 8% | ₹1,00,000 printed debt cannot create that interest |
| M2 MM-tax value | `VL=VU+τD` | tax shield is added, not multiplied by VU |
| M2 tax-rate example | use stated/calculated 30%, not stray 40% label | keeps VU and shield consistent |
| M2 inconsistent MM datum | intended KeL from KeU/Kd/D:E; qualify conflicting WACC | do not combine contradictory inputs silently |
| M3 Year-1/base-year inflation | Year-1 quote uses exponent t−1; base-year uses t | avoids one extra year of inflation |
| M3 TAD | non-cash: deduct for tax, then add back | only tax shield affects operating cash |
| M3 working capital | opening balance at T0; only ΔWC later; full recovery at end | avoids charging the whole balance repeatedly |
| M3 tax lag | source examples use same-year tax; shift only if question states lag | timing changes NPV |
| M3 rounded examples | retain full precision and round final NPV | rounded PV rows may not add exactly to printed answer |
| M4 proposal labels | tables are Proposal A and B, not “Year 1/Year 2” | comparison is between alternatives |
| M4 missing machine rate | CE machine solution assumes Rf=5% | CE flows must be discounted at an identified rate |
| M4 life sensitivity | “24.49% allowable reduction,” or signed −24.49% | compare positive adverse-change margins |
| M5 raw-material daily rate | `380,000/365=1,041.10` | 1,040.10 is arithmetic/copy error |
| M5 detailed cycle line | use the component periods from the same question | source line was copied from another example |
| M5 early rounding | full precision gives CCC 151.9312 and WCR ₹665.75 lakh | rounded daily rates produced ₹667.23 lakh |
| M5 regression intercept | y when x=0 | not y when the slope is zero |
| M5 regression forecast unit | ₹201 lakh = ₹20.1m, not ₹201m | source unit would overstate result tenfold |
| M6 share-count label | equity capital divided by face value | source arithmetic uses face value, not market price |
| M6 EPS conversion | target EPS on acquirer basis=`target EPS/q` | division preserves the comparison basis |
| M6 market-cap check | use exact EPS/price until final answer | early rounding creates false gain under no synergy |

\pagebreak

# SIX-MODULE LAST-REVISION CHECKLIST

## M1 — Finance Function and TVM
- [ ] Can define financial management and list environment: markets, institutions, instruments, regulation.
- [ ] Can map enabling/shaping/narrating and list five ethics principles.
- [ ] Can draw timeline and distinguish end versus beginning deposits.
- [ ] Can solve lump sum, uneven flows, PV/FV annuity and rate-frequency questions.
- [ ] Remember: beginning exponents run n to 1.

## M2 — Capital Structure Decision
- [ ] Can build Sales→Contribution→EBIT→EBT→PAT→EPS ladder.
- [ ] Know DOL, DFL, DCL and indifference EBIT.
- [ ] Can distinguish NI, Traditional, NOI, MM no-tax and MM tax calculation order.
- [ ] Use market weights, after-tax debt and `VL=VU+τD`.
- [ ] Can explain why practical debt is below MM-tax theoretical optimum.

## M3 — Investment Appraisal
- [ ] Include only future incremental cash flows; exclude sunk costs.
- [ ] Match nominal flows/rate and real flows/rate.
- [ ] Put opening WC at T0, changes at prior year-end, recovery at terminal date.
- [ ] Compute taxable profit, tax, add-back TAD and disposal adjustment.
- [ ] Can calculate NPV, IRR, DPP, PI and rationing choices.

## M4 — Risk Analysis
- [ ] Distinguish risk from uncertainty.
- [ ] Can compute EV, variance, SD and CV from a probability table.
- [ ] Use CE cash flows with Rf or unadjusted cash flows with RADR.
- [ ] State independence before multiplying probabilities across years.
- [ ] Report sensitivity magnitude and adverse direction; lower margin means more sensitive.

## M5 — Working Capital Decisions
- [ ] Can define permanent/temporary WC and maturity matching.
- [ ] Can annualise trade-credit discount cost with stated day basis.
- [ ] Match inventory/debtors/creditors balances with correct daily flows.
- [ ] Reconstruct RM consumed, production cost and COGS.
- [ ] Keep 365-day, lakh/million and regression units consistent.

## M6 — Mergers & Acquisitions
- [ ] Can define integration types, synergy, process and consideration forms.
- [ ] Can list pre-/post-bid defences with effects/costs.
- [ ] Define q orientation before every exchange calculation.
- [ ] Target EPS on acquirer basis is target EPS divided by q.
- [ ] Retain exact q/EPS/price so market-cap checks reconcile.

# CONSOLIDATED FORMULA INDEX

| Topic | Formula |
|---|---|
| Lump FV/PV | `FVₙ=PV₀(1+r)ⁿ`; `PV₀=FVₙ/(1+r)ⁿ` |
| m-times compounding | `FV=PV(1+j/m)ᵐⁿ` |
| Uneven FV, end | `ΣCFₜ(1+r)ⁿ⁻ᵗ` |
| Uneven FV, beginning | `ΣCFₜ(1+r)ⁿ⁻ᵗ⁺¹` |
| Annuity FV/PV | `PMT[(1+r)ⁿ−1]/r`; `PMT[1−(1+r)⁻ⁿ]/r` |
| CAPM/beta | `Ke=Rf+β(Rm−Rf)`; `β=Cov(Rp,Rm)/Var(Rm)` |
| WACC | `(E/V)Ke+(D/V)Kd(1−τ)` |
| Leverage | `DOL=C/EBIT`; `DFL=EBIT/EBT`; `DCL=C/EBT` |
| EPS/indifference | `(EBIT−I)(1−τ)/N`; `(EBIT−I₁)/N₁=(EBIT−I₂)/N₂` |
| NI value | `I=KdD`; `NI=EBIT−I`; `E=NI/Ke`; `V=E+D`; `K₀=EBIT/V` |
| NOI value | `V=EBIT/K₀`; `E=V−D`; `Ke=(EBIT−I)/E` |
| MM no tax | `VL=VU`; `KeL=KeU+(KeU−Kd)D/E` |
| MM tax | `VU=EBIT(1−τ)/KeU`; `VL=VU+τD`; `KeL=KeU+(KeU−Kd)(1−τ)D/E` |
| Inflation/Fisher | `Xₜ=X₀(1+g)ᵗ`; `1+i=(1+r)(1+h)` |
| NPV | `ΣCFₜ/(1+k)ᵗ` |
| Tax operating CF | `(revenue−cash cost)(1−τ)+τTAD` |
| WC project CF | intermediate `−ΔWC`; terminal `+WC recovery` |
| IRR interpolation | `L+[NPV_L/(NPV_L−NPV_H)](H−L)` |
| PI | `PV inflows/PV outflows = 1+NPV/I₀` for one initial outflow |
| DPP | `full years+unrecovered PV/next discounted CF` |
| Expected value | `E(X)=Σxp` |
| Variance/SD/CV | `σ²=Σx²p−E(X)²`; `σ=√σ²`; `CV=σ/E(X)` |
| CE and RADR | `CE(CF)=αE(CF)` discounted at Rf; `RADR=Rf+β(Rm−Rf)` |
| Sensitivity | `base NPV/PV affected variable×100` |
| Net WC/CCC | `WC=CA−CL`; `CCC=R+W+F+D−C` |
| Working-capital requirement | `CCC×annual operating cost/365` |
| Trade-credit cost | `d/(100−d)×365/(final day−discount day)` |
| Regression | `y=a+bx`; `b=Σdxdy/Σdx²`; `a=ȳ−bx̄` |
| Working-capital leverage | `%ΔEBIT/%ΔWC` |
| M&A ratio/shares | `q=Mtarget/Macquirer`; new shares=`q×target shares` |
| M&A EPS | `combined earnings/(acquirer shares+new shares)` |
| EPS conversion | target EPS on acquirer basis=`target EPS/q`; old-target entitlement=`q×post EPS` |
| Premium/synergy | premium=`qPacquirer−Ptarget`; synergy=`VAB−VA−VB` |
| P/E | `P/E=price/EPS`; `price=P/E×EPS` |

# ANSWER INDEX — UPLOADED PRACTICE PROBLEMS DERIVED OR CHECKED

| Source/problem | Checked answer/location in these notes |
|---|---|
| Module 1 TVM Q1–Q5 | FV: ₹70,246.40; ₹29,386.56; ₹26,620; ₹40,202.87; annual ₹1,61,051 vs half-yearly ₹1,62,889.46 — M1 §§1.2–1.3 |
| Module 1 TVM Q6–Q10 | Q6 ₹16,699.11; Q7 ₹25,611.71; Q8 ₹23,261.20; Q9 ₹7,273.73; Q10 ₹65,447.53 — M1 §1.3 |
| Module 1 FVA 1–2 | ₹46,410; ₹29,333 — M1 §1.4 method |
| Module 1 TVM Q16–Q21 | ₹12,418.43; ₹7,47,258.17; ₹76,039.01; ₹73,096.10; ₹3,60,477.62; ₹87,105.21 — M1 §§1.2–1.4 |
| M2 leverage A/B | Sunrise DCL 3.3333; Blue Horizon DCL 1.9512 — M2 §2.2 |
| M2 EBIT–EPS C/D/E | Sunshine ₹1.75 vs ₹2.94; Plan 2 ₹4.43 best in D; E indifference 9.6m — M2 §2.3 |
| M2 bank Q1–Q3 (NI) | V ₹8.80 lakh; V ₹129.6875 lakh/K₀ 15.42%; higher-debt V ₹9.20 lakh — M2 §2.4 |
| M2 bank Q4–Q5 (NOI) | V ₹31.25 lakh/Ke 19.56%; V constant ₹16 lakh — M2 §2.4 |
| M2 bank Q6–Q9 (Traditional) | Q6 ₹4 lakh debt optimum; Q7 reject; Q8 ₹3 lakh debt optimum; Q9 ₹300 crore debt optimum — M2 §2.4 |
| M2 bank Q10, Q14–Q15 (MM no tax) | V ₹2 crore/KeL 16%; intended KeL 18% in Q14; KeL 35% and WACC 21% in Q15 — M2 §2.4 |
| M2 bank Q11–Q13 (MM tax) | VL ₹1.75 lakh; no-tax V ₹16.667 lakh vs taxed V ₹10 lakh; Q13 VL ₹42.033 lakh at 30% tax — M2 §2.4 |
| M3 Problems 1–5 | nominal CF patterns; NPV −$2,103.68; four-flow NPV $29,246.64; Fisher-consistent NPV $35,095.96 — M3 §§3.1–3.2 |
| M3 Problems 6–7 | inflation/WC NPV −$15,725; multi-rate NPV about $2.164m ($2.170m rounded source) — M3 §3.3 |
| M3 Problems 8–11 | WDV NPV −$7,312.34; straight-line NPV ₹643k; Q10 annual CF ₹23,500 under stated assumptions; Q11 NPV ₹6,766,807 — M3 §3.4 |
| M3 Problems 12–15 | IRR about 10.81%; DPP 3.44y; PI 1.33; rationing NPV divisible $172.5k/indivisible $160k/exclusive C — M3 §§3.5–3.6 |
| M4 probability examples | expected NPV −₹30,743.80; A EV 4,000/CV 38.73%; B EV 5,400/CV 39.89% — M4 §4.2 |
| M4 CE examples | Golden Era CE-NPV about −$746; Machines X/Y about $6,528/$9,942, choose Y — M4 §4.3 |
| M4 RADR/sensitivity | RADR 8.4%, NPV $27,728; margins cost 26.76%, inflow 21.11%, life reduction 24.49%, IRR 21.86% — M4 §§4.4–4.5 |
| M5 Questions 1, 3–5 | aggregate WCR $213,333; Q3 CCC 30d/WCR $98,630; NovaTech CCC 85.82d/WCR 223,365; detailed Q5 CCC 151.93d/WCR ₹665.75 lakh — M5 §§5.2–5.3 |
| M5 Questions 6–7 | $4.725m forecast; ₹201 lakh forecast — M5 §5.4 |
| M6 Q1 | q NAV .811594, EPS 1.25, market 1.125 — M6 §6.5 |
| M6 Q2 | q .75 preserves EPS ₹6; q .80 gives post EPS ₹5.9375 and Y-basis accretion 5.5556% — M6 §6.5 |
| M6 Q3 | 5% headline premium; exact EPS ₹5.128205; price ₹29.74359; cap ₹116 lakh — M6 §6.6 |

**End of notes. Based on uploaded class materials; no outcome guarantee.**
