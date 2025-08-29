#!/usr/bin/env python3
"""
OpenRevolver Post-Processing Script for OrcaSlicer
Converts standard tool changes to revolver nozzle selections
"""

import sys
import re
import argparse
from pathlib import Path

class RevolverPostProcessor:
    def __init__(self):
        # Nozzle configuration - customize for your setup
        self.nozzle_config = {
            0: {"diameter": 0.4, "material": "PLA", "temp": 210},
            1: {"diameter": 0.2, "material": "PLA", "temp": 215},
            2: {"diameter": 0.6, "material": "PETG", "temp": 240},
            3: {"diameter": 0.4, "material": "ABS", "temp": 245},
            4: {"diameter": 0.8, "material": "PLA", "temp": 220},
            5: {"diameter": 1.0, "material": "PETG", "temp": 245},
        }
        
        # Mapping of features to optimal nozzle sizes
        self.feature_nozzle_map = {
            "perimeter": 0.4,
            "external_perimeter": 0.4,
            "overhang_perimeter": 0.2,
            "internal_infill": 0.8,
            "solid_infill": 0.4,
            "top_solid_infill": 0.4,
            "bridge_infill": 0.4,
            "support": 0.6,
            "support_interface": 0.2,
        }
        
        self.current_nozzle = 0
        self.current_temp = 0
    
    def find_nozzle_for_diameter(self, diameter):
        """Find nozzle index for requested diameter"""
        for idx, config in self.nozzle_config.items():
            if abs(config["diameter"] - diameter) < 0.01:
                return idx
        return 0  # Default to first nozzle
    
    def find_nozzle_for_feature(self, feature_type):
        """Select optimal nozzle for feature type"""
        if feature_type in self.feature_nozzle_map:
            diameter = self.feature_nozzle_map[feature_type]
            return self.find_nozzle_for_diameter(diameter)
        return self.current_nozzle
    
    def process_line(self, line):
        """Process a single G-code line"""
        # Tool change pattern
        tool_change = re.match(r'^T(\d+)', line)
        if tool_change:
            tool_num = int(tool_change.group(1))
            # Map tools to nozzles (can be customized)
            nozzle = tool_num % 6
            return f"REVOLVER_SELECT TOOL={tool_num} NOZZLE={nozzle}\n"
        
        # Feature type comment pattern (OrcaSlicer format)
        feature_comment = re.match(r'^;TYPE:(.+)', line)
        if feature_comment:
            feature_type = feature_comment.group(1).lower()
            new_nozzle = self.find_nozzle_for_feature(feature_type)
            
            if new_nozzle != self.current_nozzle:
                self.current_nozzle = new_nozzle
                nozzle_change = f"; Switching to {self.nozzle_config[new_nozzle]['diameter']}mm nozzle for {feature_type}\n"
                nozzle_change += f"REVOLVER_SELECT NOZZLE={new_nozzle}\n"
                
                # Update temperature if needed
                new_temp = self.nozzle_config[new_nozzle]["temp"]
                if new_temp != self.current_temp:
                    self.current_temp = new_temp
                    nozzle_change += f"M104 S{new_temp} ; Set nozzle temp\n"
                    nozzle_change += f"M109 S{new_temp} ; Wait for temp\n"
                
                return line + nozzle_change
        
        # Temperature setting pattern
        temp_set = re.match(r'^M104 S(\d+)', line)
        if temp_set:
            self.current_temp = int(temp_set.group(1))
        
        # Filament diameter comment (adjust flow for nozzle)
        filament_comment = re.match(r'^; filament_diameter = ([\d.]+)', line)
        if filament_comment:
            # Add nozzle diameter info
            nozzle_dia = self.nozzle_config[self.current_nozzle]["diameter"]
            return line + f"; nozzle_diameter = {nozzle_dia}\n"
        
        return line
    
    def process_file(self, input_file, output_file):
        """Process entire G-code file"""
        with open(input_file, 'r') as f_in:
            lines = f_in.readlines()
        
        # Insert revolver initialization after start G-code
        processed_lines = []
        in_start_gcode = False
        
        for line in lines:
            if '; start_gcode_end' in line:
                in_start_gcode = False
                processed_lines.append(line)
                # Insert revolver init
                processed_lines.append("\n; OpenRevolver Initialization\n")
                processed_lines.append("REVOLVER_SELECT NOZZLE=0 ; Start with standard nozzle\n")
                processed_lines.append("M104 S{} ; Set initial temp\n".format(
                    self.nozzle_config[0]["temp"]))
                processed_lines.append("\n")
            else:
                processed_lines.append(self.process_line(line))
        
        # Write output
        with open(output_file, 'w') as f_out:
            f_out.writelines(processed_lines)
        
        print(f"✅ Processed {input_file} -> {output_file}")
        print(f"   Added {self.count_revolver_commands(processed_lines)} revolver commands")
    
    def count_revolver_commands(self, lines):
        """Count revolver-specific commands added"""
        return sum(1 for line in lines if 'REVOLVER_SELECT' in line)

def main():
    parser = argparse.ArgumentParser(description='OpenRevolver G-code post-processor')
    parser.add_argument('input', help='Input G-code file from OrcaSlicer')
    parser.add_argument('-o', '--output', help='Output file (default: input_revolver.gcode)')
    parser.add_argument('--feature-aware', action='store_true', 
                       help='Enable automatic nozzle switching based on features')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.parent / f"{input_path.stem}_revolver{input_path.suffix}"
    
    processor = RevolverPostProcessor()
    processor.process_file(input_path, output_path)

if __name__ == "__main__":
    main()
