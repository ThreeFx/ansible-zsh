import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_files_exist(host):
    fps = ['.zshrc', '.zshrc.d', '.zprofile', '.zprofile.d']
    homes = ['/root']  # , '/home/testuser']
    fs = map(lambda f: host.file(f), [h + '/' + f for h in homes for f in fps])

    for f in fs:
        assert f.exists
