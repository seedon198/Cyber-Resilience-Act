# Industrial Control Systems (ICS/OT) Security Checklist - CRA Compliance

*Version 1.0 | Last Updated: July 2025*

## Overview

This checklist provides comprehensive guidance for assessing Industrial Control Systems (ICS) and Operational Technology (OT) environments against EU Cyber Resilience Act requirements. It focuses on critical infrastructure, manufacturing systems, and industrial automation components.

## Scope and Applicability

### Target Systems
- **SCADA Systems** - Supervisory Control and Data Acquisition
- **DCS Systems** - Distributed Control Systems  
- **PLC Networks** - Programmable Logic Controllers
- **HMI Interfaces** - Human Machine Interfaces
- **Industrial IoT** - Connected industrial devices
- **Safety Systems** - Safety Instrumented Systems (SIS)

### Regulatory Context
- EU Cyber Resilience Act compliance requirements
- IEC 62443 industrial cybersecurity standards
- Functional safety standards (IEC 61508, IEC 61511)
- Network and Information Systems (NIS2) Directive alignment

## Pre-Assessment Preparation

### Documentation Review
- [ ] **System Architecture Documentation**
  - Network topology diagrams
  - Zone and conduit segmentation
  - Data flow documentation
  - Integration points with corporate networks

- [ ] **Asset Inventory**
  - Complete OT asset register
  - Firmware and software versions
  - Communication protocols in use
  - Legacy system identification

- [ ] **Risk Assessment Documentation**
  - Existing cybersecurity risk assessments
  - Safety integrity level (SIL) classifications
  - Business impact analysis
  - Threat landscape assessment

## Core Assessment Areas

### 1. Network Security and Segmentation

#### Network Architecture
- [ ] **Zone Segregation Implementation**
  - Manufacturing zones properly segmented
  - DMZ implementation between OT/IT networks
  - Air-gapped systems where required
  - Wireless network segregation

- [ ] **Access Control Mechanisms**
  - Network access control (NAC) implementation
  - Multi-factor authentication for remote access
  - VPN security for external connections
  - Time-based access restrictions

#### Network Security Assessment Criteria
| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Network segmentation per IEC 62443-3-2 | ⚪ | | |
| Firewall rules documented and reviewed | ⚪ | | |
| Intrusion detection systems deployed | ⚪ | | |
| Network monitoring and logging enabled | ⚪ | | |

### 2. Device and Component Security

#### Hardware Security
- [ ] **Secure Boot Implementation**
  - Verified boot process for critical controllers
  - Hardware security modules (HSM) usage
  - Tamper detection mechanisms
  - Physical security controls

- [ ] **Configuration Management**
  - Default password changes
  - Secure configuration baselines
  - Configuration change control
  - Backup and recovery procedures

#### Device Security Assessment Criteria
| Component Type | Secure Configuration | Access Control | Monitoring | Compliance Status |
|----------------|---------------------|----------------|------------|-------------------|
| PLCs | ⚪ | ⚪ | ⚪ | |
| HMIs | ⚪ | ⚪ | ⚪ | |
| SCADA Servers | ⚪ | ⚪ | ⚪ | |
| Engineering Workstations | ⚪ | ⚪ | ⚪ | |

### 3. Communication Protocol Security

#### Protocol Analysis
- [ ] **Legacy Protocol Assessment**
  - Unencrypted protocol identification
  - Authentication mechanism review
  - Message integrity verification
  - Protocol vulnerability assessment

- [ ] **Modern Protocol Implementation**
  - OPC UA security implementation
  - Certificate management
  - Secure tunneling protocols
  - Protocol-specific security features

#### Protocol Security Assessment Criteria
| Protocol | Encryption | Authentication | Integrity | Availability | Status |
|----------|------------|----------------|-----------|--------------|--------|
| Modbus | ⚪ | ⚪ | ⚪ | ⚪ | |
| DNP3 | ⚪ | ⚪ | ⚪ | ⚪ | |
| OPC UA | ⚪ | ⚪ | ⚪ | ⚪ | |
| Ethernet/IP | ⚪ | ⚪ | ⚪ | ⚪ | |

### 4. Vulnerability Management

#### Vulnerability Assessment Process
- [ ] **Regular Security Scanning**
  - OT-specific vulnerability scanners
  - Non-disruptive assessment methods
  - Baseline security posture establishment
  - Continuous monitoring implementation

- [ ] **Patch Management**
  - Vendor patch notification system
  - Testing procedures for critical systems
  - Emergency patching procedures
  - Legacy system exception handling

