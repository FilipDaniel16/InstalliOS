
import json
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "manufacturer",
    "model",
    "codename",
    "soc",
    "architecture",
    "target_os",
    "status",
    "verified_compatible",
    "allow_boot",
]


def validate_device_profile(profile):
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in profile:
            errors.append(f"Missing required field: {field}")

    if errors:
        return False, errors

    if profile["manufacturer"] != "Motorola":
        errors.append("Unexpected manufacturer.")

    if profile["codename"] != "hanoip":
        errors.append("Device codename does not match this profile.")

    if profile["verified_compatible"] is not True:
        errors.append("Device compatibility is not verified.")

    if profile["allow_boot"] is not True:
        errors.append("Boot operations are disabled for this profile.")

    if profile["status"] != "verified":
        errors.append("Device status is not verified.")

    return not errors, errors


def main():
    if len(sys.argv) != 2:
        print("Usage: python device_check.py <device.json>")
        return 2

    path = Path(sys.argv[1])

    try:
        profile = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: Cannot read device profile: {exc}")
        return 2

    if not isinstance(profile, dict):
        print("ERROR: Device profile must be a JSON object.")
        return 2

    valid, errors = validate_device_profile(profile)

    if not valid:
        print("BLOCKED: Device profile is not approved.")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Profile passed basic validation.")
    print("WARNING: This does not prove hardware compatibility.")
    print("No device commands were executed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
      
