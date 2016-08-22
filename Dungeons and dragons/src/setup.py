from cx_Freeze import setup, Executable

setup(name='Edgy RPG Game',
      version='0.1',
      description='Stay edgy!',
      executables = [Executable("Dungeons_and_dragons.py")])
