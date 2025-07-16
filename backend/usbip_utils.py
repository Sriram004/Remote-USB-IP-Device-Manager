import subprocess

def run_cmd(cmd):
    result = subprocess.run(cmd.split(), capture_output=True, text=True)
    return result.stdout.strip()

def list_devices():
    output = run_cmd("usbip list -r localhost")
    return {"devices": output.splitlines()}

def attach_device(ip, busid):
    output = run_cmd(f"usbip attach -r {ip} -b {busid}")
    return {"status": "attached", "output": output}

def detach_device(port):
    output = run_cmd(f"usbip detach -p {port}")
    return {"status": "detached", "output": output}
