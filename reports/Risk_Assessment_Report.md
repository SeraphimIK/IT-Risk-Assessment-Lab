# IT Risk Assessment Report (Sample)

**Scope:** Sample small-business IT environment (servers, endpoints, network, cloud storage, and onboarding process)
**Methodology:** Qualitative Likelihood x Impact risk scoring (1-5 scale each), consistent with NIST SP 800-30
**Prepared as part of:** IT Risk Assessment Lab portfolio project

## 1. Objective
Identify and prioritize IT security risks across the in-scope environment,
assess whether existing controls adequately reduce those risks, and
recommend remediation aligned to the NIST Cybersecurity Framework (CSF).

## 2. Summary of Findings
Ten assets were assessed across servers, endpoints, network infrastructure,
a database, cloud storage, and an internal process. Of these, three risks
were rated **High**, six **Medium**, and one **Low** (see
`output/risk_register_prioritized.csv` for full detail after running the
script).

The most significant findings:

- **VPN Gateway (Score 15, High):** Remote access is protected by
  single-factor authentication only, with no multi-factor authentication
  (MFA) required. This is the highest-risk finding, since a compromised
  password would allow direct access to internal systems.
- **Domain Controller (Score 20, High):** Password policy exists but is
  not enforced for complexity or expiration, undermining the primary
  control for a system with domain-wide privileges.
- **Finance File Server (Score 15, High):** Access reviews occur only
  quarterly and manually, creating an extended window where excess
  privileges could go undetected.
- **Customer Database (Score 10, Medium):** Partial WAF coverage does not
  fully mitigate injection risk at the application layer.

## 3. Control Effectiveness Assessment
Several existing controls were found to be only partially effective:

- Antivirus (signature-based) does not address modern, behavior-based
  malware, leaving a detection gap that EDR would close.
- Manual, infrequent access reviews (quarterly, verbal approvals) are a
  recurring theme across three separate findings, suggesting a broader
  process gap in access governance rather than an isolated issue.
- Patch management exists as a process but is not consistently followed,
  indicating an enforcement gap rather than a design gap.

## 4. Recommendations
Recommendations are detailed per-risk in `risk_control_matrix.md`. At a
program level:

1. Prioritize MFA enforcement for all remote access (VPN) immediately,
   given the High rating and broad potential impact.
2. Formalize and automate access governance (reviews, approvals, and
   onboarding) rather than addressing each system individually, since the
   underlying gap is procedural.
3. Establish a patch management SLA with defined timeframes and
   compliance tracking.

## 5. Conclusion
The environment shows reasonable baseline controls (antivirus, passcodes,
firewalls) but several are not fully enforced or are managed manually,
which is the common root cause behind the highest-rated risks. Addressing
access governance and MFA would meaningfully reduce overall risk exposure.
