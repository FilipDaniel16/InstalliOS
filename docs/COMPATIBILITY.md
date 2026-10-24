InstalliOS Device Compatibility — Motorola Moto G(60)

Status

Research only — not verified compatible.

InstalliOS is investigating whether an iOS 16.5 environment can be booted on the Motorola Moto G(60).

Target device

Property| Current information
Manufacturer| Motorola
Model| Moto G(60)
Device codename| "hanoip"
SoC| Qualcomm Snapdragon 732G
GPU| Qualcomm Adreno 618
CPU architecture| ARM64
Boot method goal| Temporary boot, if supported
Compatibility status| Unverified

The "hanoip" codename is shared with the Moto G40 Fusion. Exact device identity and hardware configuration must be confirmed before attempting any boot operation.

Existing research

An Android device tree is available for this hardware:

- https://github.com/motorola-sm6150-devs/android_device_motorola_hanoip

This is an Android device configuration, not an iOS-compatible boot image.

The HackiOS source code and porting documentation are additional research starting points:

- https://github.com/oosexgang/hackios-xnu-kernel
- https://github.com/oosexgang/hackios-xnu-userland

Compatibility requirements

The following items must be investigated before attempting to boot InstalliOS:

- [ ] Confirm the exact phone variant and device codename.
- [ ] Review the existing HackiOS loader and device profile architecture.
- [ ] Determine whether compatible UEFI support exists for this device.
- [ ] Investigate device-tree and memory-map requirements.
- [ ] Determine whether the bootloader supports temporary booting of the required image format.
- [ ] Investigate display and touchscreen initialization.
- [ ] Investigate CPU, interrupt-controller and timer support.
- [ ] Investigate storage and firmware requirements.
- [ ] Investigate GPU, audio, camera and Wi-Fi drivers.
- [ ] Establish a recovery procedure before device testing.

File safety requirements

Every future boot artifact must:

1. Match an explicitly supported device profile.
2. Match a trusted manifest containing its expected SHA-256 hash.
3. Pass cryptographic hash verification before use.
4. Be rejected if its hash, manifest signature or device compatibility check fails.
5. Require explicit user confirmation before any operation that modifies device state.

A SHA-256 hash verifies file integrity against a trusted expected value. By itself, it does not establish that a file is authentic or safe.

Testing policy

No firmware flashing, partition erasure or bootloader unlocking is authorized by this research profile.

Temporary boot must not be attempted until the image format, loader compatibility, device support and recovery procedure have been verified.

Evidence log

No successful InstalliOS boot has been demonstrated on the Motorola Moto G(60).

Record future findings here with links to the relevant source code, documentation, tests and reproducible results.

Disclaimer

InstalliOS is an independent experimental project and is not affiliated with Apple or Motorola. Compatibility with iOS 16.5 has not been established for this device.
