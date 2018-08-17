import cx_Freeze

executables = [cx_Freeze.Executable("Menu.py")]
cx_Freeze.setup(
	name="Killing Stalking",
	options={"build_exe":{"packages":["pygame","os","time","pygame.locals","ctypes"]}},
	description = "Killing stalking visual novel",
	executables = executables
	)