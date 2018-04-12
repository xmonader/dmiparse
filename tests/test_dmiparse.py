# Sample Test passing with nose and pytest

from dmiparse import dmiparse

sample1 = """
# dmidecode 3.1
Getting SMBIOS data from sysfs.
SMBIOS 2.6 present.

Handle 0x0001, DMI type 1, 27 bytes
System Information
		Manufacturer: LENOVO
		Product Name: 20042
		Version: Lenovo G560
		Serial Number: 2677240001087
		UUID: CB3E6A50-A77B-E011-88E9-B870F4165734
		Wake-up Type: Power Switch
		SKU Number: Calpella_CRB
		Family: Intel_Mobile

"""
sample2 = """
Getting SMBIOS data from sysfs.
SMBIOS 2.6 present.

Handle 0x0000, DMI type 0, 24 bytes
BIOS Information
		Vendor: LENOVO
		Version: 29CN40WW(V2.17)
		Release Date: 04/13/2011
		ROM Size: 2048 kB
		Characteristics:
				PCI is supported
				BIOS is upgradeable
				BIOS shadowing is allowed
				Boot from CD is supported
				Selectable boot is supported
				EDD is supported
				Japanese floppy for NEC 9800 1.2 MB is supported (int 13h)
				Japanese floppy for Toshiba 1.2 MB is supported (int 13h)
				5.25"/360 kB floppy services are supported (int 13h)
				5.25"/1.2 MB floppy services are supported (int 13h)
				3.5"/720 kB floppy services are supported (int 13h)
				3.5"/2.88 MB floppy services are supported (int 13h)
				8042 keyboard services are supported (int 9h)
				CGA/mono video services are supported (int 10h)
				ACPI is supported
				USB legacy is supported
				BIOS boot specification is supported
				Targeted content distribution is supported
		BIOS Revision: 1.40

"""
sample3 = """
# dmidecode 3.1
Getting SMBIOS data from sysfs.
SMBIOS 2.6 present.

Handle 0x0001, DMI type 1, 27 bytes
System Information
		Manufacturer: LENOVO
		Product Name: 20042
		Version: Lenovo G560
		Serial Number: 2677240001087
		UUID: CB3E6A50-A77B-E011-88E9-B870F4165734
		Wake-up Type: Power Switch
		SKU Number: Calpella_CRB
		Family: Intel_Mobile

Handle 0x000D, DMI type 12, 5 bytes
System Configuration Options
		Option 1: String1 for Type12 Equipment Manufacturer
		Option 2: String2 for Type12 Equipment Manufacturer
		Option 3: String3 for Type12 Equipment Manufacturer
		Option 4: String4 for Type12 Equipment Manufacturer

Handle 0x000E, DMI type 15, 29 bytes
System Event Log
		Area Length: 0 bytes
		Header Start Offset: 0x0000
		Data Start Offset: 0x0000
		Access Method: General-purpose non-volatile data functions
		Access Address: 0x0000
		Status: Valid, Not Full
		Change Token: 0x12345678
		Header Format: OEM-specific
		Supported Log Type Descriptors: 3
		Descriptor 1: POST memory resize
		Data Format 1: None
		Descriptor 2: POST error
		Data Format 2: POST results bitmap
		Descriptor 3: Log area reset/cleared
		Data Format 3: None

Handle 0x0011, DMI type 32, 20 bytes
System Boot Information
		Status: No errors detected

"""
sample4 = """
# dmidecode 3.1
Getting SMBIOS data from sysfs.
SMBIOS 2.6 present.

Handle 0x0000, DMI type 0, 24 bytes
BIOS Information
		Vendor: LENOVO
		Version: 29CN40WW(V2.17)
		Release Date: 04/13/2011
		ROM Size: 2048 kB
		Characteristics:
				PCI is supported
				BIOS is upgradeable
				BIOS shadowing is allowed
				Boot from CD is supported
				Selectable boot is supported
				EDD is supported
				Japanese floppy for NEC 9800 1.2 MB is supported (int 13h)
				Japanese floppy for Toshiba 1.2 MB is supported (int 13h)
				5.25"/360 kB floppy services are supported (int 13h)
				5.25"/1.2 MB floppy services are supported (int 13h)
				3.5"/720 kB floppy services are supported (int 13h)
				3.5"/2.88 MB floppy services are supported (int 13h)
				8042 keyboard services are supported (int 9h)
				CGA/mono video services are supported (int 10h)
				ACPI is supported
				USB legacy is supported
				BIOS boot specification is supported
				Targeted content distribution is supported
		BIOS Revision: 1.40

Handle 0x002C, DMI type 4, 42 bytes
Processor Information
		Socket Designation: CPU
		Type: Central Processor
		Family: Core 2 Duo
		Manufacturer: Intel(R) Corporation
		ID: 55 06 02 00 FF FB EB BF
		Signature: Type 0, Family 6, Model 37, Stepping 5
		Flags:
				FPU (Floating-point unit on-chip)
				VME (Virtual mode extension)
				DE (Debugging extension)
				PSE (Page size extension)
				TSC (Time stamp counter)
				MSR (Model specific registers)
				PAE (Physical address extension)
				MCE (Machine check exception)
				CX8 (CMPXCHG8 instruction supported)
				APIC (On-chip APIC hardware supported)
				SEP (Fast system call)
				MTRR (Memory type range registers)
				PGE (Page global enable)
				MCA (Machine check architecture)
				CMOV (Conditional move instruction supported)
				PAT (Page attribute table)
				PSE-36 (36-bit page size extension)
				CLFSH (CLFLUSH instruction supported)
				DS (Debug store)
				ACPI (ACPI supported)
				MMX (MMX technology supported)
				FXSR (FXSAVE and FXSTOR instructions supported)
				SSE (Streaming SIMD extensions)
				SSE2 (Streaming SIMD extensions 2)
				SS (Self-snoop)
				HTT (Multi-threading)
				TM (Thermal monitor supported)
				PBE (Pending break enabled)
		Version: Intel(R) Core(TM) i3 CPU       M 370  @ 2.40GHz
		Voltage: 0.0 V
		External Clock: 1066 MHz
		Max Speed: 2400 MHz
		Current Speed: 2399 MHz
		Status: Populated, Enabled
		Upgrade: ZIF Socket
		L1 Cache Handle: 0x0030
		L2 Cache Handle: 0x002F
		L3 Cache Handle: 0x002D
		Serial Number: Not Specified
		Asset Tag: FFFF
		Part Number: Not Specified
		Core Count: 2
		Core Enabled: 2
		Thread Count: 4
		Characteristics:
				64-bit capable

"""

