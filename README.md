zsh
=========

Installes zsh and enabled drop-in configuration.

Requirements
------------

None.

Role Variables
--------------

| Variable name | Default value | Description
|---------------|---------------|-------------
`zsh_user` | `"{{ ansible_user_id }}"` | User for which to configure zsh
`zsh_host_color` | "red" | Host color in the command prompt

Dependencies
------------

None.

Example Playbook
----------------

See `molecule/default/playbook.yml`.

License
-------

BSD

Author Information
------------------

Find me on [GitHub](https://github.com/ThreeFx).
