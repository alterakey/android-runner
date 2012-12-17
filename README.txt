Android Runner
================

(C) 2012 Takahiro Yoshimura <altakey@gmail.com>

This is a template to enable ant tasks to run apps and tests...
Supporting Android SDK r20 and later on *nix-alike OSes (e.g. Mac OS X 10.6/10.7/10.8.)


0. INSTALLATION
-----------------

# Android SDK r21 and later
$ git clone git://github.com/taky/android-runner.git etc/runner
$ python etc/runner/bootstrap.py . your.package.name
$ vim runner.properties
runner.at=etc/runner
...

# Android SDK r20.0.1
$ git clone -b exp/r20.0.1 git://github.com/taky/android-runner.git etc/runner
$ python etc/runner/bootstrap.py . your.package.name
$ vim runner.properties
runner.at=etc/runner
...

# Android SDK r20
$ git clone -b exp/r20 git://github.com/taky/android-runner.git etc/runner
$ python etc/runner/bootstrap.py . your.package.name
$ vim runner.properties
runner.at=etc/runner
...


1. USAGE (basic)
-----------------

$ vim runner.properties
...
runner.activity=MainActivity
...
$ ant run
[Runs on device or emulator, emiting logcat]


2. USAGE (with test project)
-----------------------------

$ android create test-project -p test/integration -m ../..
$ ant test-integ-clean
[Cleans projects, compiles main project and test project, and runs on device or emulator]

$ android create test-project -p test/functional -m ../..
$ ant test-func-clean
[Cleans projects, compiles main project and test project, and runs on device or emulator]

$ android create test-project -p test/acceptance -m ../..
$ ant test-accept-clean
[Cleans projects, compiles main project and test project, and runs on device or emulator]

3. USAGE (with custom unit test rules, like Robolectric, Groovy, ...)
-----------------------------------------------------------------------

$ ant test-unit-clean
[Cleans projects, runs unit test rules, and possibly runs test cases on JVM]


4. BUGS
--------

 * Hackish.
 * Cannot run on Windows environments.
