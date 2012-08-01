Android Runner
================

(C) 2012 Takahiro Yoshimura <altakey@gmail.com>

This is a template to enable ant tasks to run apps and tests...
Supporting Android SDK r20 and later on *nix-alike OSes (e.g. Mac OS X 10.6/10.7/10.8.)


0. INSTALLATION
-----------------

$ git clone git://github.com/taky/android-runner.git
$ mv android-runner /usr/local/android-runner


1. USAGE (basic)
-----------------

$ cp /usr/local/android-runner/custom_rules.template.xml custom_rules.xml
$ vim local.properties
...
runner.dir=/usr/local/android-runner
...
$ vim project.properties
...
runner.activity=MainActivity
...
$ ant run
[Runs on device or emulator, emiting logcat]


2. USAGE (with test project)
-----------------------------

$ mkdir test
$ android create test-project -p test/functional -m ../..
$ vim local.properties
...
runner.dir=/usr/local/android-runner
...
$ vim project.properties
...
runner.test.functional=test/functional/
...
$ vim custom_rules.xml
...
 <import file="${runner.dir}/runner.xml" />
 <import file="${runner.dir}/test-functional.xml" />
</project>
$ ant test-func-clean
[Cleans projects, compiles main project and test project, and runs on device or emulator]


3. USAGE (with custom unit test rules, like Robolectric, Groovy, ...)
-----------------------------------------------------------------------

$ mkdir test/unit
$ vim test/unit/build.xml
...
 <target name="test" depends="compile">
   <junit ...>
 </target>

 <target name="clean">
  <delete dir="bin" />
  ...
 </target>

 <target name="compile">
   <mkdir dir="bin" />
   <javac srcdir="src" destdir="bin" ... />
   ...
   <groovyc srcdir="src" destdir="bin" ... />
   ...
 </target>
...
$ vim local.properties
...
runner.dir=/usr/local/android-runner
...
$ vim project.properties
...
runner.test.unit=test/unit/
...
$ vim custom_rules.xml
...
 <import file="${runner.dir}/runner.xml" />
 <import file="${runner.dir}/test-unit.xml" />
</project>
$ ant test-unit-clean
[Cleans projects, runs unit test rules, and possibly runs test cases on JVM]


4. BUGS
--------

 * Hackish.
 * Cannot run on Windows environments.
