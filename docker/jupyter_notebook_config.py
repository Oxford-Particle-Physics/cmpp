import os
rootbin = '/opt/root/bin'
rootlib = '/opt/root/lib'
os.environ['PYTHONPATH']      = '%s' % rootlib + ':' + os.getenv('PYTHONPATH', '')
os.environ['PATH']            = '%s:%s/bin' % (rootbin,rootbin) + ':' + os.getenv('PATH', '')
os.environ['LD_LIBRARY_PATH'] = '%s' % rootlib + ':' + os.getenv('LD_LIBRARY_PATH', '')
c.NotebookApp.extra_static_paths = ['/opt/root/js/']
c.NotebookApp.allow_remote_access = True
c.NotebookApp.ip = '*'
c.NotebookApp.allow_root = True
c.NotebookApp.open_browser = False
