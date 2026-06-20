# Citations

Track 23 implements the current public and community housing income-related
rent surface from these official sources:

- Public and Community Housing Management Act 1992, sections 104, 106, 107,
  108 to 112, 116, 118A, and Schedule 4 Part 6:
  https://www.legislation.govt.nz/act/public/1992/0076/latest/whole.html
- Public and Community Housing Management (Prescribed Elements of Calculation
  Mechanism) Regulations 2018, regulations 5 to 10 and Schedule Part 4:
  https://www.legislation.govt.nz/regulation/public/2018/0173/latest/whole.html
- Work and Income, "Calculating your rent payments":
  https://www.workandincome.govt.nz/housing/live-in-home/live-in-public-housing/calculating-rent-payments.html

The implementation separates statutory/regulatory formulas from agency
judgment inputs. Weekly assessable income, the appropriate Jobseeker Support
floor, market rent, minimum rent, unresolved discrepancy status, and whether a
calculation is excluded from the 2 March 2026 amendments are model inputs.
