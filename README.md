# OpenRevolver 🔫

An open-source revolver-style multi-nozzle system for 3D printers

## 🎯 Project Vision

OpenRevolver is a community-driven project to create a revolutionary hotend system that combines the best aspects of tool changers with multi-material capabilities. Inspired by Bambu Lab's Vortek system but designed for the open-source community, this project aims to bring wireless, multi-nozzle technology to Voron and other open-source 3D printers.

## 💡 Core Concept

Imagine a revolver cylinder at the business end of your hotend, with each chamber containing:
- Different nozzle sizes (0.2mm, 0.4mm, 0.6mm, 0.8mm)
- Different materials pre-loaded
- Wireless temperature monitoring
- Inductive heating capability

**No more purge blocks. No more filament waste. No more compromises.**

## 🚀 Key Features

### Wireless Technology
- ESP32 or similar MCU in each nozzle cartridge
- Real-time temperature monitoring
- Material type identification
- Zero physical connectors to wear out

### Inductive Power Delivery
- Qi-style wireless charging technology
- 15-25W per nozzle capability
- 8-second heat-up time target
- No electrical contacts needed

### Mechanical Design
- Precision revolver mechanism
- Servo or stepper-driven rotation
- Micrometer-level alignment
- Compatible with Voron Stealthburner (initial target)

### Multi-Configuration Support
- 6 nozzles per revolver (expandable)
- Mix of nozzle sizes and materials
- Optional: Multiple revolvers on tool changer
- Future: Different hotend geometries per chamber

## 🔧 Technical Implementation

### Hardware Requirements
- Custom PCB with wireless MCU + thermistor interface
- Inductive power receiver coils
- Precision indexing mechanism
- Modified heat breaks for quick-change support
- Servo/stepper for rotation control

### Software Stack
- Klipper integration (primary target)
- CAN bus communication
- Custom MCU firmware
- Slicer plugins for nozzle selection

### Target Platform
- **Primary**: Voron Stealthburner
- **Secondary**: Other open-source toolheads
- **Future**: Universal mounting system

## 📊 Advantages Over Current Systems

| Feature | AMS/MMU | Tool Changers | Vortek | OpenRevolver |
|---------|---------|---------------|---------|--------------|
| Zero Purge | ❌ | ✅ | ✅ | ✅ |
| Multiple Nozzle Sizes | ❌ | Per Tool | ❌ | ✅ |
| Wireless Operation | ❌ | ❌ | ✅ | ✅ |
| Open Source | ❌ | ✅ | ❌ | ✅ |
| Compact Design | ✅ | ❌ | ✅ | ✅ |

## 🛠️ Development Roadmap

### Phase 1: Proof of Concept
- [ ] Basic revolver mechanism design
- [ ] Wireless temperature monitoring
- [ ] Single nozzle inductive heating test
- [ ] Klipper integration research

### Phase 2: Alpha Prototype
- [ ] 3-nozzle revolver prototype
- [ ] Full wireless communication
- [ ] Power delivery system
- [ ] Basic software integration

### Phase 3: Beta Release
- [ ] 6-nozzle system
- [ ] Refined mechanical design
- [ ] Complete Klipper integration
- [ ] Slicer plugin development

### Phase 4: Community Release
- [ ] Full documentation
- [ ] Multiple printer support
- [ ] Advanced features
- [ ] Kit availability

## 🤝 Contributing

We welcome contributions from the community! Whether you're skilled in:
- Mechanical design (CAD/SolidWorks)
- Electronics (PCB design, wireless systems)
- Firmware development (C/C++, Python)
- Klipper configuration
- Documentation
- Testing and validation

...there's a place for you in this project!

### Getting Started
1. Fork the repository
2. Check the [Issues](../../issues) for current tasks
3. Join our [Discord](#) for discussions
4. Submit PRs with your contributions

## 📁 Repository Structure

```
open-revolver/
├── hardware/
│   ├── mechanical/     # CAD files, STLs
│   ├── electronics/    # PCB designs, schematics
│   └── bom/           # Bill of materials
├── firmware/
│   ├── mcu/           # Nozzle MCU firmware
│   └── klipper/       # Klipper integration
├── software/
│   └── slicer/        # Slicer plugins
├── docs/
│   ├── assembly/      # Build instructions
│   ├── calibration/   # Setup guides
│   └── api/           # Technical documentation
└── examples/          # Sample configurations
```

## 🎯 Design Principles

1. **Open Source First**: All designs, code, and documentation freely available
2. **Modular Design**: Components can be upgraded independently
3. **Community Driven**: Decisions made transparently with community input
4. **Quality Focus**: Reliability and precision over feature creep
5. **Accessibility**: Keep costs reasonable, parts sourceable

## 📸 Concept Renders

*Coming soon - SolidWorks renders and prototypes*

## 🙏 Acknowledgments

- Inspired by Bambu Lab's Vortek system announcement
- Built on the shoulders of the Voron Design community
- Leveraging work from ERCF, Klicky, and other open-source projects

## 📜 License

This project is licensed under the GPL v3.0 License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Project Website](#) (Coming Soon)
- [Discord Community](#) (Coming Soon)
- [Documentation Wiki](#) (Coming Soon)
- [YouTube Channel](#) (Coming Soon)

---

**"Why have one nozzle when you can have six?"** 🎯

*Started: August 29, 2025*