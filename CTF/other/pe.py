import pefile
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file.exe>")
    sys.exit(1)

pe_path = sys.argv[1]

try:
    pe = pefile.PE(pe_path)
except FileNotFoundError:
    print(f"File not found: {pe_path}")
    sys.exit(1)
except pefile.PEFormatError as e:
    print(f"Not a valid PE file: {e}")
    sys.exit(1)

print(f"=== File: {pe_path} ===\n")

# COFF Header
print("=== COFF Header ===")
coff = pe.FILE_HEADER
print(f"Machine: {hex(coff.Machine)}")
print(f"Number of Sections: {coff.NumberOfSections}")
print(f"TimeDateStamp: {coff.TimeDateStamp}")
print(f"PointerToSymbolTable: {coff.PointerToSymbolTable}")
print(f"NumberOfSymbols: {coff.NumberOfSymbols}")
print(f"Characteristics: {hex(coff.Characteristics)}\n")

# Optional Header
print("=== Optional Header ===")
opt = pe.OPTIONAL_HEADER
print(f"Magic: {hex(opt.Magic)}")
print(f"AddressOfEntryPoint: {hex(opt.AddressOfEntryPoint)}")
print(f"ImageBase: {hex(opt.ImageBase)}")
print(f"Subsystem: {opt.Subsystem}")
print(f"DllCharacteristics: {hex(opt.DllCharacteristics)}")
print(f"Number of Data Directories: {len(opt.DATA_DIRECTORY)}\n")

# Check for .NET (CLI Header)
if hasattr(opt, 'DATA_DIRECTORY'):
    clr_entry = opt.DATA_DIRECTORY[14] 
    if clr_entry.VirtualAddress != 0:
        print(f"CLI Header RVA: {hex(clr_entry.VirtualAddress)} Size: {hex(clr_entry.Size)}")
print()

# Sections
print("=== Sections ===")
for section in pe.sections:
    print(f"{section.Name.decode().rstrip(chr(0))}: VA={hex(section.VirtualAddress)}, "
          f"Size={hex(section.Misc_VirtualSize)}, RawSize={hex(section.SizeOfRawData)}")

