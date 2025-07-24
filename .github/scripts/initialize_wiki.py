#!/usr/bin/env python3
"""
Initialize GitHub Wiki with comprehensive CRA content
Creates all necessary wiki pages for the EU Cyber Resilience Act compliance hub
"""

import requests
import json
import os
from datetime import datetime

class WikiInitializer:
    def __init__(self):
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.repo_owner = 'seedon198'
        self.repo_name = 'Cyber-Resilience-Act'
        
        if not self.github_token:
            raise ValueError("GITHUB_TOKEN environment variable required")
    
    def create_wiki_page(self, page_name, content, message=None):
        """Create or update a wiki page using git operations"""
        if not self.github_token:
            print("❌ No GitHub token provided")
            return False
            
        import subprocess
        import tempfile
        
        with tempfile.TemporaryDirectory() as temp_dir:
            wiki_repo = f"https://x-access-token:{self.github_token}@github.com/{self.repo_owner}/{self.repo_name}.wiki.git"
            
            try:
                # Clone wiki repo
                result = subprocess.run(['git', 'clone', wiki_repo, temp_dir], 
                                     check=True, capture_output=True, text=True)
                
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
                commit_message = message or f"Add {page_name} wiki page"
                subprocess.run(['git', 'commit', '-m', commit_message], 
                             cwd=temp_dir, check=True)
                
                # Push changes
                subprocess.run(['git', 'push'], cwd=temp_dir, check=True)
                
                print(f"Successfully created/updated wiki page: {page_name}")
                return True
                
            except subprocess.CalledProcessError as e:
                print(f"Error updating wiki page {page_name}: {e}")
                if e.stderr:
                    print(f"   Error details: {e.stderr}")
                return False
    
    def _create_wiki_bootstrap_file(self, page_name, content):
        """Create a temporary file that can be used to bootstrap wiki"""
        import tempfile
        import os
        
        # Create a temporary directory for wiki content
        wiki_dir = "wiki-content"
        if not os.path.exists(wiki_dir):
            os.makedirs(wiki_dir)
        
        # Write the content to a file
        with open(f"{wiki_dir}/{page_name}.md", 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created bootstrap file for {page_name}")
        
        # Also try to create the page via GitHub Issues API as a workaround
        self._create_wiki_via_issues(page_name, content)
    
    def _create_wiki_via_issues(self, page_name, content):
        """Alternative method to document wiki content"""
        try:
            # Create a documentation issue with the wiki content
            issue_title = f"Wiki Content: {page_name.replace('-', ' ')}"
            issue_body = f"""# Wiki Page Content: {page_name}

This issue contains the content for the `{page_name}` wiki page. 

**Note**: This content should be manually copied to the GitHub Wiki at: https://github.com/{self.repo_owner}/{self.repo_name}/wiki/{page_name}

## Content:

{content}

---
*This issue was auto-generated to bootstrap wiki content. Once the wiki page is created, this issue can be closed.*
"""
            
            api_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/issues"
            headers = {
                'Authorization': f'token {self.github_token}',
                'Accept': 'application/vnd.github.v3+json',
                'Content-Type': 'application/json'
            }
            
            issue_data = {
                'title': issue_title,
                'body': issue_body,
                'labels': ['documentation', 'wiki-content', 'auto-generated']
            }
            
            response = requests.post(api_url, headers=headers, json=issue_data)
            if response.status_code == 201:
                issue_url = response.json().get('html_url')
                print(f"Created documentation issue for {page_name}: {issue_url}")
            else:
                print(f"Could not create issue for {page_name}: {response.status_code}")
                
        except Exception as e:
            print(f"Could not create documentation issue for {page_name}: {e}")

    def get_home_content(self):
        """Generate Home page content"""
        return f"""# EU Cyber Resilience Act (CRA) Compliance Hub

Welcome to the comprehensive wiki for EU Cyber Resilience Act compliance. This wiki provides practical guidance, tools, and resources for organizations preparing for CRA requirements.

## Quick Start Guide

### New to CRA?
1. **[What is the CRA?](CRA-Overview)** - Understanding the regulation
2. **[Timeline & Deadlines](Timeline-and-Milestones)** - Key implementation dates
3. **[Getting Started](Getting-Started)** - Your first steps toward compliance

### Ready to Implement?
1. **[Compliance Assessment](Compliance-Assessment)** - Evaluate your current state
2. **[Implementation Guide](Implementation-Guide)** - Step-by-step compliance process
3. **[Tools & Resources](Tools-and-Resources)** - Practical implementation tools

### Specialized Areas
- **[Hardware Security](Hardware-Security)** - Embedded systems and IoT compliance
- **[Industrial Systems](Industrial-Control-Systems)** - OT/ICS security requirements
- **[Penetration Testing](Penetration-Testing)** - Security assessment frameworks

## Latest Updates

**[Latest News & Developments](Latest-News)** - Auto-updated daily with CRA news

## Documentation Library

| Topic | Description | Target Audience |
|-------|-------------|-----------------|
| [CRA Overview](CRA-Overview) | Regulation fundamentals | All stakeholders |
| [Legal Requirements](Legal-Requirements) | Detailed legal analysis | Legal & compliance teams |
| [Technical Standards](Technical-Standards) | Harmonized standards reference | Technical teams |
| [Risk Assessment](Risk-Assessment) | Risk management frameworks | Risk managers |
| [Conformity Assessment](Conformity-Assessment) | Third-party evaluation process | Compliance officers |
| [Market Surveillance](Market-Surveillance) | Enforcement mechanisms | Product managers |

## By Industry & Role

### By Industry
- **[IoT & Consumer Electronics](IoT-and-Consumer-Electronics)**
- **[Industrial Equipment](Industrial-Equipment)**  
- **[Software & Services](Software-and-Services)**
- **[Automotive Systems](Automotive-Systems)**
- **[Medical Devices](Medical-Devices)**

### By Role
- **[Management Overview](Management-Overview)**
- **[Legal & Compliance](Legal-and-Compliance)**
- **[Technical Implementation](Technical-Implementation)**
- **[Security Professionals](Security-Professionals)**
- **[Testing & Validation](Testing-and-Validation)**

## Practical Tools

- **[Compliance Checklists](Compliance-Checklists)** - Ready-to-use assessment tools
- **[Gap Analysis Templates](Gap-Analysis-Templates)** - Identify compliance gaps
- **[Document Templates](Document-Templates)** - Pre-formatted compliance docs
- **[Testing Frameworks](Testing-Frameworks)** - Security assessment methodologies

## Training & Education

- **[Training Programs](Training-Programs)** - Structured learning paths
- **[Best Practices](Best-Practices)** - Industry-proven approaches
- **[Case Studies](Case-Studies)** - Real-world implementation examples
- **[FAQ](Frequently-Asked-Questions)** - Common questions answered

## Community & Support

- **[Discussions](https://github.com/seedon198/Cyber-Resilience-Act/discussions)** - Community Q&A
- **[Issues](https://github.com/seedon198/Cyber-Resilience-Act/issues)** - Report problems or request features
- **[🤝 Contributing](Contributing-Guidelines)** - How to contribute to this resource

## 🔄 About This Wiki

- **🤖 Automated Updates**: Key pages updated daily with latest developments
- **📊 Living Documentation**: Continuously updated with new guidance and standards
- **🌍 Community-Driven**: Contributions welcome from compliance professionals
- **✅ Authoritative Sources**: All content verified against official EU documentation

---

*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')} | Maintained by the CRA Compliance Community*

> **⚖️ Legal Disclaimer**: This wiki provides general guidance and should not be considered legal advice. Always consult with qualified legal professionals for specific compliance requirements.
"""

    def get_cra_overview_content(self):
        """Generate CRA Overview page content"""
        return """# CRA Overview - Understanding the Cyber Resilience Act

## What is the Cyber Resilience Act?

The **EU Cyber Resilience Act (CRA)** is landmark European legislation designed to establish mandatory cybersecurity requirements for digital products throughout their lifecycle. It represents the EU's most comprehensive approach to cybersecurity regulation for connected products.

## Key Objectives

### Primary Goals
- **Harmonize cybersecurity requirements** across the EU single market
- **Enhance cybersecurity** of digital products and services
- **Create legal certainty** for manufacturers and users
- **Improve incident response** and vulnerability management
- **Strengthen market surveillance** and enforcement

### Scope of Application

#### Products Covered
- **Consumer IoT devices** (smart home, wearables, connected appliances)
- **Industrial IoT systems** and operational technology
- **Software products** with digital elements
- **Network equipment** and telecommunications devices
- **Cybersecurity products** and services

#### Exemptions
- Products already covered by specific EU legislation
- Open-source software (with conditions)
- Products for research and development only
- Custom products for a single customer

## Regulatory Framework

### Essential Requirements
All covered products must meet:

1. **Secure by Design**: Built-in security from conception
2. **Secure by Default**: Safe default configurations
3. **Vulnerability Management**: Coordinated disclosure and patching
4. **Incident Response**: Prompt notification and remediation
5. **Documentation**: Comprehensive security documentation

### Product Classification

#### Class I (Standard Risk)
- Basic cybersecurity requirements
- Self-assessment allowed
- CE marking required

#### Class II (Important Risk)  
- Enhanced security requirements
- Third-party assessment required
- Additional documentation

### Legal Obligations

#### For Manufacturers
- Implement essential cybersecurity requirements
- Conduct conformity assessments
- Maintain technical documentation
- Report cybersecurity incidents
- Provide security updates

#### For Importers & Distributors
- Ensure manufacturer compliance
- Verify CE marking and documentation
- Report non-compliant products
- Cooperate with market surveillance

#### For Users
- Apply security updates promptly
- Report cybersecurity incidents (for important products)
- Use products according to instructions

## Implementation Timeline

### Key Dates
- **2024**: Regulation enters into force
- **2027**: Full application begins
- **2028**: Enhanced requirements for Class II products

### Transition Periods
- **36 months**: General implementation period
- **42 months**: Class II product requirements
- **Legacy products**: Grandfathering provisions apply

## Enforcement Mechanisms

### Market Surveillance
- **National authorities** monitor compliance
- **Product testing** and documentation review
- **Non-compliance penalties** up to 2.5% of global turnover
- **Product withdrawal** from market possible

### Conformity Assessment
- **Self-assessment** for Class I products
- **Third-party assessment** for Class II products
- **Notified bodies** conduct evaluations
- **CE marking** indicates compliance

## Benefits of Compliance

### For Organizations
- **Market access** across the EU
- **Competitive advantage** through security
- **Reduced cyber risks** and incidents
- **Customer trust** and confidence
- **Legal protection** and certainty

### For Users
- **Enhanced security** of digital products
- **Transparency** about cybersecurity features
- **Coordinated vulnerability** management
- **Incident response** and support
- **Long-term security** updates

## Getting Started

### Immediate Actions
1. **[Assess applicability](Compliance-Assessment)** to your products
2. **[Review requirements](Legal-Requirements)** for your product category
3. **[Identify gaps](Gap-Analysis-Templates)** in current security practices
4. **[Develop implementation plan](Implementation-Guide)** with timelines
5. **[Engage stakeholders](Management-Overview)** across the organization

### Next Steps
- **[Technical Implementation](Technical-Implementation)** - Security controls and processes
- **[Documentation](Document-Templates)** - Required technical files and declarations
- **[Testing & Validation](Testing-Frameworks)** - Security assessment and verification
- **[Conformity Assessment](Conformity-Assessment)** - Formal compliance evaluation

---

*For detailed legal analysis, see [Legal Requirements](Legal-Requirements). For technical implementation guidance, visit [Technical Implementation](Technical-Implementation).*
"""

    def get_getting_started_content(self):
        """Generate Getting Started page content"""
        return """# Getting Started with CRA Compliance

This guide provides a structured approach to beginning your CRA compliance journey, regardless of your organization size or current security maturity.

## Step 1: Determine Applicability

### Quick Assessment
Answer these questions to determine if CRA applies to your products:

#### Product Characteristics
- [ ] Does your product have digital elements?
- [ ] Is it connected to networks or other devices?
- [ ] Do you place it on the EU market?
- [ ] Is it intended for commercial use?

#### Exemption Check
- [ ] Is your product already covered by specific EU cybersecurity legislation?
- [ ] Is it open-source software developed outside commercial activity?
- [ ] Is it for R&D purposes only?
- [ ] Is it a custom product for a single customer?

**If you answered "Yes" to product characteristics and "No" to exemptions, CRA likely applies.**

### Product Classification

#### Class I Products (Standard Risk)
- Most consumer IoT devices
- Basic software products
- Standard network equipment
- Simple connected devices

#### Class II Products (Important Risk)
- Critical infrastructure components
- Identity management systems
- Advanced cybersecurity products
- High-risk network equipment

**📋 [Use our detailed assessment tool](Compliance-Assessment) for definitive classification.**

## Step 2: Current State Analysis

### Security Inventory
Document your current security posture:

#### Technical Assessment
1. **Security Controls**
   - Authentication mechanisms
   - Data encryption practices
   - Access control systems
   - Vulnerability management processes

2. **Development Practices**
   - Secure coding standards
   - Security testing procedures
   - Code review processes
   - Third-party component management

3. **Operational Security**
   - Incident response procedures
   - Security monitoring capabilities
   - Update and patch management
   - Security documentation

#### Gap Analysis
- **[Download our gap analysis template](Gap-Analysis-Templates)**
- Compare current practices with CRA requirements
- Prioritize gaps by risk and implementation effort
- Estimate resources needed for remediation

## Step 3: Compliance Planning

### Implementation Roadmap

#### Phase 1: Foundation (Months 1-3)
- [ ] Establish CRA compliance team
- [ ] Complete detailed applicability assessment
- [ ] Conduct comprehensive gap analysis
- [ ] Develop implementation budget and timeline
- [ ] Engage management support and resources

#### Phase 2: Essential Requirements (Months 4-12)
- [ ] Implement secure by design practices
- [ ] Establish vulnerability management program
- [ ] Create incident response procedures
- [ ] Develop security documentation framework
- [ ] Begin conformity assessment preparation

#### Phase 3: Documentation & Assessment (Months 13-18)
- [ ] Complete technical documentation
- [ ] Prepare EU declaration of conformity
- [ ] Engage notified body (if Class II)
- [ ] Conduct final security testing
- [ ] Implement CE marking process

#### Phase 4: Market Readiness (Months 19-24)
- [ ] Finalize all compliance documentation
- [ ] Train support and sales teams
- [ ] Establish ongoing compliance monitoring
- [ ] Prepare for market surveillance
- [ ] Launch compliant products

### Resource Planning

#### Team Structure
- **Compliance Manager**: Overall program coordination
- **Legal Counsel**: Regulatory interpretation and risk
- **Security Architect**: Technical implementation
- **Product Manager**: Product integration and timeline
- **Quality Assurance**: Testing and documentation
- **External Consultant**: Specialized expertise (optional)

#### Budget Considerations
- **Internal resources**: Staff time and training
- **External services**: Legal, consulting, assessment
- **Technology investments**: Security tools and systems
- **Compliance costs**: Notified body fees, testing
- **Ongoing costs**: Monitoring, updates, maintenance

## Step 4: Quick Wins & Early Actions

### Immediate Improvements (30 days)
1. **Security Defaults**
   - Review and strengthen default configurations
   - Disable unnecessary services and features
   - Implement secure authentication requirements

2. **Vulnerability Management**
   - Establish vulnerability disclosure policy
   - Set up security contact information
   - Begin tracking and documenting vulnerabilities

3. **Documentation**
   - Start security documentation repository
   - Document current security features
   - Create compliance tracking system

### Short-term Goals (90 days)
1. **Secure Development**
   - Implement security code review process
   - Establish security testing procedures
   - Train development team on secure coding

2. **Incident Response**
   - Create basic incident response plan
   - Establish incident reporting procedures
   - Set up security monitoring alerts

3. **Supply Chain Security**
   - Inventory third-party components
   - Assess supplier security practices
   - Implement component vulnerability tracking

## Essential Resources

### Documentation Templates
- **[Compliance Checklist](Compliance-Checklists)** - Track your progress
- **[Gap Analysis Worksheet](Gap-Analysis-Templates)** - Identify requirements gaps
- **[Implementation Plan Template](Document-Templates)** - Structure your approach

### Technical Guidance
- **[Hardware Security Guide](Hardware-Security)** - Embedded systems compliance
- **[Software Security Standards](Technical-Standards)** - Development requirements
- **[Testing Frameworks](Testing-Frameworks)** - Security assessment methods

### Industry-Specific Guidance
- **[IoT Devices](IoT-and-Consumer-Electronics)** - Consumer product requirements
- **[Industrial Systems](Industrial-Control-Systems)** - OT/ICS compliance
- **[Software Products](Software-and-Services)** - Application security requirements

## Training & Education

### Team Training Priorities
1. **Management**: CRA overview and business impact
2. **Legal**: Regulatory requirements and obligations
3. **Technical**: Security implementation and testing
4. **Quality**: Documentation and assessment procedures
5. **Sales/Marketing**: Customer communication and positioning

### External Training Options
- **[CRA Training Programs](Training-Programs)** - Structured learning paths
- Industry conferences and workshops
- Professional certification programs
- Vendor-specific security training

## 📞 Getting Help

### Internal Resources
- Establish clear escalation paths
- Create cross-functional working groups
- Regular progress reviews and updates

### External Support
- **Legal counsel** for regulatory interpretation
- **Security consultants** for technical implementation
- **Notified bodies** for conformity assessment
- **Industry associations** for peer guidance

### Community Resources
- **[GitHub Discussions](https://github.com/seedon198/Cyber-Resilience-Act/discussions)** - Ask questions and share experiences
- **[Latest News](Latest-News)** - Stay informed of regulatory updates
- **[Best Practices](Best-Practices)** - Learn from implementation experiences

## Success Metrics

### Track Your Progress
- **Compliance readiness** percentage
- **Security control** implementation status
- **Documentation** completion rate
- **Team training** completion
- **Budget and timeline** adherence

### Key Milestones
- [ ] Applicability determination complete
- [ ] Gap analysis finalized
- [ ] Implementation plan approved
- [ ] Essential requirements implemented
- [ ] Documentation package complete
- [ ] Conformity assessment passed
- [ ] Market launch ready

---

*Ready for the next step? Choose your path based on your primary focus:*
- **Technical Implementation** → [Technical Implementation Guide](Technical-Implementation)
- **Legal Compliance** → [Legal Requirements](Legal-Requirements)
- **Management Planning** → [Management Overview](Management-Overview)
- **Industry-Specific** → Select your industry from the [Home page](Home)
"""

    def get_compliance_assessment_content(self):
        """Generate Compliance Assessment page content"""
        return """# Compliance Assessment - Evaluate Your CRA Readiness

This comprehensive assessment helps you determine your current compliance status and identify specific actions needed for CRA conformity.

## Assessment Overview

### Purpose
- Evaluate current security posture against CRA requirements
- Identify specific compliance gaps and priorities
- Generate actionable improvement roadmap
- Estimate implementation effort and resources

### Assessment Scope
- Technical security controls and capabilities
- Documentation and process maturity
- Organizational readiness and governance
- Product-specific requirements and classifications

## Quick Assessment Tool

### Part A: Product Applicability

#### A1. Product Characteristics
Rate each statement (0=No, 1=Partially, 2=Yes):

- [ ] Our product contains digital elements or software
- [ ] Our product connects to networks or other devices  
- [ ] Our product is intended for the EU market
- [ ] Our product processes, stores, or transmits data
- [ ] Our product has remote management capabilities

**Score: ___/10**

#### A2. Risk Classification
Check all that apply:

**Class I Indicators:**
- [ ] Consumer IoT device (smart home, wearables)
- [ ] Basic software application
- [ ] Standard network equipment
- [ ] Low-complexity connected device

**Class II Indicators:**
- [ ] Critical infrastructure component
- [ ] Identity/access management system
- [ ] Cybersecurity product or service
- [ ] High-risk network infrastructure
- [ ] Root certificate authority
- [ ] Microprocessor with security features

**Preliminary Classification: ________________**

### Part B: Technical Security Controls

#### B1. Secure by Design (Essential Requirement 1)
Rate your implementation (0=None, 1=Basic, 2=Comprehensive):

- [ ] Security considered from initial design phase
- [ ] Threat modeling conducted for products
- [ ] Security architecture documentation maintained
- [ ] Security requirements integrated in development lifecycle
- [ ] Regular security design reviews conducted

**Score: ___/10**

#### B2. Secure by Default (Essential Requirement 2)
Rate your implementation:

- [ ] Products shipped with secure default configurations
- [ ] Unnecessary services disabled by default
- [ ] Strong authentication required by default
- [ ] Security features enabled without user action
- [ ] Default credentials eliminated or forced change

**Score: ___/10**

#### B3. Vulnerability Management (Essential Requirement 3)
Rate your implementation:

- [ ] Vulnerability disclosure policy published
- [ ] Security contact information publicly available
- [ ] Vulnerability tracking and management system
- [ ] Coordinated disclosure process established
- [ ] Security update delivery mechanism

**Score: ___/10**

#### B4. Security Update Management (Essential Requirement 4)
Rate your implementation:

- [ ] Automated security update mechanism
- [ ] Update integrity protection (signing/verification)
- [ ] Rollback capability for failed updates
- [ ] Clear update notification to users
- [ ] End-of-support lifecycle policy

**Score: ___/10**

#### B5. Incident Response (Essential Requirement 5)
Rate your implementation:

- [ ] Cybersecurity incident response plan
- [ ] Incident detection and monitoring capabilities
- [ ] Stakeholder notification procedures
- [ ] Incident documentation and tracking
- [ ] Post-incident analysis and improvement

**Score: ___/10**

### Part C: Documentation & Processes

#### C1. Technical Documentation
Rate completeness and quality:

- [ ] Comprehensive security documentation
- [ ] Risk assessment documentation
- [ ] Security control implementation details
- [ ] Testing and validation evidence
- [ ] Conformity assessment preparation

**Score: ___/10**

#### C2. Quality Management System
Rate your system maturity:

- [ ] Documented quality management procedures
- [ ] Security integration in QMS
- [ ] Regular management reviews of security
- [ ] Continuous improvement processes
- [ ] Supplier security requirements

**Score: ___/10**

#### C3. Conformity Assessment Readiness
Rate your preparation:

- [ ] Understanding of applicable standards
- [ ] Technical file preparation
- [ ] EU declaration of conformity readiness
- [ ] Notified body engagement (if Class II)
- [ ] CE marking process understanding

**Score: ___/10**

## Detailed Assessment Questionnaire

### Section 1: Essential Requirements Deep Dive

#### 1.1 Security by Design Implementation

**Product Design Phase:**
1. Do you conduct threat modeling for each product?
2. Are security requirements defined before development begins?
3. Do you follow established secure design principles?
4. Is security architecture reviewed and approved?
5. Are security controls designed to be resilient against known attack vectors?

**Development Integration:**
1. Is security integrated throughout the development lifecycle?
2. Do you use secure coding standards and guidelines?
3. Are security controls tested during development?
4. Do you conduct security code reviews?
5. Are third-party components assessed for security?

#### 1.2 Default Security Configuration

**Configuration Management:**
1. Are all products shipped with secure default settings?
2. Do you eliminate or require changing default credentials?
3. Are unnecessary services and features disabled by default?
4. Is network access restricted to essential functionality?
5. Are security features enabled without requiring user configuration?

**User Experience:**
1. Can users easily understand and manage security settings?
2. Do you provide clear security configuration guidance?
3. Are security warnings and notifications user-friendly?
4. Do you balance security with usability appropriately?
5. Is the security posture maintained across product updates?

#### 1.3 Vulnerability Management Program

**Disclosure and Communication:**
1. Do you have a published vulnerability disclosure policy?
2. Is security contact information easily accessible?
3. Do you acknowledge receipt of vulnerability reports?
4. Are disclosure timelines clearly communicated?
5. Do you coordinate with reporters and other stakeholders?

**Assessment and Remediation:**
1. Do you have a process for assessing vulnerability severity?
2. Are vulnerabilities tracked and prioritized systematically?
3. Do you develop and test security patches promptly?
4. Are workarounds provided when patches aren't immediately available?
5. Do you validate that fixes don't introduce new vulnerabilities?

### Section 2: Organizational Capability Assessment

#### 2.1 Governance and Management

**Leadership and Strategy:**
1. Is cybersecurity governance clearly defined and communicated?
2. Are cybersecurity roles and responsibilities assigned?
3. Do senior leaders actively support cybersecurity initiatives?
4. Is cybersecurity integrated into business strategy?
5. Are cybersecurity metrics regularly reviewed by management?

**Resource Allocation:**
1. Are adequate resources allocated to cybersecurity?
2. Is cybersecurity expertise available in-house or through partners?
3. Are cybersecurity tools and technologies appropriately funded?
4. Is ongoing security training provided to relevant staff?
5. Are external cybersecurity services engaged when needed?

#### 2.2 Operational Capabilities

**Incident Response:**
1. Do you have a documented incident response plan?
2. Are response team roles and responsibilities clearly defined?
3. Do you conduct regular incident response exercises?
4. Are incident communications procedures established?
5. Do you conduct post-incident analysis and improvement?

**Monitoring and Detection:**
1. Do you have security monitoring capabilities for your products?
2. Can you detect cybersecurity incidents affecting products?
3. Are security events logged and analyzed?
4. Do you have threat intelligence capabilities?
5. Can you assess the impact of security incidents?

## Scoring and Interpretation

### Overall Readiness Score

**Calculate your total score:**
- Technical Controls (Part B): ___/50 points
- Documentation & Processes (Part C): ___/30 points
- Detailed Assessment: ___/100 points (if completed)

**Total Score: ___/180 points**

### Readiness Levels

#### Level 1: Beginning (0-60 points)
**Status:** Significant work needed
**Priority Actions:**
- Complete product applicability assessment
- Begin essential requirements implementation
- Establish basic security documentation
- Engage management support and resources

#### Level 2: Developing (61-120 points)
**Status:** Good foundation, gaps remain
**Priority Actions:**
- Address specific technical control gaps
- Complete documentation requirements
- Prepare for conformity assessment
- Enhance monitoring and response capabilities

#### Level 3: Advanced (121-180 points)
**Status:** Strong compliance readiness
**Priority Actions:**
- Finalize remaining documentation
- Complete conformity assessment process
- Implement continuous improvement
- Prepare for market surveillance

### Gap Analysis Results

**High Priority Gaps** (Score 0-1):
- Essential requirements with low scores
- Critical technical controls missing
- Documentation significantly incomplete

**Medium Priority Gaps** (Score 1):
- Partially implemented controls
- Documentation needs improvement
- Process maturity opportunities

**Low Priority Gaps** (Score 2):
- Minor enhancements needed
- Documentation updates required
- Process optimization opportunities

## Next Steps Based on Results

### For Beginning Level Organizations
1. **[Start with Getting Started Guide](Getting-Started)**
2. Focus on essential requirements implementation
3. Establish basic documentation framework
4. Consider external consulting support

### For Developing Level Organizations
1. **[Technical Implementation Guide](Technical-Implementation)**
2. Complete gap remediation plan
3. Prepare conformity assessment package
4. Enhance security monitoring capabilities

### For Advanced Level Organizations
1. **[Conformity Assessment Process](Conformity-Assessment)**
2. Finalize technical documentation
3. Engage notified body (if Class II)
4. Prepare for product launch

## Assessment Tools & Templates

### Downloadable Resources
- **[Detailed Assessment Spreadsheet](Document-Templates)** - Comprehensive scoring tool
- **[Gap Analysis Template](Gap-Analysis-Templates)** - Structured gap identification
- **[Compliance Checklist](Compliance-Checklists)** - Progress tracking tool
- **[Risk Assessment Template](Risk-Assessment)** - Product risk evaluation

### Industry-Specific Assessments
- **[IoT Device Assessment](IoT-and-Consumer-Electronics)** - Consumer product focus
- **[Industrial System Assessment](Industrial-Control-Systems)** - OT/ICS requirements
- **[Software Product Assessment](Software-and-Services)** - Application security focus

---

*Need help interpreting your results? Visit our [Community Discussions](https://github.com/seedon198/Cyber-Resilience-Act/discussions) or consult the [FAQ](Frequently-Asked-Questions).*
"""

    def initialize_all_pages(self):
        """Initialize all wiki pages"""
        pages = {
            'Home': self.get_home_content(),
            'CRA-Overview': self.get_cra_overview_content(),
            'Getting-Started': self.get_getting_started_content(),
            'Compliance-Assessment': self.get_compliance_assessment_content(),
        }
        
        success_count = 0
        for page_name, content in pages.items():
            if self.create_wiki_page(page_name, content):
                success_count += 1
        
        print(f"\nSuccessfully initialized {success_count}/{len(pages)} wiki pages!")
        return success_count == len(pages)

def main():
    """Main execution"""
    try:
        initializer = WikiInitializer()
        success = initializer.initialize_all_pages()
        
        if success:
            print("\nWiki initialization completed successfully!")
            print("Visit: https://github.com/seedon198/Cyber-Resilience-Act/wiki")
        else:
            print("\nSome wiki pages failed to initialize")
            exit(1)
            
    except Exception as e:
        print(f"Error initializing wiki: {e}")
        exit(1)

if __name__ == "__main__":
    main()
