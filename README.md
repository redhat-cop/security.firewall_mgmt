security.firewall_mgmt 
======================

Role to manage and automate Firewall policies and management.

Example Playbook
----------------

Below example TCs of running the Role at Cisco ASA Firewall:

    - hosts: asa
      gather_facts: false
      roles:
         - firewall_policy_automation

License
-------

BSD

Author Information
------------------

Ansible Security Automation Team (@justjais) <https://github.com/ansible-security>.
