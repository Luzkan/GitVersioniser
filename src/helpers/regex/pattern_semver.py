from re import match


def regex_pattern_semver(tag_semver: str):
    """ https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string """
    major = r"(?P<major>0|[1-9]\d*)"
    minor = r"(?P<minor>0|[1-9]\d*)"
    patch = r"(?P<patch>0|[1-9]\d*)"
    p_rel = r"(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))"
    build = r"(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*)"
    regex_semver_pattern = r"^" + major + r"\." + minor + r"\." + patch + r"(?:-" + p_rel + r"*))?(?:\+" + build + r")?$"
    return match(regex_semver_pattern, tag_semver)
