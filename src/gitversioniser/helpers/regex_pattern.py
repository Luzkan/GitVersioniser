from re import match


class RegexPattern:
    @staticmethod
    def semver(tag_semver: str):
        """
        https://regex101.com/r/Ly7O1x/3/
        https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string
        """
        major = r"(?P<major>0|[1-9]\d*)"
        minor = r"(?P<minor>0|[1-9]\d*)"
        patch = r"(?P<patch>0|[1-9]\d*)"
        p_rel = r"(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))"
        build = r"(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*)"
        regex_semver_pattern = r"^" + major + r"\." + minor + r"\." + patch + r"(?:-" + p_rel + r"*))?(?:\+" + build + r")?$"
        return match(regex_semver_pattern, tag_semver)

    @staticmethod
    def semver_substring_to_number(semver_string: str):
        """
        https://regex101.com/r/fGHzqV/1
        """
        all_but_digits = r"[^\d]"
        match_digits = r"(\d+)"
        regex = r"(?:" + all_but_digits + r"*" + match_digits + all_but_digits + r"*)+"
        return match(regex, semver_string)
