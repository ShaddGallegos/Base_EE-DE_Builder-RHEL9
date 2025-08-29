# Base EE-DE Builder RHEL9

**Created:** September 2024

## Synopsis

A Red Hat Enterprise Linux 9 specific version of the Execution Environment and Decision Engine builder for Ansible Automation Platform. Optimized for RHEL9 systems with enhanced security and enterprise features.

## Supported Operating Systems

- Red Hat Enterprise Linux 9.x
- CentOS Stream 9
- Rocky Linux 9
- AlmaLinux 9

## Quick Usage

### Basic Setup and Execution

```bash
# Run the RHEL9-specific setup script
./EE-DE_Builder_WebUI_Install_and_Setup.sh

# Build environments using Ansible
ansible-playbook build_environments.yml

# Configure environment settings for RHEL9
ansible-playbook env_conf.yml

# Start the web interface
make run-frontend

# Run all build processes
make all
```

### RHEL9-Specific Configuration

```bash
# Test RHEL9-specific structure
./test_structure.sh

# Use RHEL9-optimized Makefile targets
make rhel9-install   # RHEL9-specific installation
make rhel9-build     # RHEL9-optimized builds
make rhel9-deploy    # RHEL9 deployment
```

### Web Interface Access

After setup, access the RHEL9-optimized web interface at:
- Local: http://localhost:3000
- Network: http://your-rhel9-server-ip:3000

## Features and Capabilities

### RHEL9-Specific Features

- Enhanced security with SELinux integration
- RHEL9 container runtime optimization
- Red Hat Universal Base Images (UBI) support
- Enterprise-grade logging and monitoring
- FIPS compliance support
- Advanced networking with Podman 4.x

### Core Features

- Web-based user interface optimized for RHEL9
- Automated RHEL9 system preparation
- Enterprise container image building
- Advanced security configurations
- Performance optimizations for RHEL9
- Integration with Red Hat Insights

### Build System Features

- RHEL9-optimized Makefile automation
- Enterprise React/TypeScript frontend
- Secure backend API services
- RHEL9 container orchestration
- Enterprise configuration management
- Desktop integration with GNOME

### Enterprise Integration

- Red Hat Subscription Manager integration
- Red Hat Container Registry access
- Ansible Automation Platform 2.x support
- Red Hat Insights integration
- Enterprise authentication systems
- Advanced monitoring and alerting

## Limitations

- Requires Red Hat Enterprise Linux 9.x
- Requires valid Red Hat subscription for enterprise features
- Network connectivity needed for Red Hat services
- Requires sufficient system resources for enterprise workloads
- Some features require specific RHEL9 package versions
- Enterprise features may require additional licensing

## Getting Help

### Documentation

- Check RHEL9-specific configuration in templates/
- Review enterprise feature documentation
- Examine Red Hat specific integration guides
- Check system logs for RHEL9-specific issues

### Support Resources

- Red Hat Customer Portal for enterprise support
- Red Hat Knowledgebase for RHEL9 issues
- Use built-in enterprise help system
- Check Red Hat Insights for system recommendations

### Enterprise Support

- Red Hat Support Portal: https://access.redhat.com
- Red Hat Customer Success for enterprise guidance
- Red Hat Consulting for implementation assistance
- Red Hat Training for skill development

### Common Issues

- Subscription registration: Ensure system is properly registered
- Container registry access: Verify Red Hat registry credentials
- SELinux contexts: Check SELinux policies and contexts
- FIPS mode: Verify FIPS compliance requirements
- Network security: Check enterprise firewall configurations
- Resource allocation: Monitor enterprise workload requirements

## Legal Disclaimer

This software is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

Use this software at your own risk. No warranty is implied or provided.

**By Shadd**
