import semver
def test_semver_parses():
    semver.Version.parse('2.3.1')