#### Vulnerability Management Assessment Criteria
| Area | Implementation | Testing | Documentation | Status |
|------|----------------|---------|---------------|--------|
| Vulnerability Scanning | ⚪ | ⚪ | ⚪ | |
| Patch Management | ⚪ | ⚪ | ⚪ | |
| Configuration Management | ⚪ | ⚪ | ⚪ | |
| Change Control | ⚪ | ⚪ | ⚪ | |

### 5. Incident Response and Recovery

#### Incident Response Capability
- [ ] **OT-Specific Incident Response Plan**
  - Industrial system-specific procedures
  - Safety system protection measures
  - Communication protocols during incidents
  - Recovery time objectives (RTO) definition

- [ ] **Business Continuity Planning**
  - Production continuity procedures
  - Manual operation capabilities
  - Backup system activation
  - Supply chain impact assessment

#### Incident Response Assessment Criteria
| Capability | Documented | Tested | Trained | Status |
|------------|------------|--------|---------|--------|
| Incident Detection | ⚪ | ⚪ | ⚪ | |
| Response Procedures | ⚪ | ⚪ | ⚪ | |
| Recovery Planning | ⚪ | ⚪ | ⚪ | |
| Communication Plan | ⚪ | ⚪ | ⚪ | |

## Safety-Security Integration

### Functional Safety Considerations
- [ ] **Safety System Protection**
  - SIL-rated system segregation
  - Safety instrumented function protection
  - Cybersecurity impact on safety functions
  - Safety lifecycle process integration

- [ ] **Fail-Safe Mechanisms**
  - Secure failure modes
  - Safety system override capabilities
  - Emergency shutdown procedures
  - Human factor considerations

## Compliance Verification

### CRA-Specific Requirements
- [ ] **Product Documentation**
  - CE marking compliance for applicable products
  - Cybersecurity risk assessment documentation
  - Vulnerability disclosure procedures
  - Support and maintenance commitments

- [ ] **Supply Chain Security**
  - Vendor cybersecurity assessments
  - Third-party component evaluation
  - Software bill of materials (SBOM)
  - Supply chain risk management

### Assessment Summary
| Compliance Area | Score | Critical Findings | Recommendations |
|----------------|-------|-------------------|-----------------|
| Network Security | __/100 | | |
| Device Security | __/100 | | |
| Protocol Security | __/100 | | |
| Vulnerability Management | __/100 | | |
| Incident Response | __/100 | | |
| **Overall Score** | **__/100** | | |

## Risk Classification

### Risk Levels
- **Critical (90-100)** - Immediate action required
- **High (70-89)** - Action required within 30 days
- **Medium (50-69)** - Action required within 90 days
- **Low (0-49)** - Action required within 180 days

### Priority Actions
1. **Immediate (Critical)**
   - [ ] Critical vulnerability remediation
   - [ ] Safety system protection
   - [ ] Emergency response capability

2. **Short-term (High)**
   - [ ] Network segmentation improvements
   - [ ] Access control enhancements
   - [ ] Monitoring system deployment

3. **Medium-term (Medium)**
   - [ ] Protocol security upgrades
   - [ ] Training program implementation
   - [ ] Documentation updates

## Tools and Resources

### Recommended Assessment Tools
- **Nessus Industrial Security** - Vulnerability scanning
- **Claroty Platform** - OT asset discovery and monitoring
- **Dragos WorldView** - ICS threat intelligence
- **Schneider Electric EcoStruxure** - Security assessment
- **Siemens Industrial Security Scanner** - Network analysis

### Standards and Guidelines
- **IEC 62443** - Industrial cybersecurity standards series
- **NIST Cybersecurity Framework** - Risk management
- **ICS-CERT Guidelines** - Industrial control systems security
- **ENISA Guidelines** - European cybersecurity guidance

## Next Steps and Recommendations

### Immediate Actions
1. Address all critical and high-risk findings
2. Implement emergency response procedures
3. Establish continuous monitoring capabilities
4. Initiate vendor security assessments

### Long-term Strategic Initiatives
1. Develop comprehensive OT security program
2. Implement security-by-design principles
3. Establish security metrics and KPIs
4. Create security awareness training program

---

**Assessment Conducted By:** ________________________  
**Date:** ________________________  
**Next Review Date:** ________________________  

*This checklist aligns with EU Cyber Resilience Act requirements and industry best practices. Regular updates ensure continued compliance with evolving regulations and threat landscape.*
