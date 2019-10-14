import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_zshrc(host):
    fps = ['.zshrc', '.zshrc.d']
    fs = map(lambda f: host.file('/root/' + f), fps)

    for f in fs:
        assert f.exists


def test_zprofile(host):
    fps = ['.zprofile', '.zprofile.d']
    fs = map(lambda f: host.file('/root/' + f), fps)

    for f in fs:
        assert f.exists
