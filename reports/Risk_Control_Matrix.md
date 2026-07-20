# Risk and Control Matrix

Maps each identified risk to its current control, the control gap, a
recommended remediation, and the related NIST Cybersecurity Framework (CSF)
function. Used to translate raw risk-register findings into an audit-style
remediation plan.

| Asset | Risk | Current Control | Gap | Recommendation | NIST CSF Function |
|---|---|---|---|---|---|
| Domain Controller | Unauthorized access via weak passwords | Basic AD password policy, not enforced | No complexity/expiration enforcement | Enforce password complexity and expiration via Group Policy | Protect (PR.AC) |
| Employee Workstations | Malware infection | Signature-based antivirus only | No behavioral/EDR detection | Deploy EDR solution with real-time monitoring | Detect (DE.CM) |
| Finance File Server | Data exfiltration via excess privilege | Manual quarterly access review | Reviews are infrequent and manual | Implement automated least-privilege access reviews (monthly) | Protect (PR.AC) |
| Guest Wi-Fi | Network intrusion via unsegmented network | Monthly password rotation | No network segmentation | Segment guest network on separate VLAN with no internal routing | Protect (PR.AC) |
| Remote Laptops | Device theft/loss | Passcode required | No full-disk encryption | Enforce full-disk encryption (e.g., BitLocker) on all endpoints | Protect (PR.DS) |
| Customer Database | SQL injection | Partial web application firewall coverage | Input fields not fully sanitized | Implement parameterized queries and expand WAF rule coverage | Protect (PR.DS) |
| Cloud Backup Storage | Misconfigured access | Access limited to IT admin group | No recurring configuration audit | Enable automated cloud configuration/posture monitoring | Detect (DE.CM) |
| VPN Gateway | Credential stuffing | Single-factor authentication | No MFA | Require MFA for all remote access | Protect (PR.AC) |
| Print Server | Outdated software | Inconsistent patch management | Patches 90+ days behind | Formalize patch management SLA (30-day max) | Protect (PR.IP) |
| Onboarding Process | Excess access granted | Verbal manager approval only | No formal workflow or audit trail | Implement documented access request/approval workflow | Identify (ID.GV) / Protect (PR.AC) |

## Notes
- Control gaps above were identified using a qualitative Likelihood x Impact
  risk-scoring model (see `risk_assessment.py`), consistent with the approach
  in NIST SP 800-30.
- The NIST CSF Function column shows which of the five core functions
  (Identify, Protect, Detect, Respond, Recover) each recommendation
  strengthens.
