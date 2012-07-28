#/bin/sh
pkg=$1

function intr() {
  adb shell am start -a android.intent.action.MAIN -c android.intent.category.HOME
  exit 0
}

trap intr SIGINT
adb shell am instrument -w ${pkg}/android.test.InstrumentationTestRunner &
adb logcat
