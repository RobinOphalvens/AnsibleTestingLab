"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def check_httpd_service(host):
    """Check that the httpd service is running on the host"""
    assert host.service("httpd").is_running