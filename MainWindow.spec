# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(5000)


block_cipher = None

SETUP_DIR = 'F:\PythonProject\chargestation'

a = Analysis(['MainWindow.py',
              'F:\PythonProject\chargestation\delegate\myDelegates.py',
              'F:\PythonProject\chargestation\mapper\ChargeMapper.py',
              r'F:\PythonProject\chargestation\mapper\UserMapper.py',
              r'F:\PythonProject\chargestation\UI\bar_win.py',
              r'F:\PythonProject\chargestation\UI\LogInWindow.py',
              r'F:\PythonProject\chargestation\UI\main_rc.py',
              r'F:\PythonProject\chargestation\UI\mainbar.py',
              r'F:\PythonProject\chargestation\UI\MainWindow.py',
              r'F:\PythonProject\chargestation\UI\ParametersWindow.py',
              r'F:\PythonProject\chargestation\UI\PlotSubWindow.py',
              r'F:\PythonProject\chargestation\UI\PlotSubWindow2.py',
              r'F:\PythonProject\chargestation\UI\PlotWindow.py',
              r'F:\PythonProject\chargestation\UI\qss_rc.py',
              r'F:\PythonProject\chargestation\UI\SigninWindow.py',
              r'F:\PythonProject\chargestation\UI\Ui_LogInWindow.py',
              r'F:\PythonProject\chargestation\UI\Ui_MainWindow.py',
              r'F:\PythonProject\chargestation\UI\Ui_ParametersWindow.py',
              r'F:\PythonProject\chargestation\UI\Ui_PlotSubWindow.py',
              r'F:\PythonProject\chargestation\UI\Ui_PlotWindow.py',
              r'F:\PythonProject\chargestation\UI\Ui_SigninWindow.py',
              r'F:\PythonProject\chargestation\UI\Ui_UserManageWindow.py',
              r'F:\PythonProject\chargestation\UI\Ui_webEngineView.py',
              r'F:\PythonProject\chargestation\UI\UserManageWindow.py',
              r'F:\PythonProject\chargestation\Util\Grade.py',
              r'F:\PythonProject\chargestation\Util\Plot.py',
              'call_mainbar.py',
              'Common.py',
              'dataProcess.py',
              'graphyWindow.py',
              'ImportDatatoExcel.py',
              'ImportDateFromExcel.py',
              'LoginWindow.py',
              'main.py',
              'MapDisplay.py',
              'ParamsSetWindow.py',
              'PlotSubWindow.py',
              'PlotWindow.py',
              'PlotWindowTemp.py',
              'SigninWindow.py',
              'UserManageWindow.py'],
             pathex=[],
             binaries=[],
             datas=[(SETUP_DIR+'\Config','Config'),
                    (SETUP_DIR+'\Icon','Icon'),
                    (SETUP_DIR+'\Log','Log'),
                    (SETUP_DIR+r'\UI','UI')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='MainWindow',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='MainWindow')