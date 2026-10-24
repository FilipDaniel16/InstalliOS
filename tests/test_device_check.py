import unittest

from installer.device_check import validate_device_profile


def base_profile():
    return {
        "manufacturer": "Motorola",
        "model": "Moto G(60)",
        "codename": "hanoip",
        "soc": "Qualcomm Snapdragon 732G",
        "architecture": "ARM64",
        "target_os": "iOS 16.5",
        "status": "research",
        "verified_compatible": False,
        "allow_boot": False,
    }


class TestDeviceCheck(unittest.TestCase):
    def test_unverified_device_is_blocked(self):
        valid, errors = validate_device_profile(base_profile())

        self.assertFalse(valid)
        self.assertTrue(
            any("compatibility is not verified" in error for error in errors)
        )

    def test_boot_is_blocked_by_default(self):
        valid, errors = validate_device_profile(base_profile())

        self.assertFalse(valid)
        self.assertTrue(
            any("Boot operations are disabled" in error for error in errors)
        )

    def test_wrong_codename_is_rejected(self):
        profile = base_profile()
        profile["codename"] = "wrong-codename"

        valid, errors = validate_device_profile(profile)

        self.assertFalse(valid)
        self.assertTrue(
            any("codename does not match" in error for error in errors)
        )

    def test_missing_required_field_is_rejected(self):
        profile = base_profile()
        del profile["soc"]

        valid, errors = validate_device_profile(profile)

        self.assertFalse(valid)
        self.assertTrue(
            any("Missing required field: soc" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
      
