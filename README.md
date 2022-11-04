# Ansible Security Firewall Management Collection

This repository contains the `security.firewall_mgmt` Ansible Collection.

## Description
An Ansible Collection to build, maintain and validate Firewall management and policies across security providers firewall appliances. See Supported Providers section for more details.

## Example Playbook

Below example TCs of running the Role at Cisco ASA Firewall:

    - hosts: asa
      gather_facts: false
      roles:
         - security.firewall_mgmt.run

## Supported providers

| **Provider**           |
|------------------------|
| Cisco ASA              |

## Requirements
This following collections should be installed:
- ansible.netcommon
- cisco.asa

### Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Release notes

Release notes are available [here](https://github.com/redhat-cop/security.firewall_mgmt/blob/main/CHANGELOG.rst).

## Author Information

Ansible Security Automation Team (@justjais) <https://github.com/ansible-security>.

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
