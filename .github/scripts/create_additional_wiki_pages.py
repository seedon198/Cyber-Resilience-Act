#!/usr/bin/env python3
"""
Comprehensive Wiki Content Creator
Creates additional specialized wiki pages for CRA compliance
"""

import os
import subprocess
import tempfile
from datetime import datetime

class WikiContentCreator:
    def __init__(self):
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.repo_owner = 'seedon198'
        self.repo_name = 'Cyber-Resilience-Act'
        
    def create_wiki_page(self, page_name, content, message=None):
        """Create or update a wiki page using git operations"""
        with tempfile.TemporaryDirectory() as temp_dir:
            wiki_repo = f"https://{self.github_token}@github.com/{self.repo_owner}/{self.repo_name}.wiki.git"
            
            try:
                # Clone wiki repo
                subprocess.run(['git', 'clone', wiki_repo, temp_dir], 
                             check=True, capture_output=True)
                
                # Write content to file
                page_file = os.path.join(temp_dir, f"{page_name}.md")
                with open(page_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Configure git
                subprocess.run(['git', 'config', 'user.email', 'action@github.com'], 
                             cwd=temp_dir, check=True)
                subprocess.run(['git', 'config', 'user.name', 'GitHub Action'], 
                             cwd=temp_dir, check=True)
                
                # Add and commit
                subprocess.run(['git', 'add', f"{page_name}.md"], 
                             cwd=temp_dir, check=True)
                commit_message = message or f"Update {page_name} wiki page"
                subprocess.run(['git', 'commit', '-m', commit_message], 
                             cwd=temp_dir, check=True)
                
                # Push changes
                subprocess.run(['git', 'push'], cwd=temp_dir, check=True)
                
                print(f"✅ Successfully created/updated wiki page: {page_name}")
                return True
                
            except subprocess.CalledProcessError as e:
                print(f"❌ Error updating wiki page {page_name}: {e}")
                return False

    def get_implementation_guide_content(self):
        """Implementation Guide page content"""
        return """# Implementation Guide - Step-by-Step CRA Compliance

This comprehensive guide provides detailed implementation steps for achieving CRA compliance, organized by organizational readiness level and product type.

## 🎯 Implementation Phases

### Phase 1: Assessment & Planning (Months 1-3)

#### 1.1 Organizational Readiness Assessment
**Week 1-2: Initial Assessment**
- Complete [Compliance Assessment](Compliance-Assessment)
- Identify key stakeholders and form compliance team
- Establish communication channels and governance
- Document current security posture and capabilities

**Week 3-4: Gap Analysis**
- Map current practices to CRA essential requirements
- Prioritize gaps by risk and implementation complexity
- Estimate resources and timeline for remediation
- Develop high-level implementation roadmap

**Week 5-8: Strategic Planning**
- Secure management commitment and budget approval
- Define roles and responsibilities for compliance team
- Establish project management framework and milestones
- Engage external expertise where needed (legal, technical)

**Week 9-12: Detailed Planning**
- Create detailed work breakdown structure
- Develop implementation timeline with dependencies
- Establish success metrics and monitoring procedures
- Finalize team structure and resource allocation

#### 1.2 Key Deliverables Phase 1
- [ ] Compliance assessment report
- [ ] Gap analysis with prioritized remediation plan
- [ ] Implementation project charter and budget
- [ ] Team structure and responsibility matrix
- [ ] Detailed implementation timeline and milestones

### Phase 2: Foundation Building (Months 4-9)

#### 2.1 Security Framework Implementation
**Months 4-5: Secure by Design**
- Establish security architecture review board
- Implement threat modeling for existing and new products
- Create secure design principles and guidelines
- Integrate security requirements into development lifecycle
- Train development teams on secure design practices

**Months 5-6: Secure by Default**
- Audit current product default configurations
- Implement secure default configuration standards
- Eliminate or force change of default credentials
- Disable unnecessary services and features by default
- Validate secure defaults across product portfolio

**Months 6-7: Vulnerability Management**
- Establish vulnerability disclosure policy and process
- Implement security contact and communication channels
- Create vulnerability assessment and prioritization procedures
- Establish coordinated disclosure timelines and processes
- Implement vulnerability tracking and management system

**Months 7-8: Security Update Management**
- Design and implement automated update mechanisms
- Implement update integrity protection (code signing)
- Create rollback capabilities for failed updates
- Establish update notification and communication procedures
- Define end-of-support lifecycle policies

**Months 8-9: Incident Response**
- Develop cybersecurity incident response plan
- Establish incident detection and monitoring capabilities
- Create stakeholder notification and communication procedures
- Implement incident documentation and tracking systems
- Conduct incident response training and exercises

#### 2.2 Key Deliverables Phase 2
- [ ] Security architecture and design standards
- [ ] Secure default configuration implementation
- [ ] Vulnerability management program
- [ ] Security update delivery system
- [ ] Incident response capabilities

### Phase 3: Documentation & Assessment (Months 10-15)

#### 3.1 Technical Documentation
**Months 10-11: Core Documentation**
- Create comprehensive security documentation
- Document risk assessment methodologies and results
- Detail security control implementation and evidence
- Prepare testing and validation documentation
- Organize technical file structure for conformity assessment

**Months 11-12: Quality Management Integration**
- Integrate cybersecurity into quality management system
- Document security-related procedures and controls
- Establish management review processes for cybersecurity
- Create continuous improvement procedures
- Document supplier security requirements and assessments

**Months 12-13: Conformity Assessment Preparation**
- Identify applicable harmonized standards
- Prepare technical files according to CRA Annex V
- Draft EU Declaration of Conformity
- Engage notified body for Class II products
- Prepare for conformity assessment procedures

#### 3.2 Third-Party Assessment (Class II Products)
**Months 13-14: Notified Body Engagement**
- Select and contract appropriate notified body
- Submit technical documentation for review
- Respond to notified body queries and requests
- Conduct required testing and evaluations
- Address any non-conformities identified

**Months 14-15: Assessment Completion**
- Receive notified body certificate or declaration
- Finalize EU Declaration of Conformity
- Implement CE marking on products and documentation
- Prepare for market surveillance compliance
- Document conformity assessment evidence

#### 3.3 Key Deliverables Phase 3
- [ ] Complete technical documentation package
- [ ] Quality management system integration
- [ ] Conformity assessment completion
- [ ] EU Declaration of Conformity
- [ ] CE marking implementation

### Phase 4: Market Readiness (Months 16-18)

#### 4.1 Operational Readiness
**Month 16: Monitoring & Response**
- Implement ongoing security monitoring
- Establish incident response operational procedures
- Create market surveillance response capabilities
- Implement post-market security monitoring
- Establish customer security support procedures

**Month 17: Training & Communication**
- Train sales and marketing teams on CRA compliance
- Develop customer communication materials
- Create compliance marketing messaging
- Prepare technical support documentation
- Establish compliance communication procedures

**Month 18: Launch Preparation**
- Conduct final compliance verification
- Complete pre-launch security testing
- Finalize all documentation and marking
- Prepare for ongoing compliance monitoring
- Establish post-launch improvement processes

#### 4.2 Key Deliverables Phase 4
- [ ] Operational security monitoring
- [ ] Team training completion
- [ ] Customer communication materials
- [ ] Final compliance verification
- [ ] Market launch readiness

## 🔧 Technical Implementation Details

### Essential Requirement 1: Secure by Design

#### Design Phase Security Integration
**Security Architecture Review**
```
1. Threat Modeling
   - Identify assets, threats, and vulnerabilities
   - Analyze attack vectors and impact scenarios
   - Design countermeasures and security controls
   - Document security architecture decisions

2. Security Requirements Definition
   - Define functional security requirements
   - Specify non-functional security requirements
   - Establish security acceptance criteria
   - Integrate with overall product requirements

3. Security Design Principles
   - Implement defense in depth
   - Apply principle of least privilege
   - Design for fail-safe defaults
   - Minimize attack surface
```

**Development Integration**
- Security requirements traceability
- Secure coding standards and guidelines
- Security-focused code review procedures
- Security testing integration in CI/CD
- Third-party component security assessment

### Essential Requirement 2: Secure by Default

#### Configuration Management
**Default Security Settings**
```
1. Authentication & Access Control
   - Strong default password policies
   - Multi-factor authentication where applicable
   - Role-based access control implementation
   - Session management and timeout controls

2. Network Security
   - Firewall rules and network segmentation
   - Encrypted communication by default
   - Secure protocol selection and configuration
   - Network service hardening

3. Data Protection
   - Encryption at rest and in transit
   - Secure key management practices
   - Data classification and handling procedures
   - Privacy-preserving default settings
```

**User Experience Design**
- Security-usability balance optimization
- Clear security status indication
- Guided security configuration workflows
- Security awareness and education features

### Essential Requirement 3: Vulnerability Management

#### Vulnerability Disclosure Program
**Policy and Procedures**
```
1. Disclosure Policy Elements
   - Scope of covered products and versions
   - Communication channels and contact information
   - Response timelines and service level agreements
   - Coordinated disclosure procedures
   - Recognition and acknowledgment procedures

2. Vulnerability Assessment Process
   - Severity scoring and prioritization criteria
   - Impact analysis and risk assessment procedures
   - Exploitation likelihood and attack complexity evaluation
   - Business impact and remediation effort assessment

3. Remediation and Communication
   - Patch development and testing procedures
   - Security advisory creation and publication
   - Customer notification and support procedures
   - Public disclosure timing and coordination
```

**Technical Implementation**
- Vulnerability tracking and management system
- Security testing and validation procedures
- Patch development and deployment automation
- Security advisory management platform

### Essential Requirement 4: Security Updates

#### Update Delivery System
**Technical Architecture**
```
1. Update Mechanism Design
   - Automated update discovery and download
   - Update integrity verification (digital signatures)
   - Incremental and full update capabilities
   - Rollback and recovery mechanisms

2. Update Management
   - Update scheduling and maintenance windows
   - User notification and consent procedures
   - Update status monitoring and reporting
   - Failed update detection and recovery

3. Lifecycle Management
   - Update support duration policies
   - End-of-support communication procedures
   - Legacy version security support
   - Migration assistance for unsupported versions
```

**Implementation Considerations**
- Bandwidth and storage optimization
- Network connectivity reliability
- Update verification and validation
- User experience and transparency

### Essential Requirement 5: Incident Response

#### Incident Management System
**Organizational Capabilities**
```
1. Incident Response Team Structure
   - Team roles and responsibilities definition
   - Escalation procedures and decision authority
   - Communication channels and coordination procedures
   - External stakeholder engagement protocols

2. Incident Detection and Analysis
   - Security monitoring and alerting systems
   - Incident classification and prioritization
   - Forensic analysis and evidence collection
   - Impact assessment and damage evaluation

3. Response and Recovery
   - Containment and mitigation procedures
   - Recovery and restoration processes
   - Communication and notification procedures
   - Lessons learned and improvement processes
```

**Technical Implementation**
- Security information and event management (SIEM)
- Incident tracking and case management system
- Communication and notification automation
- Post-incident analysis and reporting tools

## 📊 Industry-Specific Implementation

### IoT and Consumer Electronics
**Special Considerations:**
- Resource-constrained device security
- Over-the-air update mechanisms
- Consumer privacy protection
- Device lifecycle management
- **[Detailed guidance: IoT Implementation](IoT-and-Consumer-Electronics)**

### Industrial Control Systems
**Special Considerations:**
- Safety-security integration requirements
- Legacy system retrofit challenges
- Operational technology security
- Critical infrastructure protection
- **[Detailed guidance: ICS Implementation](Industrial-Control-Systems)**

### Software and Services
**Special Considerations:**
- Application security requirements
- Cloud service security
- API security and integration
- Software composition analysis
- **[Detailed guidance: Software Implementation](Software-and-Services)**

## 📋 Implementation Checklists

### Phase 1 Checklist: Assessment & Planning
- [ ] Complete organizational readiness assessment
- [ ] Identify all applicable products and classifications
- [ ] Form compliance team with defined roles
- [ ] Conduct comprehensive gap analysis
- [ ] Develop implementation budget and timeline
- [ ] Secure management commitment and resources
- [ ] Establish project governance and communication
- [ ] Engage external expertise where needed
- [ ] Create detailed implementation plan
- [ ] Establish success metrics and monitoring

### Phase 2 Checklist: Foundation Building
- [ ] Implement secure by design practices
- [ ] Establish secure default configurations
- [ ] Create vulnerability management program
- [ ] Implement security update delivery system
- [ ] Develop incident response capabilities
- [ ] Train teams on new procedures
- [ ] Establish security monitoring
- [ ] Document processes and procedures
- [ ] Conduct initial testing and validation
- [ ] Review and refine implementation

### Phase 3 Checklist: Documentation & Assessment
- [ ] Create comprehensive technical documentation
- [ ] Integrate cybersecurity into quality management
- [ ] Prepare conformity assessment package
- [ ] Engage notified body (Class II products)
- [ ] Complete required testing and evaluation
- [ ] Finalize EU Declaration of Conformity
- [ ] Implement CE marking procedures
- [ ] Document evidence and maintain records
- [ ] Prepare for market surveillance
- [ ] Establish ongoing compliance monitoring

### Phase 4 Checklist: Market Readiness
- [ ] Implement operational security monitoring
- [ ] Train customer-facing teams
- [ ] Develop customer communication materials
- [ ] Conduct final compliance verification
- [ ] Prepare post-launch improvement processes
- [ ] Establish ongoing maintenance procedures
- [ ] Create compliance communication strategy
- [ ] Finalize launch readiness verification
- [ ] Implement continuous improvement
- [ ] Monitor and respond to market feedback

## 🎓 Training and Change Management

### Team Training Programs
**Compliance Team Training:**
- CRA regulatory requirements and obligations
- Technical implementation best practices
- Documentation and assessment procedures
- Project management and coordination skills

**Technical Team Training:**
- Secure design and development practices
- Security testing and validation methods
- Vulnerability management procedures
- Incident response and crisis management

**Management Training:**
- CRA business impact and requirements
- Compliance governance and oversight
- Risk management and decision making
- Customer communication and positioning

### Change Management Strategy
- Clear communication of compliance objectives
- Regular progress updates and milestone celebration
- Team engagement and feedback collection
- Resistance identification and mitigation
- Success story sharing and recognition

## 📞 Support and Resources

### Implementation Support
- **[Technical Standards](Technical-Standards)** - Detailed technical requirements
- **[Document Templates](Document-Templates)** - Pre-formatted compliance documents
- **[Testing Frameworks](Testing-Frameworks)** - Security assessment methodologies
- **[Best Practices](Best-Practices)** - Industry-proven implementation approaches

### Community Resources
- **[GitHub Discussions](https://github.com/seedon198/Cyber-Resilience-Act/discussions)** - Implementation Q&A
- **[Case Studies](Case-Studies)** - Real-world implementation examples
- **[Latest News](Latest-News)** - Regulatory updates and developments
- **[FAQ](Frequently-Asked-Questions)** - Common implementation questions

---

*Ready to start implementation? Choose your phase:*
- **Just starting?** → [Getting Started Guide](Getting-Started)
- **Need assessment?** → [Compliance Assessment](Compliance-Assessment)
- **Technical focus?** → [Technical Implementation](Technical-Implementation)
- **Documentation help?** → [Document Templates](Document-Templates)
"""

    def get_technical_implementation_content(self):
        """Technical Implementation page content"""
        return """# Technical Implementation - CRA Security Controls

This guide provides detailed technical implementation guidance for CRA essential requirements, with practical examples and code snippets.

## 🔒 Essential Requirement 1: Secure by Design

### Security Architecture Framework

#### Threat Modeling Implementation
```python
# Example: Threat modeling automation script
import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Asset:
    name: str
    criticality: str  # High, Medium, Low
    data_classification: str
    
@dataclass
class Threat:
    id: str
    name: str
    description: str
    stride_category: str  # Spoofing, Tampering, Repudiation, etc.
    likelihood: int  # 1-5 scale
    impact: int  # 1-5 scale
    
@dataclass
class Control:
    id: str
    name: str
    description: str
    control_type: str  # Preventive, Detective, Corrective
    implementation_status: str

class ThreatModel:
    def __init__(self, product_name: str):
        self.product_name = product_name
        self.assets: List[Asset] = []
        self.threats: List[Threat] = []
        self.controls: List[Control] = []
    
    def calculate_risk_score(self, threat: Threat) -> int:
        return threat.likelihood * threat.impact
    
    def generate_report(self) -> Dict:
        high_risks = [t for t in self.threats if self.calculate_risk_score(t) >= 15]
        return {
            "product": self.product_name,
            "total_threats": len(self.threats),
            "high_risk_threats": len(high_risks),
            "control_coverage": len(self.controls)
        }
```

#### Security Requirements Integration
```yaml
# Example: Security requirements in product backlog
security_requirements:
  authentication:
    - id: "AUTH-001"
      requirement: "Multi-factor authentication for administrative access"
      priority: "High"
      acceptance_criteria:
        - "Admin users must provide at least two authentication factors"
        - "Authentication factors include something you know, have, or are"
        - "Fallback authentication method available"
      
  encryption:
    - id: "ENC-001"
      requirement: "Data encryption at rest and in transit"
      priority: "High"
      acceptance_criteria:
        - "All sensitive data encrypted using AES-256"
        - "TLS 1.3 minimum for data in transit"
        - "Key rotation every 90 days"
        
  access_control:
    - id: "AC-001"
      requirement: "Role-based access control implementation"
      priority: "Medium"
      acceptance_criteria:
        - "User roles defined with specific permissions"
        - "Principle of least privilege enforced"
        - "Regular access review and certification"
```

### Secure Development Lifecycle Integration

#### Secure Coding Standards
```python
# Example: Secure coding checklist automation
class SecureCodeChecker:
    def __init__(self):
        self.rules = {
            'input_validation': [
                'Validate all input parameters',
                'Sanitize user-provided data',
                'Use parameterized queries for database access'
            ],
            'authentication': [
                'Use strong password policies',
                'Implement account lockout mechanisms',
                'Store passwords using secure hashing'
            ],
            'session_management': [
                'Generate unique session identifiers',
                'Implement session timeout',
                'Secure session storage and transmission'
            ]
        }
    
    def check_code(self, code_file: str) -> Dict[str, List[str]]:
        findings = {'violations': [], 'recommendations': []}
        
        # Example checks (simplified)
        with open(code_file, 'r') as f:
            content = f.read()
            
        if 'password' in content.lower() and 'hash' not in content.lower():
            findings['violations'].append('Password handling without hashing detected')
            
        if 'SELECT' in content and '%s' in content:
            findings['violations'].append('Potential SQL injection vulnerability')
            
        return findings
```

#### Security Testing Integration
```yaml
# Example: CI/CD security testing pipeline
security_testing_pipeline:
  stages:
    - name: "Static Analysis"
      tools:
        - sonarqube
        - bandit  # Python security linter
        - eslint-security  # JavaScript security rules
      fail_on: "high_severity_findings"
      
    - name: "Dependency Scanning"
      tools:
        - safety  # Python dependency security
        - npm-audit  # Node.js dependency security
        - owasp-dependency-check
      fail_on: "critical_vulnerabilities"
      
    - name: "Dynamic Testing"
      tools:
        - zap_baseline_scan
        - custom_security_tests
      fail_on: "medium_and_above"
      
    - name: "Infrastructure Security"
      tools:
        - terraform_security_scan
        - docker_security_scan
        - kubernetes_security_check
      fail_on: "configuration_violations"
```

## 🛡️ Essential Requirement 2: Secure by Default

### Default Configuration Management

#### Configuration Security Framework
```python
# Example: Secure configuration management
import yaml
from typing import Dict, Any

class SecureConfigManager:
    def __init__(self):
        self.security_defaults = {
            'authentication': {
                'password_policy': {
                    'min_length': 12,
                    'complexity_required': True,
                    'history_check': 5,
                    'expiry_days': 90
                },
                'session_timeout': 30,  # minutes
                'max_failed_attempts': 3,
                'lockout_duration': 15  # minutes
            },
            'network': {
                'encryption_required': True,
                'min_tls_version': '1.3',
                'unused_ports_disabled': True,
                'firewall_enabled': True
            },
            'logging': {
                'security_events_logged': True,
                'log_retention_days': 365,
                'log_integrity_protection': True
            }
        }
    
    def generate_secure_config(self, product_type: str) -> Dict[str, Any]:
        config = self.security_defaults.copy()
        
        # Customize based on product type
        if product_type == 'iot_device':
            config['network']['auto_update_enabled'] = True
            config['device']['debug_mode_disabled'] = True
            
        elif product_type == 'enterprise_software':
            config['authentication']['mfa_required'] = True
            config['audit']['compliance_logging'] = True
            
        return config
    
    def validate_config(self, config: Dict[str, Any]) -> List[str]:
        violations = []
        
        # Check password policy
        if config.get('authentication', {}).get('password_policy', {}).get('min_length', 0) < 8:
            violations.append('Password minimum length below security baseline')
            
        # Check encryption
        if not config.get('network', {}).get('encryption_required', False):
            violations.append('Network encryption not enforced')
            
        return violations
```

#### Default Security Settings Implementation
```bash
#!/bin/bash
# Example: System hardening script for IoT devices

# Disable unnecessary services
systemctl disable bluetooth
systemctl disable wifi-direct
systemctl disable ssh  # Unless specifically required

# Configure firewall defaults
ufw --force enable
ufw default deny incoming
ufw default allow outgoing

# Set secure file permissions
chmod 600 /etc/shadow
chmod 644 /etc/passwd
chmod 644 /etc/group

# Configure secure defaults for network
echo "net.ipv4.ip_forward=0" >> /etc/sysctl.conf
echo "net.ipv4.conf.all.send_redirects=0" >> /etc/sysctl.conf
echo "net.ipv4.conf.all.accept_redirects=0" >> /etc/sysctl.conf

# Apply security kernel parameters
sysctl -p

# Set up automatic security updates
cat > /etc/apt/apt.conf.d/20auto-upgrades << EOF
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
APT::Periodic::AutocleanInterval "7";
EOF
```

### User Experience Security Design

#### Security-Usability Balance
```javascript
// Example: User-friendly security implementation
class SecurityUXManager {
    constructor() {
        this.securityLevel = 'standard';
        this.userPreferences = {};
    }
    
    // Progressive security disclosure
    showSecuritySettings(userType) {
        const settings = {
            'basic': [
                'password_change',
                'two_factor_setup',
                'privacy_settings'
            ],
            'advanced': [
                'encryption_options',
                'audit_log_access',
                'api_key_management',
                'session_management'
            ],
            'expert': [
                'security_policy_config',
                'advanced_logging',
                'custom_rules',
                'integration_settings'
            ]
        };
        
        return settings[userType] || settings['basic'];
    }
    
    // Security status dashboard
    getSecurityStatus() {
        return {
            overall_score: this.calculateSecurityScore(),
            active_threats: this.getActiveThreats(),
            recommendations: this.getSecurityRecommendations(),
            compliance_status: this.getComplianceStatus()
        };
    }
    
    // Guided security setup
    generateSetupWizard() {
        return [
            {
                step: 1,
                title: "Account Security",
                description: "Set up strong authentication",
                required: true,
                actions: ['set_password', 'enable_2fa']
            },
            {
                step: 2,
                title: "Privacy Settings",
                description: "Configure data sharing preferences",
                required: false,
                actions: ['data_retention', 'sharing_preferences']
            }
        ];
    }
}
```

## 🔍 Essential Requirement 3: Vulnerability Management

### Vulnerability Disclosure Program

#### Automated Vulnerability Tracking
```python
# Example: Vulnerability management system
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum

class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"

class Status(Enum):
    OPEN = "open"
    ACKNOWLEDGED = "acknowledged"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

@dataclass
class Vulnerability:
    id: str
    title: str
    description: str
    severity: Severity
    status: Status
    reporter: str
    reported_date: datetime
    affected_products: list
    cvss_score: float
    cve_id: str = None
    
class VulnerabilityManager:
    def __init__(self):
        self.vulnerabilities = {}
        self.sla_times = {
            Severity.CRITICAL: timedelta(days=1),
            Severity.HIGH: timedelta(days=7),
            Severity.MEDIUM: timedelta(days=30),
            Severity.LOW: timedelta(days=90)
        }
    
    def create_vulnerability(self, vuln_data: dict) -> str:
        vuln = Vulnerability(**vuln_data)
        self.vulnerabilities[vuln.id] = vuln
        
        # Send acknowledgment to reporter
        self.send_acknowledgment(vuln)
        
        # Set SLA deadline
        self.set_sla_deadline(vuln)
        
        return vuln.id
    
    def calculate_priority(self, vuln: Vulnerability) -> int:
        priority_score = 0
        
        # CVSS score weight
        priority_score += vuln.cvss_score * 10
        
        # Affected products weight
        priority_score += len(vuln.affected_products) * 5
        
        # Time factor (urgency increases over time)
        days_open = (datetime.now() - vuln.reported_date).days
        priority_score += days_open * 2
        
        return int(priority_score)
    
    def generate_security_advisory(self, vuln: Vulnerability) -> dict:
        return {
            'advisory_id': f"SA-{vuln.id}",
            'title': vuln.title,
            'severity': vuln.severity.value,
            'cvss_score': vuln.cvss_score,
            'affected_products': vuln.affected_products,
            'description': vuln.description,
            'mitigation_steps': self.get_mitigation_steps(vuln),
            'patch_availability': self.check_patch_status(vuln),
            'published_date': datetime.now().isoformat()
        }
```

#### Coordinated Disclosure Process
```yaml
# Example: Disclosure policy configuration
disclosure_policy:
  contact_information:
    security_email: "security@company.com"
    pgp_key: "https://company.com/security/pgp-key.asc"
    bug_bounty_platform: "hackerone.com/company"
    
  response_timeline:
    acknowledgment: "24 hours"
    initial_assessment: "5 business days"
    status_updates: "weekly"
    resolution_target:
      critical: "24 hours"
      high: "7 days"
      medium: "30 days"
      low: "90 days"
      
  disclosure_timeline:
    coordinated_disclosure: "90 days after fix"
    early_disclosure_conditions:
      - "active exploitation detected"
      - "vulnerability already public"
      - "vendor unresponsive beyond SLA"
      
  scope:
    in_scope:
      - "All company products and services"
      - "Corporate infrastructure accessible from internet"
      - "Mobile applications and web applications"
    out_of_scope:
      - "Social engineering attacks"
      - "Physical security issues"
      - "Denial of service attacks"
```

### Security Testing Framework

#### Automated Security Testing
```python
# Example: Automated security testing framework
import requests
import subprocess
from typing import List, Dict

class SecurityTestSuite:
    def __init__(self, target_url: str):
        self.target_url = target_url
        self.test_results = []
    
    def run_vulnerability_scan(self) -> Dict:
        results = {
            'sql_injection': self.test_sql_injection(),
            'xss': self.test_xss(),
            'authentication': self.test_authentication(),
            'authorization': self.test_authorization(),
            'ssl_tls': self.test_ssl_configuration()
        }
        return results
    
    def test_sql_injection(self) -> List[Dict]:
        payloads = ["'", "1' OR '1'='1", "'; DROP TABLE users; --"]
        findings = []
        
        for payload in payloads:
            try:
                response = requests.get(
                    f"{self.target_url}/search?q={payload}",
                    timeout=10
                )
                if "error" in response.text.lower() or "sql" in response.text.lower():
                    findings.append({
                        'type': 'sql_injection',
                        'payload': payload,
                        'response_code': response.status_code,
                        'evidence': response.text[:200]
                    })
            except Exception as e:
                continue
                
        return findings
    
    def test_ssl_configuration(self) -> Dict:
        try:
            result = subprocess.run([
                'testssl.sh', '--json', self.target_url
            ], capture_output=True, text=True)
            
            # Parse testssl.sh JSON output
            ssl_results = json.loads(result.stdout)
            return {
                'weak_ciphers': self.extract_weak_ciphers(ssl_results),
                'protocol_support': self.extract_protocol_support(ssl_results),
                'certificate_issues': self.extract_cert_issues(ssl_results)
            }
        except Exception as e:
            return {'error': str(e)}
```

## 🔄 Essential Requirement 4: Security Updates

### Automated Update System

#### Update Delivery Architecture
```python
# Example: Secure update delivery system
import hashlib
import json
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

class SecureUpdateManager:
    def __init__(self, private_key_path: str):
        with open(private_key_path, 'rb') as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(), password=None
            )
    
    def create_update_package(self, update_data: bytes, version: str) -> dict:
        # Calculate checksum
        checksum = hashlib.sha256(update_data).hexdigest()
        
        # Create update manifest
        manifest = {
            'version': version,
            'checksum': checksum,
            'size': len(update_data),
            'timestamp': datetime.now().isoformat(),
            'type': 'security_update'
        }
        
        # Sign the manifest
        manifest_bytes = json.dumps(manifest, sort_keys=True).encode()
        signature = self.private_key.sign(
            manifest_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return {
            'manifest': manifest,
            'signature': signature.hex(),
            'update_data': update_data
        }
    
    def verify_update_package(self, package: dict, public_key) -> bool:
        try:
            # Verify signature
            manifest_bytes = json.dumps(package['manifest'], sort_keys=True).encode()
            signature = bytes.fromhex(package['signature'])
            
            public_key.verify(
                signature,
                manifest_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            
            # Verify checksum
            actual_checksum = hashlib.sha256(package['update_data']).hexdigest()
            expected_checksum = package['manifest']['checksum']
            
            return actual_checksum == expected_checksum
            
        except Exception as e:
            return False
```

#### Update Client Implementation
```javascript
// Example: Client-side update manager
class UpdateClient {
    constructor(deviceId, publicKey) {
        this.deviceId = deviceId;
        this.publicKey = publicKey;
        this.updateEndpoint = 'https://updates.company.com/api/v1';
        this.currentVersion = this.getCurrentVersion();
    }
    
    async checkForUpdates() {
        try {
            const response = await fetch(`${this.updateEndpoint}/check`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    device_id: this.deviceId,
                    current_version: this.currentVersion,
                    device_type: this.getDeviceType()
                })
            });
            
            const updateInfo = await response.json();
            
            if (updateInfo.update_available) {
                return this.processUpdateInfo(updateInfo);
            }
            
            return null;
        } catch (error) {
            console.error('Update check failed:', error);
            return null;
        }
    }
    
    async downloadAndApplyUpdate(updateInfo) {
        try {
            // Download update package
            const updatePackage = await this.downloadUpdate(updateInfo.download_url);
            
            // Verify signature and integrity
            if (!this.verifyUpdatePackage(updatePackage)) {
                throw new Error('Update verification failed');
            }
            
            // Create backup before applying update
            await this.createBackup();
            
            // Apply update
            const success = await this.applyUpdate(updatePackage);
            
            if (success) {
                this.reportUpdateSuccess(updateInfo.version);
                return true;
            } else {
                await this.rollbackUpdate();
                return false;
            }
            
        } catch (error) {
            console.error('Update failed:', error);
            await this.rollbackUpdate();
            return false;
        }
    }
    
    verifyUpdatePackage(package) {
        // Implement signature verification using public key
        // Verify checksum
        // Check version compatibility
        return true; // Simplified for example
    }
}
```

## 🚨 Essential Requirement 5: Incident Response

### Incident Response Framework

#### Incident Detection and Classification
```python
# Example: Incident management system
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class IncidentType(Enum):
    SECURITY_BREACH = "security_breach"
    DATA_LEAK = "data_leak"
    MALWARE = "malware"
    UNAUTHORIZED_ACCESS = "unauthorized_access"
    VULNERABILITY_EXPLOITATION = "vulnerability_exploitation"
    SYSTEM_COMPROMISE = "system_compromise"

class Severity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class SecurityIncident:
    id: str
    type: IncidentType
    severity: Severity
    description: str
    affected_systems: list
    detected_at: datetime
    reporter: str
    status: str = "open"
    
class IncidentResponseManager:
    def __init__(self):
        self.incidents = {}
        self.response_procedures = {
            IncidentType.SECURITY_BREACH: self.handle_security_breach,
            IncidentType.DATA_LEAK: self.handle_data_leak,
            IncidentType.MALWARE: self.handle_malware,
        }
    
    def create_incident(self, incident_data: dict) -> str:
        incident = SecurityIncident(**incident_data)
        self.incidents[incident.id] = incident
        
        # Immediate response actions
        self.immediate_response(incident)
        
        # Trigger response procedure
        if incident.type in self.response_procedures:
            self.response_procedures[incident.type](incident)
        
        return incident.id
    
    def immediate_response(self, incident: SecurityIncident):
        # Log incident
        self.log_incident(incident)
        
        # Notify response team
        self.notify_response_team(incident)
        
        # Start containment if critical
        if incident.severity == Severity.CRITICAL:
            self.initiate_containment(incident)
    
    def handle_security_breach(self, incident: SecurityIncident):
        response_plan = [
            "Isolate affected systems",
            "Preserve evidence",
            "Assess scope of breach",
            "Notify stakeholders",
            "Begin recovery procedures"
        ]
        
        for step in response_plan:
            self.execute_response_step(incident.id, step)
    
    def generate_incident_report(self, incident_id: str) -> dict:
        incident = self.incidents[incident_id]
        
        return {
            'incident_id': incident.id,
            'type': incident.type.value,
            'severity': incident.severity.value,
            'timeline': self.get_incident_timeline(incident_id),
            'affected_systems': incident.affected_systems,
            'response_actions': self.get_response_actions(incident_id),
            'lessons_learned': self.get_lessons_learned(incident_id),
            'recommendations': self.get_recommendations(incident_id)
        }
```

#### Automated Incident Response
```yaml
# Example: Incident response automation
incident_response_automation:
  triggers:
    - name: "multiple_failed_logins"
      condition: "failed_login_count > 10 in 5 minutes"
      severity: "medium"
      actions:
        - "block_source_ip"
        - "notify_security_team"
        - "create_incident_ticket"
    
    - name: "malware_detected"
      condition: "antivirus_alert == 'malware_found'"
      severity: "high"
      actions:
        - "isolate_affected_system"
        - "preserve_forensic_evidence"
        - "escalate_to_incident_commander"
        - "notify_stakeholders"
    
    - name: "data_exfiltration"
      condition: "unusual_data_transfer > threshold"
      severity: "critical"
      actions:
        - "block_network_traffic"
        - "preserve_logs"
        - "activate_crisis_team"
        - "prepare_breach_notification"
  
  escalation_matrix:
    low:
      notify: ["security_analyst"]
      sla: "4 hours"
    medium:
      notify: ["security_analyst", "security_manager"]
      sla: "2 hours"
    high:
      notify: ["security_team", "management", "legal"]
      sla: "1 hour"
    critical:
      notify: ["all_stakeholders", "executive_team", "pr_team"]
      sla: "15 minutes"
```

## 📊 Monitoring and Metrics

### Security Metrics Dashboard
```python
# Example: Security metrics collection
class SecurityMetricsCollector:
    def __init__(self):
        self.metrics = {}
    
    def collect_vulnerability_metrics(self) -> dict:
        return {
            'total_vulnerabilities': self.count_vulnerabilities(),
            'critical_vulnerabilities': self.count_critical_vulnerabilities(),
            'mean_time_to_patch': self.calculate_mttr(),
            'vulnerability_density': self.calculate_vulnerability_density(),
            'disclosure_compliance': self.check_disclosure_compliance()
        }
    
    def collect_incident_metrics(self) -> dict:
        return {
            'incident_count': self.count_incidents(),
            'mean_time_to_detect': self.calculate_mttd(),
            'mean_time_to_respond': self.calculate_mttr_incidents(),
            'false_positive_rate': self.calculate_false_positive_rate(),
            'incident_recurrence': self.calculate_recurrence_rate()
        }
    
    def collect_compliance_metrics(self) -> dict:
        return {
            'control_implementation': self.assess_control_implementation(),
            'documentation_completeness': self.assess_documentation(),
            'training_completion': self.assess_training_status(),
            'audit_readiness': self.assess_audit_readiness()
        }
    
    def generate_dashboard(self) -> dict:
        return {
            'vulnerability_metrics': self.collect_vulnerability_metrics(),
            'incident_metrics': self.collect_incident_metrics(),
            'compliance_metrics': self.collect_compliance_metrics(),
            'trend_analysis': self.analyze_trends(),
            'risk_assessment': self.assess_current_risk()
        }
```

## 🎯 Implementation Checklist

### Security Controls Implementation
- [ ] Threat modeling process established
- [ ] Secure design principles documented and implemented
- [ ] Secure coding standards adopted
- [ ] Security testing integrated in CI/CD
- [ ] Default security configurations implemented
- [ ] Vulnerability disclosure program active
- [ ] Security update delivery system operational
- [ ] Incident response procedures tested
- [ ] Security monitoring and logging implemented
- [ ] Compliance metrics tracking established

### Documentation and Evidence
- [ ] Security architecture documentation complete
- [ ] Technical security controls documented
- [ ] Testing evidence collected and organized
- [ ] Incident response procedures documented
- [ ] Vulnerability management procedures documented
- [ ] Security training records maintained
- [ ] Compliance assessment evidence prepared
- [ ] Continuous monitoring procedures established

---

*For implementation support and questions, visit our [GitHub Discussions](https://github.com/seedon198/Cyber-Resilience-Act/discussions) or review our [Best Practices](Best-Practices) guide.*
"""

    def create_additional_pages(self):
        """Create additional specialized pages"""
        additional_pages = {
            'Implementation-Guide': self.get_implementation_guide_content(),
            'Technical-Implementation': self.get_technical_implementation_content(),
        }
        
        success_count = 0
        for page_name, content in additional_pages.items():
            if self.create_wiki_page(page_name, content):
                success_count += 1
        
        return success_count == len(additional_pages)

def main():
    """Main execution"""
    try:
        creator = WikiContentCreator()
        success = creator.create_additional_pages()
        
        if success:
            print("\n✅ Additional wiki pages created successfully!")
        else:
            print("\n❌ Some additional wiki pages failed to create")
            
    except Exception as e:
        print(f"❌ Error creating additional wiki pages: {e}")

if __name__ == "__main__":
    main()
