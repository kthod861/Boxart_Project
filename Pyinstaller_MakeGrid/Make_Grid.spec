# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['F:\\Boxart_Project\\Pyinstaller_MakeGrid/Make_Grid.py'],
    pathex=[],
    binaries=[],
    datas=[('F:\\Boxart_Project\\Pyinstaller_MakeGrid/Lib/MCL.ico', 'Lib/'), ('F:\\Boxart_Project\\Pyinstaller_MakeGrid/Lib/Demo.ui', 'Lib/'), ('F:\\Boxart_Project\\Pyinstaller_MakeGrid/Lib/Demo_Lib.py', 'Lib/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Make_Grid',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['F:\\Boxart_Project\\Pyinstaller_MakeGrid\\Lib\\MCL.ico'],
)
