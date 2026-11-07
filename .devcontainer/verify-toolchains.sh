#!/usr/bin/env bash

set -euo pipefail

export XDEBUG_MODE=off

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
java_build_dir="$(mktemp -d)"

cleanup() {
    rm -rf -- "$java_build_dir"
}

trap cleanup EXIT

echo "Installed toolchains:"
python --version
node --version
npm --version
php --version | head -n 1
composer --version
java --version | head -n 1
javac --version

expected_output=$'Buddy says woof!\nLuna says woof!\n3\n4'

python_output="$(python "$project_root/python/03/oop.py")"
typescript_output="$(node --disable-warning=ExperimentalWarning --experimental-transform-types "$project_root/typescript/03/oop.ts")"
php_output="$(php "$project_root/php/03/oop.php")"

javac -d "$java_build_dir" "$project_root/java/03/Oop.java"
java_output="$(java -cp "$java_build_dir" Oop)"

assert_output() {
    local language="$1"
    local actual_output="$2"

    if [[ "$actual_output" != "$expected_output" ]]; then
        echo "$language output did not match the expected result." >&2
        echo "Expected:" >&2
        printf '%s\n' "$expected_output" >&2
        echo "Actual:" >&2
        printf '%s\n' "$actual_output" >&2
        return 1
    fi

    echo "$language OOP example: OK"
}

echo
echo "Checking lesson 03/OOP:"
assert_output "Python" "$python_output"
assert_output "TypeScript" "$typescript_output"
assert_output "PHP" "$php_output"
assert_output "Java" "$java_output"

echo
echo "Dev Container verification completed successfully."
