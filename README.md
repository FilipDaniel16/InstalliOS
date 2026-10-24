InstalliOS

Experimental iOS compatibility research and device-porting project

InstalliOS explores the technical requirements for running an iOS 16.5 environment on non-Apple hardware, starting with research into the Motorola Moto G(60).

«Project status: Research only. No Motorola boot image is currently verified or supported.»

Initial target

- Device: Motorola Moto G(60)
- Device codename: "hanoip"
- Chipset: Qualcomm Snapdragon 732G
- Architecture: ARM64
- Boot goal: Temporary boot, if compatible with the device's bootloader and loader
- Development host: Windows 11, with Linux build tooling if required

Project goals

- Investigate existing HackiOS source code and device-porting requirements.
- Research the Motorola "hanoip" hardware platform.
- Develop device identification and file-verification tools.
- Verify downloaded artifacts using trusted SHA-256 manifests.
- Reject corrupted files and incompatible device targets.
- Investigate display, input, storage, and Wi-Fi compatibility.
- Document installation prerequisites and recovery procedures.

Safety

InstalliOS is experimental research software.

- Do not flash unverified images.
- Do not assume that Snapdragon hardware guarantees compatibility.
- Do not unlock a bootloader without understanding the data-loss implications.
- Do not distribute proprietary firmware without authorization.
- Require explicit confirmation before any future operation that modifies a device.

Development status

- [x] Initial project scope defined
- [x] First device selected
- [ ] Upstream source and licensing review
- [ ] Motorola compatibility investigation
- [ ] Device detection prototype
- [ ] Trusted manifest and SHA-256 verification
- [ ] Build environment validated
- [ ] Device-specific loader feasibility established
- [ ] Hardware testing

Disclaimer

InstalliOS is an independent experimental project. It is not an official Apple or Motorola product. iOS compatibility, bootability, and hardware functionality have not been established for the target device.
