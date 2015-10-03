#!/usr/bin/env python
#coding:utf-8

import os
import sys

#获取资源文件
def get_resource():
	print '\nGetting resource...'
	os.system('java -jar %s/apktool_2.0.1.jar d -f -o %s %s' % (_running_path, _apk_resource_folder, _source_apk_path))

#获取java源码
def get_source_code():
	print '\nGetting source code...'
	convert_apk_to_jar()
	convert_jar_to_java()
	delete_tmp_files()

#将apk转化为jar
def convert_apk_to_jar():
	print '****Converting apk to jar...'
	os.system('sh %s/dex2jar-2.1/d2j-dex2jar.sh -f -o %s %s' % (_running_path, _apk_jar, _source_apk_path))

#将jar转化为java代码
def convert_jar_to_java():
	print '****Converting jar to java source code...'
	os.system('java -jar %s/procyon-decompiler-0.5.30.jar -jar %s --verbose 0 -o %s' % (_running_path, _apk_jar, _apk_source_code_folder))

#删除临时文件
def delete_tmp_files():
	print '****Clean temp files...'	
	os.system('rm -rf %s' % _apk_jar)

#让用户输入想要的操作，并做出相应的处理
def process_user_choice():
	print '\n=====================================Operation======================================='
	print '1.Get java source code from apk (with Procyon Java Decompiler)'	
	print '2.Get resource and smali code from apk (with Apktool)'
	print '(Press \'enter\' to get both two mentioned above)'
	print '=====================================================================================\n'
	
	_operation = raw_input('Choose the operation or Press \'enter\' to continue: ')
	
	if _operation == '1':
		get_source_code()
	elif _operation == '2':
		get_resource()
	else:
		get_source_code()
		get_resource()

#确定反编译的输出目录，默认是当前apk所属目录
def get_output_folder():
	if not len(os.path.dirname(_source_apk_path)) == 0:
		return os.path.dirname(_source_apk_path) + '/'
	else:
		return os.path.dirname(_source_apk_path)

#获取要反编译的apk路径
def get_input_apk_path():
	if len(sys.argv) == 1:
		return raw_input('please input the apk\'s path: ')
	else:
		return sys.argv[1]

#获取此脚本所在的路径
_running_path = os.path.split(os.path.realpath(sys.argv[0]))[0]

#初始化相关变量
_source_apk_path = get_input_apk_path()
_output_folder = get_output_folder()
_apk_basename = os.path.basename(_source_apk_path).strip()
_apk_basename_without_ext = os.path.splitext(_apk_basename)[0]
_apk_jar = '%s-dex2jar.jar' % (_output_folder + _apk_basename_without_ext)
_apk_source_code_folder = '%s_source_code' % (_output_folder + _apk_basename_without_ext)
_apk_resource_folder = '%s_resource' % (_output_folder + _apk_basename_without_ext)

process_user_choice()


