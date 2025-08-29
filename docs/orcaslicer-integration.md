# OrcaSlicer Integration Guide

## Overview

OpenRevolver works with OrcaSlicer through three integration methods:

1. **Post-Processing Script** (Easiest - Start Here)
2. **Klipper Macro Translation** (Medium)
3. **Native OrcaSlicer Fork** (Advanced - Future)

## Method 1: Post-Processing Script

### Setup

1. Configure OrcaSlicer for multi-material:
   - Add 6 "filaments" representing your 6 nozzles
   - Name them by size: "PLA 0.4mm", "PLA 0.2mm", etc.
   - Set appropriate temperatures for each

2. In OrcaSlicer, go to **Print Settings → Output Options → Post-processing scripts**

3. Add the command:
   ```
   python3 /path/to/revolver_postprocess.py
   ```

### Usage

1. Design your multi-material model
2. Assign "filaments" (nozzles) to different parts
3. Slice normally
4. The script automatically converts tool changes to revolver commands

### Advanced: Feature-Based Nozzle Selection

Enable automatic nozzle switching based on feature type:

```bash
python3 revolver_postprocess.py input.gcode --feature-aware
```

This automatically selects:
- 0.2mm for overhangs and support interfaces
- 0.4mm for perimeters and solid infill
- 0.6-0.8mm for internal infill
- 1.0mm for support structures

## Method 2: Klipper Macro Translation

### Setup

1. Include the revolver.cfg in your printer.cfg:
   ```
   [include revolver.cfg]
   ```

2. Configure OrcaSlicer for standard tool changes:
   - Set up as a multi-extruder printer
   - Use T0, T1, T2, etc. for tool changes

3. The Klipper macros intercept tool changes and convert them

### Custom Tool Change G-code

In OrcaSlicer's **Machine G-code → Tool change G-code**:

```gcode
; OpenRevolver tool change
; Map tool to nozzle based on your needs
{% if current_extruder == 0 %}
  REVOLVER_SELECT NOZZLE=0  ; 0.4mm standard
{% elif current_extruder == 1 %}
  REVOLVER_SELECT NOZZLE=1  ; 0.2mm detail
{% elif current_extruder == 2 %}
  REVOLVER_SELECT NOZZLE=4  ; 0.8mm infill
{% endif %}
```

## Nozzle Mapping Strategy

### By Material Type
- T0 → Nozzle 0: PLA 0.4mm (standard)
- T1 → Nozzle 1: PLA 0.2mm (detail) 
- T2 → Nozzle 2: PETG 0.6mm
- T3 → Nozzle 3: ABS 0.4mm
- T4 → Nozzle 4: PLA 0.8mm (fast)
- T5 → Nozzle 5: TPU 0.6mm

### By Feature Type
- External walls → 0.4mm
- Fine details → 0.2mm
- Infill → 0.8mm
- Support → 0.6mm
- First layer → 0.4mm

## OrcaSlicer Settings

### Recommended Filament Settings

For each "filament" (nozzle), adjust:

1. **Filament diameter**: Keep at 1.75mm
2. **Nozzle diameter**: Set to actual nozzle size
3. **Layer height limits**:
   - 0.2mm nozzle: 0.05-0.15mm layers
   - 0.4mm nozzle: 0.1-0.3mm layers
   - 0.6mm nozzle: 0.2-0.45mm layers
   - 0.8mm nozzle: 0.3-0.6mm layers

4. **Line width**:
   - Default: 120% of nozzle diameter
   - First layer: 140% of nozzle diameter

### Print Settings

1. **Different nozzle for supports**: Enable
2. **Tool change retraction**: Minimal (no purge needed!)
3. **Wipe tower**: DISABLE (not needed!)

## Troubleshooting

### Tool Changes Not Working
- Verify post-processing script path is correct
- Check script has execute permissions: `chmod +x revolver_postprocess.py`
- Test manually: `python3 revolver_postprocess.py test.gcode`

### Wrong Nozzle Selected
- Check nozzle mapping in script configuration
- Verify Klipper macro definitions
- Enable verbose logging in Klipper

### Temperature Issues
- Each nozzle maintains its own temperature
- Pre-heat next nozzle during previous layer
- Use `revolver_postprocess.py` temperature management

## Future: Native OrcaSlicer Fork

We're planning a native fork that will:
- Show nozzle sizes in the UI
- Calculate flow rates per nozzle
- Optimize tool paths for nozzle changes
- Preview which nozzle is used where

Want to help? Check our [GitHub Issues](https://github.com/SamuraiBuddha/open-revolver/issues)!
