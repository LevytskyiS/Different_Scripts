from pathlib import Path


file = Path("./practice/testpy.py")
main_folder = Path.cwd()
endfolder = Path("./testfolder")
end_path = main_folder.joinpath(endfolder).joinpath(file.name)
try:
    file.rename(end_path)
except FileNotFoundError as e:
    print("File not found")
