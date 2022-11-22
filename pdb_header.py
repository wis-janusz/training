"""Quick and dirty script to replace PDB codes in pdb files HEADER with filenames. 

This scprits works only when placed inside a directory containing any number of pdb files.
It automatically replaces PDB codes in HEADER (line 1, columns starting at 63) with the filname for all pdb files in the directory.

Usage:

    Drop the file into a directory with pdb files.
    Type "python -m pdb_header" in the console.
"""
import glob

"""Reads a file as list of lines. Replaces the PDB code with the filename. Saves the file under the same name.

"""
def replace_PDB_header(filename: str):

    with open(filename, "r") as file_in:
        pdb_lines = file_in.readlines()

    strucutre_name_padded = filename[: filename.rfind(".")].ljust(18,' ')+'\n'
    pdb_lines[0] = pdb_lines[0].replace(pdb_lines[0][62:], strucutre_name_padded)

    with open(filename, "w") as file_out:
        file_out.writelines(pdb_lines)

"""Main loop of the program.

Detects all pdb files in the directory, executes replace_PDB_header and gives some minimal console output.

"""
if __name__ == "__main__":

    all_files = glob.glob("*.pdb")
    print(
        f"{len(all_files)} pdb files found. Replacing all PDB codes in HEADER with file names."
    )

    for pdb in glob.glob("*.pdb"):
        replace_PDB_header(pdb)
        print(f"File {pdb} HEADER replaced.")

    print(f"Done replacing HEADER of {len(all_files)} pdb files.")
