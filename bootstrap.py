import os
import shutil

class PackagePath(object):
    def __init__(self, package_name):
        self.name = package_name

    def generate(self):
        return self.name.replace('.', '/')

class FileOperation(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def make_directory_if_not_exist(self, iter):
        for name in iter:
            path = "%s/%s" % (self.dest, name)
            try:
                os.makedirs(path)
            except OSError, e:
                if e.errno == 17:
                    print "%s already exists, ignoring" % path
        return self

    def copy_file(self, map):
        for srcname, destname in map.iteritems():
            shutil.copyfile("%s/%s" % (self.src, srcname), "%s/%s" % (self.dest, destname))
        return self

if __name__ == '__main__':
    import sys

    try:
        src = os.path.dirname(sys.argv[0])
        dest = sys.argv[1]
        package = sys.argv[2]
    except IndexError:
        print "usage: %s <project path> <package name>" % sys.argv[0]
        sys.exit(1)

    package_path = PackagePath(package).generate()

    FileOperation(src, dest).make_directory_if_not_exist((
        'test/unit/libs',
        'test/unit/src/%s' % package_path
    ))
    FileOperation(src, dest).copy_file({
        "custom_rules.template.xml": "custom_rules.xml",
        "runner-template.properties": "runner.properties",
        "test-unit-build.template.xml": "test/unit/build.xml",
        "test-unit-TestRunner.template.java": "test/unit/src/%s/TestRunner.java" % package_path
    })
    print """\
Test environment has been set up for %(package)s!  Next:
1. Set runner.properties up
2. Fix package name in test/unit/%(package_path)s/TestRunner.java (i.e. x.y.z -> %(package)s)
3. 'ant test-unit-clean' to start unit tests
4. 'ant test-functional-clean' to start functional tests
   (NB. you need to create a test-project beforehand to do this)
""" % dict(package=package, package_path=package_path)
