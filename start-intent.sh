#/bin/sh
intent=$1
pkg=$2
activity=$3

function intr() {
  adb shell am start -a android.intent.action.MAIN -c android.intent.category.HOME
  exit 0
}

trap intr SIGINT

adb shell am start -a $intent -n $pkg/$activity &
adb logcat