biosInfoTests = {
		"Vendor": "LENOVO",
		"Version": "29CN40WW(V2.17)",
		"Release Date": "04/13/2011",
		"ROM Size": "2048 kB",
		"Characteristics": "",
		"BIOS Revision": "1.40",
}
sysInfoTests = {
		"Manufacturer": "LENOVO",
		"Product Name": "20042",
		"Version": "Lenovo G560",
		"Serial Number": "2677240001087",
		"UUID": "CB3E6A50-A77B-E011-88E9-B870F4165734",
		"Wake-up Type": "Power Switch",
		"SKU Number" : "Calpella_CRB",
		"Family": "Intel_Mobile",
}

sysConfigurationTests = {
	"Option 1": "String1 for Type12 Equipment Manufacturer",
	"Option 2": "String2 for Type12 Equipment Manufacturer",
	"Option 3": "String3 for Type12 Equipment Manufacturer",
	"Option 4": "String4 for Type12 Equipment Manufacturer",
}

sysEventLogTests = {
	"Area Length": "0 bytes",
	"Header Start Offset": "0x0000",
	"Data Start Offset": "0x0000",
	"Access Method": "General-purpose non-volatile data functions",
	"Access Address": "0x0000",
	"Status": "Valid, Not Full",
	"Change Token": "0x12345678",
	"Header Format": "OEM-specific",
	"Supported Log Type Descriptors": "3",
	"Descriptor 1": "POST memory resize",
	"Data Format 1": "None",
	"Descriptor 2": "POST error",
	"Data Format 2": "POST results bitmap",
	"Descriptor 3": "Log area reset/cleared",
	"Data Format 3": "None",
}

sysBootTests = {
	"Status": "No errors detected",
}

processorTests = {
		"Socket Designation": "CPU",
		"Type": "Central Processor",
		"Family": "Core 2 Duo",
		"Manufacturer": "Intel(R) Corporation",
		"ID": "55 06 02 00 FF FB EB BF",
		"Signature": "Type 0, Family 6, Model 37, Stepping 5",
		"Flags": "",
		"Version": "Intel(R) Core(TM) i3 CPU       M 370  @ 2.40GHz",
		"Voltage": "0.0 V",
		"External Clock": "1066 MHz",
		"Max Speed": "2400 MHz",
		"Current Speed": "2399 MHz",
		"Status": "Populated, Enabled",
		"Upgrade": "ZIF Socket",
		"L1 Cache Handle": "0x0030",
		"L2 Cache Handle": "0x002F",
		"L3 Cache Handle": "0x002D",
		"Serial Number": "Not Specified",
		"Asset Tag": "FFFF",
		"Part Number": "Not Specified",
		"Core Count": "2",
		"Core Enabled": "2",
		"Thread Count": "4",
		"Characteristics":"",
}

def test_parse_simple_section():
	dmi = dmiparse(sample1)
	
	assert len(dmi) == 1
	assert len(dmi["System Information"].props)==8
	assert "System Information" == dmi["System Information"].title

	for k, v in sysInfoTests.items():
		assert dmi["System Information"].props[k].val == v

def test_parse_section_with_list_property():
	dmi = dmiparse(sample2)

	assert len(dmi) == 1
	assert len(dmi["BIOS Information"].props) == 6
	assert dmi["BIOS Information"].title == "BIOS Information"
	assert len(dmi["BIOS Information"].props["Characteristics"].items) == 18

	for k, v in biosInfoTests.items():
		assert dmi["BIOS Information"].props[k].val == v



def test_parse_multiple_simple_sections():
	dmi = dmiparse(sample3)

	assert len(dmi) == 4

	for k, v in sysInfoTests.items():
		assert v == dmi["System Information"].props[k].val

	for k, v in sysConfigurationTests.items():
		assert v == dmi["System Configuration Options"].props[k].val

	for k, v in sysEventLogTests.items():
		assert v == dmi["System Event Log"].props[k].val

	for k, v in sysBootTests.items():
		assert v == dmi["System Boot Information"].props[k].val

def test_parse_multiple_with_list_properties():
	dmi = dmiparse(sample4)

	assert len(dmi) == 2
	assert len(dmi["BIOS Information"].props["Characteristics"].items) == 18
	assert len(dmi["Processor Information"].props) == 24
	assert len(dmi["Processor Information"].props["Flags"].items) == 28

	for k, v in biosInfoTests.items():
		assert dmi["BIOS Information"].props[k].val == v

	for k, v in processorTests.items():
		assert  v == dmi["Processor Information"].props[k].val

