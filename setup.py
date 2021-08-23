import cx_Freeze

executables = [ cx_Freeze.Executable("Juego.py",
                                     icon = "Imagenes/Icono.ico",
                                     shortcut_name="Mente Brillante",
                                     shortcut_dir="DesktopFolder"
                                     )]

cx_Freeze.setup(
        name="Mente Brillante",
        options={"build_exe":{"packages":["pygame","pymunk","numpy"],
                              "include_files":["Imagenes","Audios","Fonts"]}},
        executables = executables
    ) 