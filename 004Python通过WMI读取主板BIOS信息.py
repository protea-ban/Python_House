#!/usr/bin/u/ubv/a python
# -*- coding:utf-8 -*-

import wmi
bios = wmi.WMI().Win32_BIOS()[0]

print('完整版本信息：', bios.BIOSVersion)
print('内部识别号：', bios.BuildNumber)
print('代码集：', bios.CodeSet)
print('当前语言：', bios.CurrentLanguage)
print('简要描述信息：', bios.Description)
print(bios.IdentificationCode)
print('制造商：', bios.Manufacturer)
print('名称:', bios.Name)
print('当前操作系统：', bios.TargetOperatingSystem)
print('是否主BIOS：', bios.PrimaryBIOS)
print('安装日期：', bios.InstallDate)
print('发布日期：', bios.ReleaseDate)
print('序列号：', bios.SerialNumber)
print('BIOS版本：', bios.Version)
