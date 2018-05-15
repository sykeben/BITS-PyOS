# Built-in configuration defaults.
# Do not edit; edit /boot/bits-cfg.txt instead.
defaults = """
# BITS configuration file
[bits]

# To run BITS in batch mode, set batch to a list of one or more of the
# following keywords; BITS will then run all of the requested operations, then
# save the log file to disk.
#
# test: Run the full BITS testsuite.
# acpi: Dump all ACPI structures.
# smbios: Dump all SMBIOS structures.
#
# Leave batch set to an empty string to disable batch mode.
batch =

# Uncomment the following to run all available batch operations
#batch = test acpi smbios
"""
