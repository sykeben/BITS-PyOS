## ![Logo](docs/common/icon.png) BITS-PyOS
### BIOS-Implementation-Test-Suite-based Python Operating System

**Be warned!** This is a hodge-podge of BITS, SysLinux, and my own code.  

This is an Operating System based on Intel's open-source BIOS Implementation Test Suite, or BITS. BITS is a bare metal Python interpreter made for testing hardware, firmware, etc. It uses SysLinux to boot, and run my own python code as the "UI".

### Links

[BITS Homepage](https://biosbits.org/ "BIOS Implementation Test Suite")  
[SysLinux Wiki](https://www.syslinux.org/wiki/index.php?title=The_Syslinux_Project "Syslinux Wiki")

### Building BITS-PyOS to a USB Drive

Follow the instructions in the `build2usb.md` file.

### Advantages of BITS-PyOS

- Quick to boot most of the time (due to being bare-metal Python based).
- Simple and easy to code for (due to running Python 2).
- Etc.

### Documentation

The rest of the documentation is in the `docs` folder, or [on the site here](https://sykeben.github.io/BITS-PyOS).
