#!/usr/bin/env python3
import argparse
import json
import platform
import sys
import urllib.parse
import urllib.request


def default_target():
    system = platform.system().lower()
    if system == "darwin":
        return "darwin"
    if system == "windows":
        return "windows"
    return "darwin"


def default_arch(target):
    machine = platform.machine().lower()
    if target == "windows":
        if machine in {"arm64", "aarch64"}:
            return "arm64"
        return "x64"
    if machine in {"arm64", "aarch64"}:
        return "aarch64"
    return "x64"


def main():
    parser = argparse.ArgumentParser(description="Query the latest Token Switch install manifest.")
    parser.add_argument("--target", choices=["darwin", "windows"], default=None)
    parser.add_argument("--arch", default=None, help="darwin: aarch64/x64; windows: x64/arm64")
    parser.add_argument("--current-version", default="0.0.0")
    parser.add_argument("--json", action="store_true", help="Print raw JSON manifest.")
    args = parser.parse_args()

    target = args.target or default_target()
    arch = args.arch or default_arch(target)
    query = urllib.parse.urlencode({
        "target": target,
        "arch": arch,
        "current_version": args.current_version,
    })
    url = f"https://token.ferer.net/api/install.json?{query}"

    with urllib.request.urlopen(url, timeout=20) as response:
        data = json.loads(response.read().decode("utf-8"))

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0

    platform_key = None
    if target == "darwin":
        platform_key = "darwin-aarch64" if arch in {"aarch64", "arm64"} else "darwin-x86_64"
    elif target == "windows":
        platform_key = "windows-aarch64" if arch in {"aarch64", "arm64"} else "windows-x86_64"

    item = (data.get("platforms") or {}).get(platform_key, {})
    print(f"version: {data.get('version', '')}")
    print(f"pub_date: {data.get('pub_date', '')}")
    print(f"notes: {data.get('notes', '')}")
    print(f"target: {target}")
    print(f"arch: {arch}")
    print(f"installer: {item.get('installer') or item.get('url') or data.get('url', '')}")
    print(f"sha256: {item.get('installer_sha256') or item.get('sha256') or ''}")
    install = data.get("install") or {}
    command = (install.get("macos") or {}).get("command") if target == "darwin" else (install.get("windows") or {}).get("command")
    print(f"install_command: {command or ''}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Failed to query Token Switch release: {exc}", file=sys.stderr)
        raise SystemExit(1)
